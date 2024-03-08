from openai import OpenAI

client = OpenAI()

def get_response(prompt):
    # Create a request to the chat completions endpoint
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        # Assign the role and content for the message
        messages = [ {"role": "user", "content": prompt}],
        temperature = 0
    )

    return response.choices[0].message.content
