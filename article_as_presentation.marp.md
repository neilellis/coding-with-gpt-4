---
marp: true
theme: default
paginate: true
_class: lead
---

# AI in Software Development

Hey everyone, my name is Neil Ellis! I'm glad to share my experiences with you today, diving into the world of AI, specifically focusing on ChatGPT, GPT-4, and large language models. Everything I'm talking about today is available on GitHub https://github.com/neilellis/coding-with-gpt-4, this talk is a summary of the main article in the repo.

<!-- Hey everyone! I'm very glad to share my experiences with you today, diving into the world of coding with AI,
specifically focusing on ChatGPT, GPT-4, and large language models. We'll explore their potential in the realm of software development and how
they're changing the way we write code.

Everything I'm talking about today is available on GitHub https://github.com/neilellis/coding-with-gpt-4, this talk is a
summary of the main article in the repo. It was edited for brevity mostly by GPT-4 of course.
-->
---

### Who Am I?

I'm a software developer who has worked in the banking sector and for several startups. I've been a professional developer for about 20 years.

<!--
I'm a software developer who has worked in the banking sector and for several startups. I've been a professional developer for about 20 years and coding for the last 40 years. I'm a generalist, full-stack engineer from a predominantly C, C++, Java, Typescript and Objective-C background. Currently I'm being taught Python by GPT-4.
-->

---

### A brief history of AI in software development

AI has been around for quite some time, but with the advent of GPT-4, we're experiencing a "WWW moment" – a critical turning point that's transforming AI from a niche field to a widespread technological revolution. This moment is akin to the introduction of the `<IMG>` tag 30 years ago, which fundamentally changed the World Wide Web.

<!--

AI has been around for quite some time, but with the advent of GPT-4, we're experiencing a "World Wide Web moment" – a critical
turning point that's transforming AI from a niche field to a widespread technological revolution. The release of GPT-4 and it's multi-modal model
is akin to the introduction of the `<IMG>` tag 30 years ago, which fundamentally changed the World Wide Web from novelty to
consumer facing technology.

The rapid advancement of AI has generated tremendous excitement, and while its initial impact has been characterized by
novelty, AI's potential for utility is undoubtedly vast. Just as the Internet evolved over time from a toy to become a
fundamental aspect of modern life, AI is poised to follow a similar trajectory.
-->
---

### The impact of AI on software development

As a software developer I've seen firsthand how AI can be both amazing and frustrating. GPT-4, for instance, can generate good to great code, especially in areas where I'm less familiar. However, it still makes too many mistakes and changes its mind too much, making it unsuitable for use without human supervision.

<!--
As a software developer I've seen firsthand how AI can be both amazing and
frustrating. GPT-4, for instance, can generate good to great code, especially in areas where I'm less familiar. However,
it still makes too many mistakes and changes its mind too much, making it unsuitable for use without human supervision.
-->

---

### Opportunites and benefits of AI in software development

1. Rapid prototyping
2. Exploring alternative solution
3. Documentation and commenting
4. Code reviews

<!-- 
That said, AI is an invaluable tool for expanding our capabilities. Here are some areas where AI-powered tools like
GPT-4 shine:

1. **Rapid prototyping**: AI can help generate code snippets, templates, and even more complex code structures, speeding
   up the development process.
2. **Exploring alternative solutions**: AI can generate multiple solutions to a problem, providing fresh perspectives
   and inspiring creative problem-solving.
3. **Documentation and commenting**: AI can assist with drafting documentation and writing code comments, serving as a
   starting point for more polished work.
4. **Code review**: AI can offer feedback and suggestions during code reviews, identifying potential improvements or
   pointing out possible issues.
-->

---

### Challenges and limitations of AI in software development

Despite its potential, AI has limitations that need to be addressed to make it a more reliable tool for developers:

1. Outdated libraries and APIs
2. Inconsistency
3. Reliability

<!--

Despite its potential, AI has limitations that need to be addressed to make it a more reliable tool for developers:

1. **Outdated libraries and APIs**: AI models are not always up-to-date with the latest libraries and APIs, which can
   lead to frustration when outdated solutions are suggested. This problem could be mitigated through the use of ChatGPT
   plugins, ReAct style feedback loops or innovative model updating techniques such as LoRA.
2. **Inconsistency**: AI-generated code may not have a consistent style or follow the same idioms, making the resulting
   code look like a patchwork. Future tools like GitHub Copilot X could learn from an organization's codebase to
   generate code that follows more consistent patterns.
3. **Reliability**: AI models like GPT-4 are still in their infancy and may not always generate satisfactory code.
   Patience and persistence are key when working with AI to refine its output.

