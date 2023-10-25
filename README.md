# Latent Space Activation

There have been many papers such as "Take a Deep Breath" "Step Back" and "Let's think through this step by step" and I noticed that no one has yet generalized what's going on with the models. Why do these techniques work and how can you generalize them more broadly?

This repo is here to demonstrate a few techniques that you can use to activate latent space (embedded knowledge and abilities within the models). 

The first thing to know is that LLMs have vast amounts of knowledge and capabilities embedded in the networks. Most people seem to expect them to magically pop out correct answers and abilities on the first go with inadequate context. But this is setting the bar way higher than human intelligence. What most ML scientists don't know about the brain is that there are hundreds (if not thousands) of parallel processes and sequences that spool up correct answers. Not only that, the longer you work on a problem, the more relevant information gets recruited into "working memory". This can be approximated with iterative retrieval or activation of latent knowledge. Furthermore, the LLM "knows" how to tackle many problems, but like humans, it helps to stop and think for a moment about how to address a problem. 

This is the nature of my work on cognitive architecture - how to create patterns that can do all this automatically without needing manual prompts. However, in order to get consistent performance in a more straightforward manner, you can also use static prompts. 

## Technique 1: Iterative Dialog

Ever "talk through a problem" to yourself? Either out loud or in your head? What you're doing here is using several neurocognitive techniques to prime your brain to recall relevant facts and procedures to solve a problem or answer a question. Let's lay out a series of possible questions that you might use to approach any such problem and then demonstrate how you can use the ChatGPT API, with it's intrinsic dialog handling capabilities, to approximate the same:

```markdown
Main Question: Who was emperor during the absolute apogee of Roman power?

Dialog 1: Well, first I need to think about Rome in general. What do I know about Rome that is relevant?

Dialog 2: Next, maybe I need to figure out how I define the answer. What criteria am I looking to judge on?

Dialog 3: Based on all this, what can I answer?
```

You can see this method implemented in the first experiment `technique01_dialog.py`. To use this, just run it, ask a question, and you will see the internal dialog process. This is aided by `system01_dialog.txt` which is not strictly necessary - you could simply use prompt chaining and an ordinary conversation to achieve the same or similar results. 