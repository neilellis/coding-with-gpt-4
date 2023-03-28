#!/home/ubuntu/venv/bin/python3.10
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI


llm = ChatOpenAI(model='gpt-3.5-turbo',temperature=0.2)
tools = load_tools(['python_repl', 'requests', 'terminal',  'serpapi', 'wikipedia', 'human',  'pal-math', 'pal-colored-objects'], llm=llm)

agent = initialize_agent(tools, llm, agent="chat-zero-shot-react-description", verbose=True)

agent.run("Ask the human what they want to do")