-->

---

### Best practices for working with AI in software development

When using AI to write code, consider the following best practices:

1. Start simple
2. Be specific
3. Be patient
4. Iterate
5. Leverage context

<!--

1. **Start simple**: Begin with a basic code snippet to gauge the AI's capabilities and limitations before building on
   it.
2. **Be specific**: Provide clear and precise instructions to the AI to minimize miscommunication and incorrect
   assumptions.
3. **Be patient**: Expect occasional slow response times and minor issues while using AI tools in their early stages.
4. **Iterate**: Refine the AI-generated code to improve its quality and functionality progressively.
5. **Leverage context**: Take advantage of the AI's working memory to maintain a holistic understanding of the code,
   leading to smarter results. The less it has to remember the better job it tends to do.

-->
---

### The future of AI in software development

As AI continues to advance, we can expect even greater integration with software development. Some potential future developments include:

1. Improved models
2. AI-assisted debugging
3. AI-driven project management
4. AI-based code security
5. AI and low-code/no-code platforms

<!--
As AI continues to advance, we can expect even greater integration with software development. Some potential future
developments include:

1. **Improved models**: As AI models like GPT-4 continue to evolve, we can anticipate better performance, increased
   accuracy, and fewer mistakes.  With a large or unbounded context the AI will be able to comprehend the relationship between more
   parts of your code base. The more developers use and interact with these models, the more they'll improve.
2. **AI-assisted debugging**: AI could both statically and dynamically analyze code for common bugs or performance
   issues and suggest solutions, streamlining the debugging process.
3. **AI-driven project management**: AI models could help manage software projects by predicting timelines, identifying
   potential bottlenecks, and suggesting resource allocation strategies to optimize development efforts.
4. **AI-based code security**: AI could analyze code for security vulnerabilities, helping developers spot weaknesses
   before they become critical issues.
5. **AI and low-code/no-code platforms**: The gold standard, AI may eventually empower non-developers to create custom
   appl
-->
--- 

## An example

The following is an example of using GPT-4 to write some code, without any user editing. This is only really possible on relatively trivial code, if nothing else it shows what the near future could, and undoubtedly will, look like.

<!--
The following is an example of using GPT-4 to write some code, without any user editing. This is only really possible on relatively trivial code, if nothing else it shows what the near future could, and undoubtedly will, look like.
-->

---

**User>** Get the latest headlines from BBC News using snscrape python library and put the results in headlines.md

<!-- 
First I ask for a basic python app that uses snscrape to scrape Twitter
-->

---

**AI>** ...preamble...

First, make sure you have the snscrape library installed:

```bash
pip install snscrape
```

<!-- 
After the usual disclaimer and pre-amble from GPT it asks me to install snscrape, which I do.
-->
---


**AI>** Then, you can create a Python script using the following code:

```python
import snscrape.modules.twitter as sntwitter
import datetime
import os


# Function to get the latest headlines from BBC News
def get_latest_headlines(user, num_headlines):
    headlines = []
    for i, tweet in enumerate(sntwitter.TwitterUserScraper(user).get_items()):
        if i >= num_headlines:
            break
        headlines.append(tweet.content)
    return headlines

...

print("Headlines saved to 'headlines.md'")

```

<!-- 
    ChatGPT returns me the complete Python script I need, as you can see. The full script, not shown here, performs exactly as expected, producing a simple list of headlines in the markdown file.
-->

---

### Iterate on the design

So now let's improve on this and get a summary and a photo for each headline. 

<!--
So now let's improve on this and get a summary and a photo for each headline. This will help to show the iterative process of working with GPT.
-->

___

**User>** Now alter the code so that it fetches the web page from the link in the Tweet, takes the first 1000 characters of paragraph text and sends them to openai to summarise. Now put the headlines and the summarised text in the markdown file headlines.md in markdown format.

**AI>** ...preamble... 

First, make sure you have the required libraries installed:

```bash
pip install snscrape requests bs4 openai
```

<!--
I start by increasing my requirements to include a summary, using OpenAI to summarize.

I'm prompted to install some more libraries, which I do.
-->

---


```python
import snscrape.modules.twitter as sntwitter

...

# Function to get the latest headlines from BBC News
def get_latest_headlines(user, num_headlines):
    headlines = []
    for i, tweet in enumerate(sntwitter.TwitterUserScraper(user).get_items()):
        if i >= num_headlines:
            break
        headlines.append((tweet.content, tweet.urls[0] if tweet.urls else None))
    return headlines

...
```
<!--
I run the new code and it generates an error, so I pass the error back to GPT with no other comments
-->

