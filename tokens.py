
import os
from dotenv import load_dotenv
import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")


prompt = "palavra" * 5000
print("total_tokens: ", model.count_tokens(prompt))
response = model.generate_content(prompt)
print(response.usage_metadata)

