import os
import google.generativeai as genai

# Make sure your GOOGLE_API_KEY environment variable is set
# e.g., os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"

# Configure the API with your key
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

print("Available Gemini models:")
for m in genai.list_models():
    # Only list models that support generateContent (for chat/text)
    if 'generateContent' in m.supported_generation_methods:
        print(f"  - {m.name} (description: {m.description})")