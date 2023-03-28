## This is out of date.

We're in such a fast moving area that any statement I make will be superseded before you read it!

## What ChatGPT Can and Can't Do anything

It's not going to take away programmers jobs just yet. At best it's a great sidekick to help you brainstorm code and to 
sketch out the basics. However it's trajectory will definitely change the

## How do you write code using GPT-4?

### Write Something, Anything

Start by asking GPT-4 to write something trivial you can understand. Then ask it to add features, to change the coding
style etc. The best way to understand what it can and can't do is trial and error.

### Be Specific

You are talking to a moderately experienced programmer. If you aren't specific then Chat-GPT will make it's own choices,
and you might not like them. So if in doubt be specific. The code is less value than your prompt so don't be afraid to
scrap the code and change your prompt as many times as you need until your happy with the result.

### Be Patient

This is still early days for this paradigm and Chat GPT is a tad unreliable. If it just stops producing output try
saying 'continue'. If you don't think it's done a good job, say so and ask it to do better. You can highlight the
specifics of what you don't like. It's also pretty slow at times.

### And Iterate

When it's produced code, say it keeps calling the same database code over and over, just ask it to extract a common
function. Or if the database is too normalized (everything in one table) ask it to denormalise it.

### Build on Previous Steps

Once you're happy with the code that writes to the database you can ask it to extract the schema for you, ask it to add
FK relationships. Then you can ask it to write a REST API that queries that database.

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

## Know The Limitations

### Entropy

Each request for the same information can potentially return a different set of code. Not only that in can be in a
different style using different idioms. If you join these pieces of code together it can look like a patchwork as it
doesn't have a single consistent coding style.

### Performance Issues and Crashes

GPT-4 is still very new, and it is not amazingly reliable, sometimes it just gives up halfway through the response, so
you
might have to prompt it again with 'continue'. These are all typical teething problems.

### This is TODAY's Solution

Around the corner we'll have Github CoPilot X and other deeply integrated tools which will reduce the need for direct '
chat' style programming. We'll also have GPT plugins which will remove many of the existing limitations, including
knowledge of the latest packages etc.

## The Future

### Deeper Tool Integration

### Larger and Larger Contexts (with the goal being infinite)

### Open Source Alternatives

## The Example
