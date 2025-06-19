import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Check if an API key was loaded 
if not api_key:
    print("Error: GEMINI_API_KEY not found in environment variables.")
    sys.exit(1) # Exit the script if no API key present

client = genai.Client(api_key=api_key)

# Check if at least one command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: python main.py")
    sys.exit(1) # Exit if no content is provided

# sys.argv[1] is the first argument after the script name
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=sys.argv[1]
)
print("\n")
print(response.text)
print('Prompt tokens: ' + str(response.usage_metadata.prompt_token_count))
print('Response tokens: ' + str(response.usage_metadata.candidates_token_count))
print("\n")