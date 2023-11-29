#this will take a input file and generate a outline of it
#def generate_outline():
#this will generate paper idea examples
#def generate_paper_ideas():
#this will use input paper's outline to generate a similar paper
#def outline_based_generate():
#this will use input paper's outline to generate a similar paper but will also try to copy the style of input paper
#def outline_based_generate_style():
#this will generate a paper on a random subject while copying the style of input paper
#def generate_style_random_paper():



import os
from openai import OpenAI


api_key = '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'
model = "gpt-3.5-turbo-1106"
base_filename = "gpt/gpt3"


# Set your API key here
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=api_key,
)

def read_text_from_file(file_path):
    """ Reads and returns the content of a text file. """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "The file was not found."
    except Exception as e:
        return f"An error occurred: {e}"



def save_string_to_file(text, base_filename): 
    """
    Saves a given string to a text file. If the file already exists, increment the file name by 1.
    """
    # Start with the base filename
    filename = base_filename
    file_extension = '.txt'
    counter = 1

    # Check if the file exists and increment the counter until the file does not exist
    while os.path.exists(filename + file_extension):
        filename = f"{base_filename}({counter})"
        counter += 1

    # When a unique filename is found, write the text to the file
    with open(filename + file_extension, 'w') as file:
        file.write(text)

    print(f"File saved as: {filename}{file_extension}")
    return filename + file_extension



def generate_outline(text):
    """
    Generates an outline based on the input text.
    """
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Create an outline for the following text:\n\n{text}",
        }
    ],
    model=model,
)
    
    chat_completion = chat_completion.choices[0].message.content
    return chat_completion

def generate_paper_ideas():
    """
    Generates paper idea examples based on a given subject.
    """
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Generate a list of paper topics about random subjects.",
        }
    ],
    model=model,
    )
    chat_completion = chat_completion.choices[0].message.content
    return chat_completion

def outline_based_generate(text):
    """
    Generates a paper based on an input outline.
    """
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Write a paper based on the following outline:\n\n{generate_outline(text)}",
        }
    ],
    model=model,
    )
    chat_completion = chat_completion.choices[0].message.content
    save_string_to_file(chat_completion, base_filename=base_filename)
    return chat_completion

def outline_based_generate_style(text):
    """
    Generates a similar paper based on an input paper's outline and tries to copy the style of the input paper.
    """
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Using the style of the following text:\n\n{text}\n\nWrite a paper based on this outline:\n\n{generate_outline(text)}",
        }
    ],
    model=model,
    )
    chat_completion = chat_completion.choices[0].message.content
    save_string_to_file(chat_completion, base_filename=base_filename)
    return chat_completion


def generate_style_random_paper(text):
    """
    Generates a paper on a random subject while trying to copy the style of the input paper.
    """
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Using the style of the following text:\n\n{text}\n\nWrite a paper on one of these random subjects {generate_paper_ideas()}.",
        }
    ],
    model=model,
    )
    chat_completion = chat_completion.choices[0].message.content
    save_string_to_file(chat_completion, base_filename=base_filename)
    return chat_completion

