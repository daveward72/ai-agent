import os
import sys
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types

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
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )
    if (is_verbose):
        print(f"User prompt: {prompt}")
    print(f"Response: {response.text}")
    if (is_verbose):
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    sys.exit(0)

if __name__ == "__main__":
    main()
