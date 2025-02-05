import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main() -> None:
    agent = AssistantAgent("assistant", OpenAIChatCompletionClient(model="gpt-4o"))
    print(await agent.run(task="Say 'Hello World!'"))

asyncio.run(main())
