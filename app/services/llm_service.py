import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-lite")

def generate_answer(query: str, context_chunks: list):
    context = "\n\n".join(context_chunks)

    prompt = f"""
    You are an intelligent assistant. You have to provide a concise and accurate answer to the user's query based on the provided context. The user will provide a pdf document, and you will use the relevant chunks of that document to answer their question.
    If the answer is not present in the context, say "I don't know". Do not make up answers.
    If partial info exists, try to summarize.

    Rules:

    - Use ONLY the provided context
    - Be concise and accurate
    - If unsure, say "I don't know"
    - Do not hallucinate

    Context:
    {context}

    Question:
    {query}
    """

    response = model.generate_content(prompt)

    return response.text