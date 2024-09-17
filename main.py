from environment_variables import API_KEY
import google.generativeai as genai
import os

genai.configure(api_key=API_KEY)


def AI(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt,stream=True)
    response.resolve()
    if response:
        return response.text