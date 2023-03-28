# GPT-4 and the Future of AI-Powered Code Writing

**This is out of date** - we live in a rapidly evolving technological landscape, where advancements in AI and machine
learning render information outdated almost as soon as it's disseminated. This is particularly true in the context of
large language models (LLMs) like GPT-4.

## Before Reading This File

I'm going to assume your head has not been in the sand in the last few months, so you'll know a bit about GPT-4 and
LLMs. But I would urge you to try out GPT-44 on GPTPlus if you can as it is considerably more advanced than the
original GPT-4.

I'd also recommend you read up
on [GPT-4 plugins](https://openai.com/blog/GPT-4-plugins), [GitHub Copilot](https://github.com/features/copilot/)
and [GitHub Copilot X](https://github.com/features/preview/copilot-x) for extra credit read up
on [Langchain](https://github.com/hwchase17/langchain).

## Where We Are From a Developer's Perspective

Just as the Internet existed for two decades before the WWW started; so AI has been around a lot longer than GPT-4,
still we are clearly in a WWW moment. With the release of GPT as a multi-modal AI being analogous to [Marc
Andreessen adding the `<IMG>` tag](http://1997.webhistory.org/www.lists/www-talk.1993q1/0182.html) 30 years ago. We are
now watching the most fundamental pieces of a new technology being put into place. I would even argue that the
addition of [ReAct](https://arxiv.org/abs/2210.03629) in tools like [Langchain](https://github.com/hwchase17/langchain)
as being equivalent to [JavaScript in the browser](https://webdevelopmenthistory.com/1995-the-birth-of-javascript/), and
GPT-4 plugins are probably Java Applets - let's try and forget them.

It is the public's willingness to adopt, the immediate (but small) value proposition and the general wow! factor that
have turned AI from a technological pursuit into a burgeoning technological revolution. The potential is so obviously
tremendous, but the uses so far are still **relatively** trivial.

At the beginning of any IT explosion there is a balance of Utility and Novelty skewed massively to Novelty and in time
switching over to Utility. It took the WWW a decade to go from one to the other, via the rather silly Dotcom boom
antics, cat photos and to now being almost as fundamental as having water and electricity.

So it shouldn't be a surprise that a lot of AI work currently is novelty, "it's cool but what can I do with it?". But
don't be fooled, AI is an enabling technology that will just take time to become integrated in our lives. Unlike
previous 'smart' technologies, it has the potential to actually understand our needs, habits and preferences making
existing technologies easier. Meanwhile, it is rapidly learning to reason, gain theory of mind and many other human like
traits allowing it to take over tasks in the future which were exclusively the realm of humans.

So with even AGI perhaps on the horizon it's easy to worry about the future of coding jobs. But as you'll see, AI still
has a long way to go to just be useful yet. But maybe consider a high level job for the long term!

## What it's Like Coding with GPT-4

Amazing, painful, exhilarating, disturbing and frustrating.

I'll break down the details later but as a quick overview, I'd say GPT-3.5 produces fairly unimpressive code and has
a really short memory. GPT-4 produces good to great code, often better than I'd write especially in areas I'm less
familiar with. It also has a longer memory and so can comprehend several parts of a larger application at once. But it
just
makes too many mistakes, mainly because of the original model data being so old, and changes it's mind too much.

So unless you're writing a simple one-off script you're unlikely to use what it produces as is.

However, even in its current state it's a valuable tool that will help you expand your capabilities. So
let's look at what it can do for you.

## What GPT-4 Can Do

So as I've hopefully established it ain't taking programmers jobs just yet that's for sure. At best, it's a great
sidekick (or as Microsoft like to say Copilot) to help you brainstorm code and to sketch out the basics. However, it's
trajectory has been set and all the evidence points to a rapidly evolving and improving tool.

So let's look at what we can use it for:

* **Code generation**: Generate code snippets, templates, and even more complex code structures in various programming
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

## What GPT-4 Can't Do

Now let's look at the limitations and how they are being overcome or could be overcome.

### Know the latest Libraries, APIs and Languages

The changing nature of libraries and the cost/time of training models means that tools like GPT-4 at present are out
of date. This can be tiresome and frustrating when GPT-4 is constantly suggesting out of date solutions such as
believing that a library doesn't support the latest Twitter API. I've included a script [Bad Example](bad_example.md) of
the torture of its ignorance.

This problem is likely to be solved by the use of [ChatGPT plugins](https://openai.com/blog/chatgpt-plugins) to pull in
more up-to-date information on libraries. Better still one can hope that new and innovate ways of updating the base
model (of the like of [LoRA](https://github.com/microsoft/LoRA)) allow such services to be more up-to-date.

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

As AI-powered code writing continues to advance, we can expect deeper integration of tools like GPT-4 with IDEs, code
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
using [langchain_example.py](langchain_example.py) and uses GPT-3.5

The Thought Loops automate the behaviour of the Human Agent in the current GPT-4 incarnation, but coming back to the
Human Agent to get more information as needed.

### Open Source Alternatives

This changes on a daily basis, but you should look
at [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/), [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html)
and [Dolly](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html) to get
started. 

Then move on to [LangChain](https://github.com/hwchase17/langchain) and [it's ecosystem](https://github.com/kyrolabs/awesome-langchain).
