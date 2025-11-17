import argparse
import os
import asyncio

from browser_use import Agent, Browser, ChatBrowserUse, Tools
from dotenv import load_dotenv

load_dotenv()


async def main(resume_path: str):
    chrome_path = os.getenv("CHROME_PATH")
    llm = ChatBrowserUse()
    tools = Tools()
    browser = Browser(
        cross_origin_iframes=True,
        executable_path=chrome_path,
    )

    task = """
    Visit http://localhost:8000/test.html
    Enter first name "John" and last name "Doe"
    Upload the resume file
    """

    available_file_paths = [resume_path]

    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
        tools=tools,
        available_file_paths=available_file_paths,
    )

    history = await agent.run()

    input("Press Enter to continue...")
    return history.final_result()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="test file upload")
    parser.add_argument("--resume", required=True, help="Path to resume PDF file")

    args = parser.parse_args()

    asyncio.run(main(args.resume))
