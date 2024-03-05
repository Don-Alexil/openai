from openai import OpenAI

client = OpenAI()

prompt="""Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

response = client.completions.create(
    model = "gpt-3.5-turbo-instruct", 
    prompt = prompt,
    max_tokens = 100 
)

# Extract the text from response
print("Choice[0] Text: " + response.choices[0].text)
