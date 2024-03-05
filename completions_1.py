from openai import OpenAI


client = OpenAI()

response = client.completions.create(
    model = "gpt-3.5-turbo-instruct", 
    prompt = "What is the OpenAI API?"
)

print(response)

# Extract the model from response
print("Model: " + response.model)

# Extract the total_tokens from response
print("Total Tokens: " + str(response.usage.total_tokens))

# Extract the text from response
print("Choice[0] Text: " + response.choices[0].text)
