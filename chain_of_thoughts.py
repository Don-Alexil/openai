from openai_utils import get_response

# Create the chain-of-thought prompt
prompt = """
Q: Get the age of my friend's father in 10 years, given that now he's double my friend's age, and my friend is 20.
A: Let's think step by step and print output numeroted."""

response = get_response(prompt)
print(response)