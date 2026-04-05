# backend/agent/loop.py
import os
import json
from typing import AsyncGenerator
from google import genai
from google.genai import types
from dotenv import load_dotenv
from .tools import TOOLS, execute_tool
from .prompts import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "gemini-3.1-flash-lite-preview"


async def run_agent_stream(query: str) -> AsyncGenerator[dict, None]:
    # Build initial message history
    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=query)]
        )
    ]

    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        tools=[TOOLS],
    )

    iteration = 0
    max_iterations = 10

    while iteration < max_iterations:
        iteration += 1

        response = client.models.generate_content(
            model=MODEL,
            contents=messages,
            config=config,
        )

        # Add model response to history
        messages.append(response.candidates[0].content)

        # Collect any function calls from response parts
        fn_calls = [
            part.function_call
            for part in response.candidates[0].content.parts
            if part.function_call is not None
        ]

        # No function calls — model is done
        if not fn_calls:
            for part in response.candidates[0].content.parts:
                if part.text:
                    yield {"type": "final", "content": part.text}
            return

        # Execute each function call and collect responses
        fn_response_parts = []
        for fn_call in fn_calls:
            name = fn_call.name
            inputs = dict(fn_call.args)

            yield {"type": "tool_call", "tool": name, "input": inputs}

            result = execute_tool(name, inputs)

            yield {"type": "tool_result", "tool": name, "result": result}

            fn_response_parts.append(
                types.Part(
                    function_response=types.FunctionResponse(
                        name=name,
                        response={"result": result}
                    )
                )
            )

        # Feed all tool results back as a single user turn
        messages.append(
            types.Content(role="user", parts=fn_response_parts)
        )

    yield {"type": "error", "content": "Agent exceeded maximum iterations"}