"""
Demo code for headline generation using GPT-3.
"""

import os

import openai
from litellm import completion

from yival.logger.token_logger import TokenLogger
from yival.wrappers.string_wrapper import StringWrapper


def headline_generation(tech_startup_business: str) -> str:
    """
    Demo code for headline generation using GPT-3.
    """
    logger = TokenLogger()
    logger.reset()
    # Ensure you have your OpenAI API key set up
    openai.api_key = os.getenv("OPENAI_API_KEY")
    messages = [{
        "role":
        "system",
        "content":
        "You are a helpful assistant that help company grow."
    }, {
        "role":
        "user",
        "content":
        str(
            StringWrapper(
                template="""
                Generate landing one page headline for {tech_startup_business}
                """,
                variables={
                    "tech_startup_business": tech_startup_business,
                },
                name="task"
            )
        )
    }]
    # Use the chat-based completion
    response = completion(
        model="gpt-3.5-turbo", messages=messages
    )
    res = response['choices'][0]['message']['content']
    token_usage = response['usage']['total_tokens']
    logger.log(token_usage)
    return res
