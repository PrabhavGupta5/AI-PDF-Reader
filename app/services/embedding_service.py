import google.generativeai as genai

genai.configure(api_key="APIKey")

def get_embedding(text: str):
    response = genai.embed_content(
        model="gemini-embedding-2",
        content=text
    )
    return response["embedding"]