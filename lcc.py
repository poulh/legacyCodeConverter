import argparse
import openai
import dotenv
import glob
import os
import re


def get_common_file_extension(language):
    # Define a prompt to ask for the most common file extension for a programming language
    prompt = f"What is the most common file extension for {language} programming language? Only return the letters that make up the file extension."

    # Call the OpenAI API to get the common file extension
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can adjust the engine based on your preference
        prompt=prompt,
        temperature=0,
    )

    # Extract and return the generated extension
    extension = response.choices[0].text.strip()
    return extension.lower()


def convert_legacy_to_modern(legacy_code, target_language):
    # Initialize a conversation with the prompt
    conversation = [
        {"role": "system", "content": "You are a helpful assistant that translates code."},
        {"role": "user", "content": f"Translate the following legacy code encased in triple backticks to {target_language}:\n\n```{legacy_code}```\n\nOnly return the converted code."}
    ]

    # Call the OpenAI API with the Chat Completion model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=conversation,
        temperature=0
    )

    # Extract and return the assistant's reply (generated code)
    assistant_reply = response.choices[0].message["content"]

    # Remove surrounding triple backticks and language identifier
    code_lines = re.search(r'```[^\n]*\n([\s\S]+?)```', assistant_reply, re.MULTILINE).group(1)

    return code_lines


def main():
    parser = argparse.ArgumentParser(description="Legacy Script Converter")
    parser.add_argument("--legacy-path", required=True, help="Path to the legacy code file(s) using a glob pattern")
    parser.add_argument("--output-path", required=True,
                        help="Path to the parent directory for saving the updated scripts")
    parser.add_argument("--convert-to", required=True, help="Target language to convert to")
    args = parser.parse_args()

    # Load environment variables from .env file
    dotenv.load_dotenv()

    # Access the API key from the environment variables
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Find all matching files using glob pattern
    legacy_files = glob.glob(args.legacy_path)

    for legacy_file_path in legacy_files:
        # Read legacy code from the file
        with open(legacy_file_path, 'r') as legacy_file:
            legacy_code = legacy_file.read()

        # Convert legacy code to the target language using OpenAI API
        modern_code = convert_legacy_to_modern(legacy_code, args.convert_to)

        # Determine the appropriate file extension for the target language
        extension = get_common_file_extension(args.convert_to)

        # Determine the output file name
        file_name = os.path.basename(legacy_file_path)
        file_name_without_extension = os.path.splitext(file_name)[0]
        output_file_name = f"{file_name_without_extension}.{extension}"

        # Determine the output file path
        output_file_path = os.path.join(args.output_path, output_file_name)

        # Write the updated script to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(modern_code)

    print("Legacy script conversion complete.")


if __name__ == "__main__":
    main()
