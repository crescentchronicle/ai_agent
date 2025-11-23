import sys
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    arg_length = sys.argv
    print("Hello from ai-agent!")

    
    if len(arg_length) == 1 or arg_length == None:
        print("Prompt empty")
        sys.exit(1)
    
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=f"{sys.argv[1:]}"
    )
    print(response.text)

    usage = response.usage_metadata

    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")


if __name__ == "__main__":
    main()