---

**Prompt>**
```
/Users/neil/IdeaProjects/coding-with-gpt-4/scrape/app_with_summary.py:16: DeprecatedFeatureWarning: content is
deprecated, use rawContent instead
headlines.append((tweet.content, tweet.urls[0] if tweet.urls else None))
Traceback (most recent call last):
File "/Users/neil/IdeaProjects/coding-with-gpt-4/scrape/app_with_summary.py", line 47, in <module>
bbc_headlines = get_latest_headlines('BBCNews', num_headlines)
File "/Users/neil/IdeaProjects/coding-with-gpt-4/scrape/app_with_summary.py", line 16, in get_latest_headlines
headlines.append((tweet.content, tweet.urls[0] if tweet.urls else None))
AttributeError: 'Tweet' object has no attribute 'urls'
```


<!--
GPT apologises and gives the new code. I realise I want to make a few tweaks though.
-->

___

### New requirements

**Prompt>** Please use The Guardian instead of BBC News. Please remove links and hashtags from the headlines before putting into headlines.md. Please also ask open ai to summarise the text in the style of a news report. Also extract a link to a relevant photo from the website, they are in a <source> tag within a <picture> tag, to include with the paragraph text. Also the openai key is provided as an environment variable. Also use text-davinci-003 not text-davinci-002.

<!-- 
    Don't try and read the whole prompt here. Basically I now update my requirements to use the Guardian not BBC News website, clean up the headlines and include both an image and a summary in the style of a news report. 
-->
___

```python
import os
import snscrape.modules.twitter as sntwitter
import requests
from bs4 import BeautifulSoup
import openai
import re

# Set up OpenAI API Key
openai.api_key = os.environ["OPENAI_API_KEY"]


# Function to get the latest headlines from The Guardian
def get_latest_headlines(user, num_headlines):
  
...

# Function to extract the first 1000 characters of paragraph text and a relevant photo URL from a URL
def extract_text_and_photo(url):
...  


# Function to summarize text in the style of a news report using OpenAI
def summarize_text(text):
...

# Fetch the headlines
guardian_headlines = get_latest_headlines('guardian', 10)

# Process the headlines and save to a file
with open('headlines.md', 'w') as f:
...
print("Headlines and summaries saved to 'headlines.md'")

```

<!-- 
GPT obliges and gives me a 100% functional script that does exactly what I asked for.
-->

---

![bg contain](headlines.png)


<!--
This script does indeed fetch the latest tweets from The Guardian, extract the text and a relevant photo URL from the
linked web pages. It sends the text to OpenAI for summarization in the style of a news report. Then saves the headlines, 
summaries, and photo URLs to a file named "headlines.md". 

You can get the generated source code in the GitHub repo.

And indeed the headlines.md file looks like this ...
-->


---

### The future, today

Let's take a look at what the (fairly near) future might look.

