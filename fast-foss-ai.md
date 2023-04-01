> I'm a professional developer but an AI amateur, and I don't have the actual resources to implement this. So this is really just brainfood for others trying to move AI forward in the FOSS arena.

One of the problems I've seen is that there is a problem of cost in terms of time, effort and money to create a large corpus of fine-tuning data that can be used to improve the quality of a LLM model.

My suggestion is simple, affordable and I believe has the potential to be cost effective. It involves five steps.

## 1. Start with a completely free model

This can be a a relatively low quality model, as long as it can be trained to train itself.

## 2. Provide a base level of fine tuning - like Alpaca

So that it is possible to add the next level of fine-tuning.

## 3. Train to train

Add an additional set of fine tuning which has the single goal of being able to evaluate the quality of a chat conversation as further training data. **THIS IS THE IMPORTANT PART** It needs to be clear that the goal is a high quality, unbiased etc. conversation where being corrected is acceptable etc.

## 4. Self-Selected Reinforcement Learning

```Please rate the suitability of this conversation as fine tuning data for an AI, out of 10.```

> The above will work on GPT-4 btw.

The idea is that at the end of every conversation the AI Chatbot has, it is asked to evaluate the suitability of the conversation to be added to the training corpus. Only the highest quality conversations are accepted. They are then placed in a public git repository. They can then be scrutinised by interested parties before running in the NEXT round of fine-tuning. 

## 5. Make the chatbot available publicly

So that all the awful and brilliant conversations can take place.

So the idea is, once the AI has passed the point it can evaluate conversations you are not paying a commercial AI to create training data and you are instead using *highly filtered* training data from it's users, where the AI does the actual filtering. I.e. the user does not evaluate the conversation as good or bad, the AI does. And the AI can receive more and more fine tuning to become better at evaluating training data. Also the whole process can be automated, with peer reviewing taking place in the Git repo.


If this is all very obvious, then sorry. I have no real experience in this field, but I'm just looking at what is the stumbling blocks for FOSS AI.


