import re
import openai
from time import time, sleep
from halo import Halo
import textwrap
import yaml


###     file operations


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)



def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()


###     API functions


def chatbot(conversation, model="gpt-4", temperature=0, max_tokens=2000):
    max_retry = 7
    retry = 0
    while True:
        try:
            spinner = Halo(text='Thinking...', spinner='dots')
            spinner.start()
            
            response = openai.ChatCompletion.create(model=model, messages=conversation, temperature=temperature, max_tokens=max_tokens)
            text = response['choices'][0]['message']['content']

            spinner.stop()
            
            return text, response['usage']['total_tokens']
        except Exception as oops:
            print(f'\n\nError communicating with OpenAI: "{oops}"')
            exit(5)


def chat_print(text):
    formatted_lines = [textwrap.fill(line, width=120, initial_indent='    ', subsequent_indent='    ') for line in text.split('\n')]
    formatted_text = '\n'.join(formatted_lines)
    print('\n\n\nCHATBOT:\n\n%s' % formatted_text)


if __name__ == '__main__':
    openai.api_key = open_file('key_openai.txt').strip()
    
    main_question = input('What is your main query or question? ')
    
    prompts = [
  'What information do I already know about this topic? What information do I need to recall into my working memory to best answer this?',
  'What techniques or methods do I know that I can use to answer this question or solve this problem? How can I integrate what I already know, and recall more valuable facts, approaches, and techniques?',
  'And finally, with all this in mind, I will now discuss the question or problem and render my final answer.',]
    conversation = list()
    conversation.append({'role': 'system', 'content': open_file('system01_dialog.txt')})

    for p in prompts:
        conversation.append({'role': 'user', 'content': p})
        print('\n\n\nUSER: %s' % p)
        response, tokens = chatbot(conversation)
        conversation.append({'role': 'assistant', 'content': response})
        print('\n\n\nCHATBOT:\n%s' % response)
    
    a = input('Press enter to end.')