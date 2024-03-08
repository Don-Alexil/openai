from openai_utils import get_response

story = """\nIn a distant galaxy, there was a brave space explorer named Alex. Alex had spent years traveling through the cosmos, 
discovering new planets and meeting alien species. One fateful day, while exploring an uncharted asteroid belt, Alex stumbled
 upon a peculiar object that would change the course of their interstellar journey forever...\n"""

# Create a prompt that completes the story
prompt = f"""Complete the story delimited by triple backticks ```${story}```"""

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)