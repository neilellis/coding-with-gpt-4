# ChatGPT and the Future of AI-Powered Code Writing

**This is out of date** - we live in a rapidly evolving technological landscape, where advancements in AI and machine
learning render information outdated almost as soon as it's disseminated. This is particularly true in the context of
large language models (LLMs) like ChatGPT.

## Before Reading This File

I'm going to assume your head has not been in the sand in the last few months, so you'll know a bit about ChatGPT and
LLMs. But I would urge you to try out ChatGPT4 on GPTPlus if you can as it is considerably more advanced than the
original ChatGPT.

I'd also recommend you read up
on [ChatGPT plugins](https://openai.com/blog/chatgpt-plugins), [GitHub Copilot](https://github.com/features/copilot/)
and [GitHub Copilot X](https://github.com/features/preview/copilot-x) for extra credit read up
on [Langchain](https://github.com/hwchase17/langchain).

## What ChatGPT Can Do

Well it's not going to take away programmers jobs just yet. At best, it's a great sidekick to help you brainstorm code
and to sketch out the basics. However, it's trajectory has been set and all the evidence points to a rapidly evolving
and improving tool.

So let's look at what we can use it for:

* **Code generation**: Generate code snippets, templates, and even more complex code structures in various programming
  languages. It is particularly useful for writing boilerplate code, creating initial drafts, and exploring different
  implementation options.
* **Brainstorming and idea exploration**: Brainstorm solutions and explore alternative approaches to a known problem. It
  can provide a fresh perspective and inspire creative problem-solving. This is in fact where the [entropy](#Entropy)
  problem can work in our favour, be giving us multiple different ways to solve the same problem.
* **Documentation and commenting**: Get the first draft of documentation and writing code comments, this is fairly
  sophisticated and can give you at least a starting point for real documentation.
* **Code review suggestions**: ChatGPT can provide feedback and suggestions during code reviews, identifying potential
  improvements or pointing out possible issues in the code.
* **Learning a new language**: Try asking ChatGPT to write code in a language you don't understand. Then try fixing the
  problems that come up, if you're stuck paste the errors back into ChatGPT to get its thoughts. On a personal note,
  I've been re-learning Python this exact way.

## What ChatGPT Can't Do

Now let's look at the limitations and how they are being overcome or could be overcome.

### Libraries and Languages are Constantly Changing

The changing nature of libraries and the cost/time of training models means that tools like ChatGPT at present are out
of date. This can be tiresome and frustrating when GPT is constantly suggesting out of date solutions such as believing
that a library doesn't support the latest Twitter API. I've included a script [Bad Example](bad_example.md) of the
torture of its ignorance.

This problem is likely to be solved by the use of [ChatGPT plugins](https://openai.com/blog/chatgpt-plugins) to pull in
more up-to-date information on libraries. Better still one can hope that new and innovate ways of updating the base
model (of the like of [LoRA](https://github.com/microsoft/LoRA)) allow such services to be more up todate.

Also, take a look at the [Langchain Example](langchain.md) which was generated
using [langchain_example.py](langchain_example.py). In this you can see ChatGPT solving problems as it finds them. While
not very reliable and more a proof of concept, it does also find out issues with outdated code examples.

### Entropy

Each request for the same information can potentially return a different set of code. Not only that in can be in a
different style using different idioms. In coding an idiom is the choice of one or more ways of achieving the same goal.
For example how you create an empty list.

```empty_list = []```

```empty_list = list()```

If you join pieces of code with different idioms together it can look like a patchwork as it doesn't have a single
consistent coding style.

I'd expect to see is that future tooling such as GitHub Copilot X will look at your or your organisations code base to
establish the idiomatic code that you write. Also in the farther future there is the possibility that further
fine-tuning on the model will impose a standardized set of idioms.

### Performance Issues and Crashes

GPT-4 is still very new, and it is not amazingly reliable, sometimes it just gives up halfway through the response, so
you might have to prompt it again with 'continue'. These are all typical teething problems. These will be trivially
fixed.

## How do you write code using GPT-4?

Writing code using GPT-4, or any similar AI-powered code generation tool, involves a combination of clear communication,
patience, and iterative development. Here are some key points to consider when writing code with GPT-4:

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

### Context is Everything

Arguably the largest single improvement is the size of the context in GPT-4. Context is the working memory of the AI,
it's you instructions and it's responses. In GPT-3.5 it was 3K now it's 30K tokens. This is still not large enough to
hold an entire typical application in memory. But it is large enough to write a small prototype or large enough to help
you debug or improve a large script/class etc.

The reason why context is so important is that with GPT-4 you can ask it to write a small application including the
database schema, some backend code, a REST API, a web application and the dockerfiles and docker compose files to launch
them all with. Because it can hold so much in context it knows what the schema is when it writes the REST API. And as
you back and forwards with changes or clarifications it doesn't lose site of the overall application.

Inevitably the code will become larger than the context and you'll need to paste in whole files again and ask for
operations against those files.

### This is TODAY's Solution

Around the corner we'll have [GitHub Copilot X](https://github.com/features/preview/copilot-x) and other deeply
integrated tools which will reduce the need for direct '
chat' style programming. We'll also have GPT plugins which will remove many of the existing limitations, including
knowledge of the latest packages etc.

## The Future

### Deeper Tool Integration

As AI-powered code writing continues to advance, we can expect deeper integration of tools like ChatGPT with IDEs, code
editors, and version control systems. This will enable seamless collaboration between the AI model and developers,
making it easier to access AI-generated code suggestions and apply them to the project at hand.

The [GitHub Copilot X](https://github.com/features/preview/copilot-x) is a prime example.

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

This trial and error approach can be simulated using Langchain and a ReAct loop.

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
using [langchain_example.py](langchain_example.py)

The Thought Loops automate the behaviour of the Human Agent in the current ChatGPT incarnation, but coming back to the
Human Agent to get more information as needed.

### Open Source Alternatives

This changes on a daily basis, but you should look at LLaMA, Alpaca and Dolly to get started.
