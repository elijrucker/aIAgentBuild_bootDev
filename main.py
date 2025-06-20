import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages)


def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print("Response:")
    print(response.txt)


if __name__ == "__main__":
    main()

# load_dotenv()
# api_key = os.environ.get("GEMINI_API_KEY")

# # Check if an API key was loaded 
# if not api_key:
#     print("Error: GEMINI_API_KEY not found in environment variables.")
#     sys.exit(1) # Exit the script if no API key present

# client = genai.Client(api_key=api_key)

# # Check if at least one command-line argument is provided
# if len(sys.argv) < 2:
#     print("Usage: python main.py")
#     sys.exit(1) # Exit if no content is provided

# # Check against 'verbose' flag in agent prompt
# if '--verbose' in sys.argv:
#     print("User prompt: {user_prompt}")

# # Create a list in order to support agent-user conversation
# messages = [
#     types.Content(role="user", parts=[types.Part(text=user_prompt)]),
# ]

# # sys.argv[1] is the first argument after the script name
# response = client.models.generate_content(
#     model='gemini-2.0-flash-001',
#     contents=messages,
# )
# print("\n")
# print(response.text)
# print('Prompt tokens: ' + str(response.usage_metadata.prompt_token_count))
# print('Response tokens: ' + str(response.usage_metadata.candidates_token_count))
# print("\n")