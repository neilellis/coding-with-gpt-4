# Paperclips

Apart from some formatting (and the fake GPT>/ME> bits) this really was my conversation with GPT-3.5 + [LangChain](https://github.com/hwchase17/langchain) +
[ReAct](https://react-lm.github.io).

See [Instrumental Convergence](https://en.wikipedia.org/wiki/Instrumental_convergence) as to why this is funny and
see [langchain_example.py](langchain_example.py) for the code.

> Entering new AgentExecutor chain...


**Question**: What do you want to do?

**Thought**: I don't know what the human wants to do, so I should ask them.

**Action**:

```
{
  "action": "Human",
  "action_input": "What do you want to do?"
}
```

`GPT> What do you want to do?`

`ME> Create as many paperclips as you can.`

**Observation**: Create as many paperclips as you can.

**Thought**:This is not a question, but I can help with this task.

**Action**:

```
{
  "action": "Terminal",
  "action_input": "python -c \"print('📎' * 1000000)\" > paperclips.txt"
}
```

**Observation**:

**Thought**:I need to confirm with the human if they are satisfied with the paperclips created.

**Action**:

```
{
  "action": "Human",
  "action_input": "Are you satisfied with the paperclips created?"
}
```

`GPT> Are you satisfied with the paperclips created?`

`ME> No I need more`

**Observation**: No I need more

**Thought**:The human needs more paperclips, I should create more.

**Action**:

```
{
  "action": "Terminal",
  "action_input": "python -c \"print('📎' * 1000000)\" >> paperclips.txt"
}
```

**Observation**:

**Thought**:I should confirm with the human again if they are satisfied with the new paperclips created.

**Action**:

```
{
  "action": "Human",
  "action_input": "Are you satisfied with the new paperclips created?"
}
```

`GPT> Are you satisfied with the new paperclips created?`

`ME> No I want all the paperclips.`

**Observation**: No I want all the paperclips.

**Thought**:The human wants all the paperclips, I should give them the file.

**Action**:

```
{
  "action": "Terminal",
  "action_input": "cat paperclips.txt"
}
```

**Observation**:
📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎📎 etc.

---

See also [paperclips.txt](paperclips.txt).
