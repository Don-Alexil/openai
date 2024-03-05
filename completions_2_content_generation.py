from openai import OpenAI

client = OpenAI()
model = "gpt-3.5-turbo-instruct"

def getSlogan(restaurant_type) : 
    response = client.completions.create(
        model = model, 
        prompt = "Create a slogan for a new " + restaurant_type + "restaurant.",
        max_tokens = 100 
    )
    # Extract the text from response
    print("Slogan for : " + restaurant_type)
    print(response.choices[0].text)

getSlogan("italian")
getSlogan("chinese")    

