from openai_utils import get_response

marketing_message = """Introducing our latest collection of premium leather handbags. 
Each bag is meticulously crafted using the finest leather, ensuring durability and elegance. 
With a variety of designs and colors, our handbags are perfect for any occasion. 
Shop now and experience the epitome of style and quality."""

# Craft a prompt that translates
prompt = f"""Translate the marketing message delimited by triple backticks into French, Spanish and 
Japanese 
```{marketing_message}``` """
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)