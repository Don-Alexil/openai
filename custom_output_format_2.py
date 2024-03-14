from openai_utils import get_response

text = """The sun was setting behind the mountains, casting a warm golden glow across the landscape. """

# Create the instructions
instructions = """You will be provided with a text delimited by triple backticks. 
Extract the language and the number of sentences in the text.
If the text contains more than one sentence, generate a suitable title for it,
otherwise, write 'N/A' for the title"""

# Create the output format
output_format = """Use the following format for the output:         
    - Text: <text we want to title>
    - Language: <text language>
    - N_sentences: <number of sentences>         
    - Title: <the generated title>"""

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)