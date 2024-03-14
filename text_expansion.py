from openai_utils import get_response

product_description = """
Product: "Smart Home Security Camera"
    - High-tech security camera with night vision and motion detection.
    - Easy setup and remote monitoring.
    - Two-way audio communication for real-time interaction.
    - Mobile app integration for convenient control and alerts.
    - Weather-resistant design for both indoor and outdoor use.
    - Smart AI algorithms for advanced person and object detection.
    - Cloud storage and local backup options for recorded footage.
    - Infrared LEDs for clear imaging even in complete darkness.
    - Customizable motion zones to focus on specific areas.
    - Compatibility with voice assistants for hands-free control.
"""

# Craft a prompt to expand the product's description
prompt = f"""Expand the product description delimited by triple backticks, using one paragraph, 
capturing  unique features, benefits, and potential applications.
```{product_description}```
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)