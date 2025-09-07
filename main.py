import os
import sys
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file
from functions.call_function import call_function

def main():
    if len(sys.argv) < 2:
        print("Supply the prompt as a single command line argument, optionally specifiying a --verbose flag.")
        sys.exit(1)

    prompt = sys.argv[1]
    is_verbose = len(sys.argv) > 2 and sys.argv[2] == '--verbose'

    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    client = genai.Client(api_key=api_key)
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )
    if (is_verbose):
        print(f"User prompt: {prompt}")
    print(f"Response: {response.text}")
    for function_call_part in response.function_calls:
        #print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        func_response = call_function(function_call_part, is_verbose)
        
        if len(func_response.parts) == 0 or not func_response.parts[0].function_response or not func_response.parts[0].function_response.response:
            raise Exception("Response invalid")
        
        if is_verbose:
            print(f"-> {func_response.parts[0].function_response.response}")


    if (is_verbose):
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    sys.exit(0)

if __name__ == "__main__":
    main()
