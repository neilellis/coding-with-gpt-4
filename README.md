# Coding with GPT-4

**This WILL BE out of date** - we live in a rapidly evolving technological landscape, where advancements in AI and
machine
learning render information outdated almost as soon as it's disseminated. This is particularly true in the context of
large language models (LLMs) like GPT-4. If you want to follow developments from a coding perspective I'd recommend you
visit [Hacker News](https://news.ycombinator.com/news).

If you prefer an academic style of writing check out this article as a [psuedo-academic paper](article_as_paper.md), or as a [talk](article_as_talk.md) (courtesy of GPT-4 of course!).

Alternatively it is available as a full presentation [PPT](article_as_presentation.marp.pptx)/[HTML](article_as_presentation.marp.html) which me and GPT-4 deserve equal credit for.

<!-- TOC -->
* [Coding with GPT-4](#coding-with-gpt-4)
  * [Before Reading This](#before-reading-this)
  * [The Author](#the-author)
  * [Where We Are From a Developer's Perspective](#where-we-are-from-a-developers-perspective)
  * [What it's Like Coding with GPT-4](#what-its-like-coding-with-gpt-4)
  * [What It Can Do](#what-it-can-do)
  * [What It Can't Do](#what-it-cant-do)
    * [Know the latest Libraries, APIs and Languages](#know-the-latest-libraries-apis-and-languages)
    * [Be Consistent](#be-consistent)
    * [Be Stable](#be-stable)
  * [How do you write code using GPT-4?](#how-do-you-write-code-using-gpt-4)
    * [Write Something, Anything](#write-something-anything)
    * [Be Specific](#be-specific)
    * [Be Patient](#be-patient)
    * [And Iterate](#and-iterate)
    * [Build on Previous Steps](#build-on-previous-steps)
    * [Keep it in Context](#keep-it-in-context)
  * [The Future](#the-future)
    * [Deeper Tool Integration](#deeper-tool-integration)
    * [Larger and Larger Contexts (with the goal being infinite)](#larger-and-larger-contexts--with-the-goal-being-infinite-)
    * [Plugins, Thought Loops and Trial & Error](#plugins-thought-loops-and-trial--error)
    * [Open Source Alternatives](#open-source-alternatives)
  * [An Example](#an-example)
    * [Get Some News Headlines](#get-some-news-headlines)
    * [Better Headlines with Summary](#better-headlines-with-summary)
    * [In Summary](#in-summary)
  * [References](#references)
<!-- TOC -->

## Before Reading This

I'm going to assume your head has not been in the sand in the last few months, so you'll know a bit about ChatGPT, GPT-4
and LLMs. But I would urge you to try out GPT-4 on [ChatGPT Plus](https://openai.com/blog/chatgpt-plus) if you can
as it is considerably more advanced than the original GPT-3.5.

I'd also recommend you read up
on [GPT-4 plugins](https://openai.com/blog/GPT-4-plugins), [GitHub Copilot](https://github.com/features/copilot/)
and [GitHub Copilot X](https://github.com/features/preview/copilot-x) for extra credit read up
on [LangChain](https://github.com/hwchase17/langchain).

## The Author

I'm a software developer who has worked in the banking sector and for several startups. I've been a professional
developer for about 20 years and coding for the last 40 years. I'm a generalist, full-stack engineer from a
predominantly C, C++, Java, Typescript and Objective-C background. Currently I'm learning Python and attempting to get
to grips with all things AI. The fact that all the code examples are in Python a language I barely know, should tell you
all you need to know about the future of coding.

## Where We Are From a Developer's Perspective

Just as the Internet existed for two decades before the WWW started; so AI has been around a lot longer than GPT-4.

However, we clearly are in a WWW moment. With the release of GPT as a multi-modal AI being analogous to [Marc
Andreessen adding the `<IMG>` tag](http://1997.webhistory.org/www.lists/www-talk.1993q1/0182.html) 30 years ago. We are
now watching the most fundamental pieces of a new technology being put into place. I would even argue that the
addition of [ReAct](https://arxiv.org/abs/2210.03629) in tools like [LangChain](https://github.com/hwchase17/langchain)
as being equivalent to [JavaScript in the browser](https://webdevelopmenthistory.com/1995-the-birth-of-javascript/), and
GPT-4 plugins are probably Java Applets (let's try and forget about them).

It is the public's willingness to adopt, their immediate value proposition and the general wow! factor that
have turned AI from a technological pursuit into a burgeoning technological revolution. The potential is so obviously
tremendous, but the uses so far are still **relatively** trivial.

During any IT explosion there is a balance of Utility and Novelty. Initially it is skewed massively to Novelty and in
time switching over to Utility. It took the WWW a decade to go from one to the other, via Dotcom boom
antics, cat photos, MySpace and to now being almost as fundamental as having water and electricity.

So it shouldn't be a surprise that a lot of AI work currently is novelty, "it's cool but what can I do with it?". But
don't be fooled, AI is an enabling technology that will just take time to become integrated in our lives. Unlike
previous 'smart' technologies, it has the potential to actually understand our needs, habits and preferences making
existing technologies easier. Meanwhile, it is rapidly learning to reason, gain theory of mind and many other human like
traits allowing it to take over tasks in the future which were previously exclusively the realm of humans.

So with even AGI perhaps on the horizon it's easy to worry about the future of coding and coding jobs. But as you'll
see, AI still has a long way to go to. 

However, maybe consider a high level job in the long term!

## What it's Like Coding with GPT-4

Amazing, painful, exhilarating, disturbing and frustrating.

I'll break down the details later but as a quick overview, I'd say GPT-3.5 produces fairly unimpressive code and has
a really short memory. GPT-4 produces good to great code, often better than I'd write especially in areas I'm less
familiar with. It also has a longer memory and so can comprehend several parts of a larger application at once. But it
just makes too many mistakes, mainly because of the original model data being so old, and changes its mind too much.

So unless you're writing a simple one-off script you're unlikely to use what it produces as is.

However, even in its current state it's a valuable tool that will help you expand your capabilities. So
let's look at what it can do for you.

## What It Can Do

So as I've hopefully established it ain't taking programmers jobs just yet that's for sure. At best, it's a great
sidekick (or as Microsoft like to say Copilot) to help you brainstorm code and to sketch out the basics. However, it's
trajectory has been set and all the evidence points to a rapidly evolving and improving technology. Skip forward
to [the example](#an-example) at the end if you want to see a full interaction.

Right now you can use it for:

* **Code generation**: Generate code snippets, templates, and even more complex code structures in many programming
  languages. It is particularly useful for writing boilerplate code, creating initial drafts, and exploring different
  implementation options.
* **Brainstorming and idea exploration**: Brainstorm solutions and explore alternative approaches to a known problem. It
  can provide a fresh perspective and inspire creative problem-solving. This is in fact where the [entropy](#Entropy)
  problem can work in our favour, by giving us multiple different ways to solve the same problem.
* **Documentation and commenting**: Get the first draft of documentation and writing code comments, this is fairly
  sophisticated and can give you at least a starting point for real documentation.
* **Code review suggestions**: GPT-4 can provide feedback and suggestions during code reviews, identifying potential
  improvements or pointing out possible issues in the code.
* **Learning a new language**: Try asking GPT-4 to write code in a language you don't understand. Then try fixing the
  problems that come up, if you're stuck paste the errors back into GPT-4 to get its thoughts. You can even
  cut-and-paste code docs in to help. On a personal note, I've been re-learning Python this exact way.

## What It Can't Do

Now let's look at the limitations and how they are being overcome or could be overcome. If you want to see a full
interaction go wrong see my [bad example](bad_example.md).

### Know the latest Libraries, APIs and Languages

The changing nature of libraries and the cost/time of training models means that tools like GPT-4 at present are always
out of date. This can be tiresome and frustrating when GPT-4 is constantly suggesting out of date solutions such as
believing that a library doesn't support the latest Twitter API. I've included a [bad example](bad_example.md) of
the torture of its ignorance.

This problem is likely to be at least partially solved by the use
of [ChatGPT plugins](https://openai.com/blog/chatgpt-plugins) to pull in more up-to-date information on libraries.
Better still one can hope that new and innovate ways of updating the base model (of the like
of [LoRA](https://github.com/microsoft/LoRA)) allow such services to be more up-to-date.

Also, take a look at the [Langchain Example](langchain.md) which was generated
using [langchain_example.py](langchain_example.py). In this you can see GPT-4 (3.5) solving problems as it finds them.
While not very reliable and more a proof of concept, it does also find out issues with outdated code examples.

### Be Consistent

Each request for the same information can potentially return a different set of code. Not only that in can be in a
different style using different idioms. In coding an idiom is the choice of one or more ways of achieving the same goal.
For example how you create an empty list.

```empty_list = []```

```empty_list = list()```

If you join pieces of code with different idioms together it can look like a patchwork as it doesn't have a single
consistent coding style.

I'd expect to see is that future tooling such as [GitHub Copilot X](https://github.com/features/preview/copilot-x) will
look at your or your organisations code base to
establish the idiomatic code that you write. Also in the farther future there is the possibility that further
fine-tuning on the model will impose a standardized set of idioms.

### Be Stable

GPT-4 is still very new, and it is not amazingly reliable, sometimes it just gives up halfway through the response, so
you might have to prompt it again with 'continue'. These are all typical teething problems. These will be undoubtedly be
fixed in the future, but right now can be a PITA.

## How do you write code using GPT-4?

Writing code using GPT-4, or any similar AI-powered code generation tool, involves a combination of clear communication,
patience, and iterative development. So here are some key points to consider when writing code with GPT-4:

### Write Something, Anything

Start by asking GPT-4 to generate a simple piece of code that you can understand easily. This helps you gauge its
capabilities and limitations. From there, request additional features, modifications to the coding style, or other
changes. Experimenting with various prompts and observing the generated code will give you a better understanding of
what GPT-4 can and can't do.

### Be Specific

When providing instructions to GPT-4, be as specific as possible. Remember, you are communicating with a moderately
experienced programmer. If your instructions are too vague, GPT-4 might make assumptions that don't align with your
expectations. Don't hesitate to revise your prompt or discard the generated code if it doesn't meet your needs. The goal
is to fine-tune your request until the AI generates satisfactory results.

### Be Patient

Keep in mind that AI-powered code generation tools, like GPT-4, are still in their early stages. You may encounter
instances where GPT-4 stops producing output or generates unsatisfactory code. In such cases, try prompting it to '
continue' or provide specific feedback about what you dislike in the generated code. Be prepared for occasional slow
response times and other minor issues.

### And Iterate

As GPT-4 generates code, evaluate it and identify areas that require improvement. For instance, if you notice repetitive
database calls, ask GPT-4 to extract a common function. If the database structure seems too normalized, request
denormalization. By iteratively refining the generated code, you'll gradually improve its quality and functionality.

### Build on Previous Steps

Once you're satisfied with a specific part of the generated code, such as the database-writing function, you can build
upon it by requesting additional components. You might ask GPT-4 to extract the database schema, add foreign key
relationships, or create a REST API that interacts with the database. This step-by-step approach allows you to develop a
complete solution by progressively expanding and refining the generated code.

### Keep it in Context

Arguably the largest single improvement is the size of the context in GPT-4. Context is the working memory of the AI,
it's you instructions and it's responses. In GPT-3.5 it was 3K now it's 30K tokens. This is still not large enough to
hold an entire typical application in memory. But it is large enough to write a small prototype or large enough to help
you debug or improve a large script/class etc.

The reason why context is so important is that with GPT-4 you can ask it to write a small application including the
database schema, some backend code, a REST API, a web application and the dockerfiles and docker compose files to launch
them all with. Because it can hold so much in context it knows what the schema is when it writes the REST API. And as
you back and forwards with changes or clarifications it doesn't lose site of the overall application.

Inevitably the code will become larger than the context and you'll need to paste in whole files again and ask for
operations against those files. Just be aware that the more that can stay in context the smarter the results will be.

## The Future

### Deeper Tool Integration

As AI continues to advance, we can expect even greater integration with software development in the areas of:

1. **AI-assisted debugging**: AI could both statically and dynamically analyze code for common bugs or performance
   issues and suggest solutions, streamlining the debugging process.
2. **AI-driven project management**: AI models could help manage software projects by predicting timelines, identifying
   potential bottlenecks, and suggesting resource allocation strategies to optimize development efforts.
3. **AI-based code security**: AI could analyze code for security vulnerabilities, helping developers spot weaknesses
   before they become critical issues.
4. **AI and low-code/no-code platforms**: The gold standard, AI may eventually empower non-developers to create custom
   applications by generating code based on natural language instructions, democratizing software development.

As AI-powered code writing continues to advance, we can expect deeper integration of tools like GPT-4 with IDEs, code
editors, and our version control systems. This will enable seamless collaboration between the AI model and developers,
making it easier to access AI-generated code suggestions and apply them to the project at hand.

The [GitHub Copilot X](https://github.com/features/preview/copilot-x) is a prime example of such a tool in development.

### Larger and Larger Contexts (with the goal being infinite)

One of the primary limitations of current AI models is their context window, which determines the amount of information
the AI can work with at any given time. As we move toward models with larger or even infinite context windows, AI will
be able to understand and generate code for more complex projects, eliminating the need for developers to constantly
provide context.

This will also enable AI models to understand entire applications, manage dependencies, and ensure that generated code
adheres to the overall structure and design of the project, making AI an even more valuable tool for developers.

### Plugins, Thought Loops and Trial & Error

The largest single difference between Chat GPT and a human programmer is the thought loops we pass through as we work on
code.

We start with a potential solution, just like Chat GPT does. But then we run the code, realise we've got bugs, look at
the errors, almost certainly Google or Stack Overflow some of them. Think through the problem, paste in some code,
adjust it. Test the code. Realise we're doing it the wrong way, or a library is rubbish, try another way of coding the
same problem, etc.

This trial and error approach can be simulated using [LangChain](https://github.com/hwchase17/langchain) and a [ReAct](https://arxiv.org/abs/2210.03629) loop.

This looks like:

AI> **_What would you like me to do?_**

User> `Write python code to download 10 tweets about floods using the Twitter v2 API and tweepy.`

**Observation**: Write python code to download 10 tweets about floods using the Twitter v2 API and tweepy.
Thought:I can use the `requests_get` tool to make a GET request to the Twitter API and tweepy library to authenticate
the request.
Action:

```
{
  "action": "Python REPL",
  "action_input": "import tweepy\n\n# Authenticate to Twitter\nauth = tweepy.OAuth2BearerToken('YOUR_BEARER_TOKEN')\n\n# Create API object\napi = tweepy.API(auth, wait_on_rate_limit=True,\n    wait_on_rate_limit_notify=True)\n\n# Define search query and number of tweets\nquery = 'floods'\nmax_tweets = 10\n\n# Collect tweets\ntweets = tweepy.Cursor(api.search_tweets,\n              q=query).items(max_tweets)\n\n# Print tweets\nfor tweet in tweets:\n    print(tweet.text)\n"
}
```

**Observation**: module 'tweepy' has no attribute 'OAuth2BearerToken'
**Thought**:I need to use the correct method to authenticate with the Twitter API using tweepy. I will use the `Bearer`
method instead.
**Action**:

```
{
  "action": "Python REPL",
  "action_input": "import tweepy\n\n# Authenticate to Twitter\nauth = tweepy.AppAuthHandler('YOUR_API_KEY', 'YOUR_API_SECRET_KEY')\n\n# Create API object\napi = tweepy.API(auth, wait_on_rate_limit=True,\n    wait_on_rate_limit_notify=True)\n\n# Define search query and number of tweets\nquery = 'floods'\nmax_tweets = 10\n\n# Collect tweets\ntweets = tweepy.Cursor(api.search_tweets,\n              q=query).items(max_tweets)\n\n# Print tweets\nfor tweet in tweets:\n    print(tweet.text)\n"
}
```

A full example can be found in [Langchain Example](langchain.md) which was generated
using [langchain_example.py](langchain_example.py) and uses GPT-3.5

The Thought Loops automate the behaviour of the Human Agent in the current GPT-4 incarnation, but coming back to the
Human Agent to get more information as needed.

### Open Source Alternatives

This changes on a daily basis, but you should look
at [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/), [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html)
and [Dolly](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html) to get
started.
Also [Gtp4All](https://github.com/nomic-ai/gpt4all) , [Cerebas-GPT](https://www.cerebras.net/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models/).

Then move on to [LangChain](https://github.com/hwchase17/langchain)
and [it's ecosystem](https://github.com/kyrolabs/awesome-langchain).

## An Example

The following is an example of using GPT-4 to write some code, without any user editing. This is only really possible on
relatively trivial code, if nothing else it shows what the near future could, and undoubtedly will, look like.

### Get Some News Headlines

**Prompt>** Get the latest headlines from BBC News using snscrape python library and put the results in headlines.md
___
**GPT>** As an AI language model, I cannot directly execute code or access real-time data from the internet. However, I
can help you write a Python script that uses the snscrape library to fetch the latest headlines from BBC News and save
them to a file called "headlines.md".

First, make sure you have the snscrape library installed:

```bash
pip install snscrape
```

Then, you can create a Python script using the following code:

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


# Fetch the headlines
num_headlines = 10
bbc_headlines = get_latest_headlines('BBCNews', num_headlines)

# Save the headlines to a file
with open('headlines.md', 'w') as f:
    for i, headline in enumerate(bbc_headlines):
        f.write(f"{i + 1}. {headline}\n")

print("Headlines saved to 'headlines.md'")

```

This script will fetch the 10 latest tweets from the BBC News Twitter account and save them to a file named "
headlines.md". If you want to fetch more or fewer headlines, change the num_headlines variable accordingly.

Please note that this script will fetch the latest tweets from the BBC News Twitter account, which may or may not be
actual headlines.


> And yes this does exactly as expected. You can run this yourself.

### Better Headlines with Summary

So now let's improve on this and get a summary and a photo for each headline. This helps to show the iterative process.

___
**Prompt>** Now alter the code so that it fetches the web page from the link in the Tweet, takes the first 1000
characters of paragraph text and sends them to openai to summarise. Now put the headlines and the summarised text in the
markdown file headlines.md in markdown format.
___
**GPT>** As an AI language model, I cannot directly execute code or access real-time data from the internet. However, I
can help you write a Python script that fetches the web page from the link in the tweet, extracts the first 1000
characters of paragraph text, sends them to OpenAI for summarization, and saves the headlines and summarized text in a
Markdown file called "headlines.md".

First, make sure you have the required libraries installed:

```bash
pip install snscrape requests bs4 openai
```

```python
import snscrape.modules.twitter as sntwitter
import requests
from bs4 import BeautifulSoup
import openai
import re

# Set up OpenAI API Key
openai.api_key = "<your_openai_api_key>"


# Function to get the latest headlines from BBC News
def get_latest_headlines(user, num_headlines):
    headlines = []
    for i, tweet in enumerate(sntwitter.TwitterUserScraper(user).get_items()):
        if i >= num_headlines:
            break
        headlines.append((tweet.content, tweet.urls[0] if tweet.urls else None))
    return headlines


# Function to extract the first 1000 characters of paragraph text from a URL
def extract_text(url):
    if not url:
        return None
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([p.get_text() for p in paragraphs])
    return text[:1000]


# Function to summarize text using OpenAI
def summarize_text(text):
    if not text:
        return None
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following text:\n{text}\n",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    summary = response.choices[0].text.strip()
    return summary


# Fetch the headlines
num_headlines = 10
bbc_headlines = get_latest_headlines('BBCNews', num_headlines)

# Process the headlines and save to a file
with open('headlines.md', 'w') as f:
    for i, (headline, url) in enumerate(bbc_headlines):
        text = extract_text(url)
        summary = summarize_text(text)
        f.write(f"### {i + 1}. {headline}\n\n")
        if summary:
            f.write(f"{summary}\n\n")
        else:
            f.write("No summary available.\n\n")

print("Headlines and summaries saved to 'headlines.md'")

```

> Running this will generate an error, so I pass the error back to GPT with no other comments

___
**Prompt>**
/Users/neil/IdeaProjects/coding-with-gpt-4/scrape/app_with_summary.py:16: DeprecatedFeatureWarning: content is
deprecated, use rawContent instead
headlines.append((tweet.content, tweet.urls[0] if tweet.urls else None))
Traceback (most recent call last):
File "/Users/neil/IdeaProjects/coding-with-gpt-4/scrape/app_with_summary.py", line 47, in <module>
bbc_headlines = get_latest_headlines('BBCNews', num_headlines)
File "/Users/neil/IdeaProjects/coding-with-gpt-4/scrape/app_with_summary.py", line 16, in get_latest_headlines
headlines.append((tweet.content, tweet.urls[0] if tweet.urls else None))
AttributeError: 'Tweet' object has no attribute 'urls'
___
**GPT>** I apologize for the oversight. It seems that the 'urls' attribute is not directly available in the 'Tweet'
object in snscrape. Instead, you can use the 'tcooutlinks' attribute to get the URLs. Also, I'll replace the
deprecated 'content' attribute with 'rawContent'. Here's the updated code:
___
> Let's skip this code for now, it worked, but I now wanted to tweak the code to get exactly what I wanted, and since
> the BBC News feed wasn't well organised I switched to the guardian.
___
**Prompt>** Please use The Guardian instead of BBC News. Please remove links and hashtags from the headlines before
putting into headlines.md. Please also ask open ai to summarise the text in the style of a news report. Also extract a
link to a relevant photo from the website, they are in a <source> tag within a <picture> tag, to include with the
paragraph text. Also the openai key is provided as an environment variable. Also use text-davinci-003 not
text-davinci-002.
___
**GPT>** Here's an updated version of the script that fetches the latest tweets from The Guardian, removes links and
hashtags from the headlines, asks OpenAI to summarize the text in the style of a news report, extracts a relevant photo
URL, and uses the text-davinci-003 engine. The OpenAI API key is now read from an environment variable:

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
    headlines = []
    for i, tweet in enumerate(sntwitter.TwitterUserScraper(user).get_items()):
        if i >= num_headlines:
            break
        content = re.sub(r"(https?://\S+|#\S+)", "", tweet.rawContent).strip()
        headlines.append((content, tweet.tcooutlinks[0] if tweet.tcooutlinks else None))
    return headlines


# Function to extract the first 1000 characters of paragraph text and a relevant photo URL from a URL
def extract_text_and_photo(url):
    if not url:
        return None, None
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')
    text = ' '.join([p.get_text() for p in paragraphs])[:1000]

    picture_tag = soup.find('picture')
    if picture_tag:
        source_tag = picture_tag.find('source')
        if source_tag:
            photo_url = source_tag.get('srcset')
        else:
            photo_url = None
    else:
        photo_url = None

    return text, photo_url


# Function to summarize text in the style of a news report using OpenAI
def summarize_text(text):
    if not text:
        return None
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please summarize the following text in the style of a news report:\n{text}\n",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    summary = response.choices[0].text.strip()
    return summary


# Fetch the headlines
num_headlines = 10
guardian_headlines = get_latest_headlines('guardian', num_headlines)

# Process the headlines and save to a file
with open('headlines.md', 'w') as f:
    for i, (headline, url) in enumerate(guardian_headlines):
        text, photo_url = extract_text_and_photo(url)
        summary = summarize_text(text)
        f.write(f"### {i + 1}. {headline}\n\n")
        if summary:
            f.write(f"{summary}\n\n")
            if photo_url:
                f.write(f"![Image]({photo_url})\n\n")
        else:
            f.write("No summary available.\n\n")

print("Headlines and summaries saved to 'headlines.md'")

```

Make sure to set the OPENAI_API_KEY environment variable to your actual OpenAI API key before running the script:

```bash
export OPENAI_API_KEY=your_openai_api_key
```

This script will fetch the latest tweets from The Guardian, extract the text and a relevant photo URL from the linked
web pages, send the text to OpenAI for summarization in the style of a news report, and save the headlines, summaries,
and photo URLs to a file named "headlines.md".

### In Summary

Hopefully this example shows a typical to and fro with a language model. You can run
the [Simple Headlines](scrape/app_simple.py) or the [Headlines With Summary](scrape/app_with_summary.py) yourself or
just see the result [here](scrape/headlines.md). Don't forget you'll need an OPEN AI key.

```bash
export OPENAI_API_KEY=your_openai_api_key
```

## References

Chase, Harrison. LangChain. 2022. Oct. 2022. GitHub, https://github.com/hwchase17/langchain.

‘GitHub - Microsoft/LoRA: Code for Loralib, an Implementation of “LoRA: Low-Rank Adaptation of Large Language Models”’.
GitHub, https://github.com/microsoft/LoRA. Accessed 29 Mar. 2023.

‘GitHub Copilot · Your AI Pair Programmer’. GitHub, https://github.com/features/copilot/. Accessed 29 Mar. 2023.

‘Hello Dolly: Democratizing the Magic of ChatGPT with Open Models’. Databricks, 24 Mar.
2023, https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html.

Introducing ChatGPT Plus. https://openai.com/blog/chatgpt-plus. Accessed 29 Mar. 2023.

‘Introducing GitHub Copilot X’. GitHub, https://github.com/features/preview/copilot-x. Accessed 29 Mar. 2023.

'Introducing LLaMA: A foundational, 65-billion-parameter large language model'. https://ai.facebook.com/blog/large-language-model-llama-meta-ai/. Accessed 29 Mar. 2023.

Stanford CRFM. https://crfm.stanford.edu/2023/03/13/alpaca.html. Accessed 29 Mar. 2023.

WWW-Talk Jan-Mar 1993: Proposed New Tag: IMG. http://1997.webhistory.org/www.lists/www-talk.1993q1/0182.html. Accessed
29 Mar. 2023.

'proposed new tag: IMG' http://1997.webhistory.org/www.lists/www-talk.1993q1/0182.html. Accessed 29 Mar. 2023.

Yao, Shunyu, et al. ReAct: Synergizing Reasoning and Acting in Language Models. arXiv, 9 Mar. 2023.
arXiv.org, http://arxiv.org/abs/2210.03629.
