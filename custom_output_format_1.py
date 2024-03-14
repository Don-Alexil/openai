from openai_utils import get_response

text = """The sun was setting behind the mountains, casting a warm golden glow across the landscape. 
Birds were chirping happily, and a gentle breeze rustled the leaves of the trees. 
It was a perfect evening for a leisurely stroll in the park"""

# Create the instructions
instructions = "You will be provided with a text delimited by triple backticks. Generate a suitable title for it and detect the text language. "

# Create the output format
output_format = """Use the following format for the output:         
    - Text: <text we want to title>
    - Language: <text language>         
    - Title: <the generated title>"""

# Create the final prompt
prompt = instructions + output_format + f"""```${text}```"""
response = get_response(prompt)
print(response)