This was my conversation with GPT-3.5 + [LangChain](https://github.com/hwchase17/langchain) + [ReAct](https://react-lm.github.io).

This shows the usual development loop with ChatGPT but now ChatGPT has some agency and plugins.

<!--

So now let's take a look at what the (fairly near) future might look.

The following was a conversation I had with GPT-3.5 + LangChain + ReAct.

This shows the usual development loop with ChatGPT but now ChatGPT has some agency and plugins.

-->

---

**AI**> *What would you like me to do?*

**User**> `Write python code to download 10 tweets about floods using the Twitter v2 API and tweepy.`

**Observation**: Write python code to download 10 tweets about floods using the Twitter v2 API and tweepy.

**Thought**: I can use the `requests_get` tool to make a GET request to the Twitter API and tweepy library to authenticate the request.

**Action**:

```
{
  "action": "Python REPL",
  "action_input": "... Python code ..."
}
```
<!--
As you can see we now don't have a simple to and fro between user and AI like with ChatGPT.
The AI can start conversations, have chains of thought and agency, it's not just waiting for input.

We see Thoughts as the AI figures out its next action, sometimes these thought and action loops can be quite long, 
in this example not-so-much.
-->
---

**Observation**: module 'tweepy' has no attribute 'OAuth2BearerToken'

**Thought**:I need to use the correct method to authenticate with the Twitter API using tweepy. I will use the `Bearer`
method instead.

**Action**:

```
{
  "action": "Python REPL",
  "action_input": "... Python code ..."
}
```
<!--

The AI continues to figure out how to use Twitter. It has a decent first stab.

-->
---
**Observation**: Expected token_type to equal "bearer", but got None instead

**Thought**: There seems to be an issue with the authentication. I will check the API keys and try again.

**Action**:

```
{
  "action": "Human",
  "action_input": "Can you please provide me with the correct API key and secret key for the Twitter API?"
}
```
<!-- 
That fails, so it now asks me for the API Key and secret to connect to the Twitter API.
-->

---
**AI**> *Can you please provide me with the correct API key and secret key for the Twitter API?*

**User**>`Use bearer token instead`

**Observation**: Use bearer token instead

**Thought**: The human provided me with a bearer token instead of API keys. I will modify the authentication code to use the bearer token instead.

**Action**:

```
{
  "action": "Python REPL",
  "action_input": "import tweepy
    auth = tweepy.AppAuthHandler('YOUR_BEARER_TOKEN', '')
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)      
    query = 'floods'
    max_tweets = 10  
    tweets = tweepy.Cursor(api.search_tweets, q=query).items(max_tweets)
    for tweet in tweets:
        print(tweet.text)"
}
``` 
<!-- 
But I want to use a bearer token instead, so I tell it. It adjusts the code, but it doesn't actually have a valid token yet.
-->
---
**Observation**: Expected token_type to equal "bearer", but got None instead

**Thought**: There still seems to be an issue with the authentication. I will check the bearer token and try again.

**Action**:

```
{
  "action": "Human",
  "action_input": "Can you please confirm that the bearer token is correct?"
}
```
<!--
 It gets an error, and to solve the problem it decides to ask me if the bearer token is valid.
-->
---

**AI**> *Can you please confirm that the bearer token is correct?*

**User**> `<twitter-bearer-token>`

**Observation**: <twitter-bearer-token>

**Thought**: It seems like the bearer token provided has some special characters that need to be properly encoded. I will modify the authentication code to include the encoded bearer token.

**Action**:

```
{
  "action": "Python REPL",
  "action_input": "... Python code ..."
}
```

<!-- 

I then reply with a valid bearer token, which it correctly understands as being one, notices some characters need to be escaped and uses it.

-->

---


**Observation**:

```json
{
  "data": [
    {
      "edit_history_tweet_ids": [
        "1640699294465527808"
      ],
      "id": "1640699294465527808",
      "text": "RT @Greenisamissio1: When the sun floods the forest with its light, birds chirp, and the silence in the morning has much to tell you, the d\u2026"
    },
    {
      "edit_history_tweet_ids": [
        "1640699275817496577"
      ],
      "id": "1640699275817496577",
      "text": "Following the river on the way to Liege - lists of evince of restoration and reconstruction after the floods https://t.co/L0ZMNGlH5a"
    },
    ...
```
<!-- 
And now we have the correct result, just as we asked.

If you want to see some silliness with paperclips there's another example in this repo where I ask the AI to do the one thing we mustn't ask.
-->
---

```python
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI


llm = ChatOpenAI(model='gpt-3.5-turbo',temperature=0.5)
tools = load_tools(['python_repl', 'requests', 'terminal', 'serpapi', 'wikipedia', 
                    'human',  'pal-math', 'pal-colored-objects'], llm=llm)

agent = initialize_agent(tools, llm, agent="chat-zero-shot-react-description", 
                         verbose=True)

agent.run("Ask the human what they want to do")

```
<!--
The code I used for this is pretty simple with most of the heavy lifting done by LangChain.
-->

---

### Final thoughts

AI's role in software development is rapidly evolving, and while it may not replace developers entirely, it will undoubtedly redefine the way we write code. By embracing AI's potential and understanding its limitations, we can work alongside these powerful tools to create more efficient, innovative, and secure software solutions.

<!--
AI's role in software development is rapidly evolving, and while it may not replace developers entirely, it will
undoubtedly redefine the way we write code. By embracing AI's potential and understanding its limitations, we can work
alongside these powerful tools to create more efficient, innovative, and secure software solutions.

The journey has just begun, and I believe the key to success is collaboration between humans and AI. As software
developers, we should remain curious and open to the possibilities that AI offers, while always maintaining a critical
eye on its output. In the end, our collective expertise will drive AI to become an indispensable tool in the software
development process.
-->
---

### References

Thank you for your time!

Everything in this talk, including references, source code and full transcripts are in the repo: 

https://github.com/neilellis/coding-with-gpt-4

<!--

Thank you for your time, I hope this short presentation has given you a taste for what we can do with the new generation
of AIs. Even if you already played with ChatGPT I urge you to try ChatGPT-4 and if you've used ChatGPT-4 I urge you to 
play with LangChain.

Everything in this talk, including references, source code and full transcripts are in the repo. 
-->
