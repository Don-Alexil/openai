from openai import OpenAI
# Import the tenacity library
from tenacity import (
  retry, 
  wait_random_exponential, 
  stop_after_attempt
)

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

def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": "system", "content": system_prompt},
      		  {"role": "user", "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-3.5-turbo", messages= messages, temperature=0)
  
  return response.choices[0].message.content

# Add the appropriate parameters to the decorator
@retry(wait=wait_random_exponential(min=5, max=40), stop=stop_after_attempt(4))
def get_response_with_retry(model, message):
    response = client.chat.completions.create(
      model=model,
      messages=[message]
    )
    return response.choices[0].message.content