from llm.client import client
from prompts import SYSTEM_PROMPT
import json
def answer(question, document):
    """
    This function takes a question and a document as input, and returns an answer based on the provided information.
    It uses the Groq API to generate a response from the LLaMA model.
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "oYou are a research assistant that helps users with their research tasks. You can provide summaries, explanations, and insights on various topics. You can also assist with data analysis, literature reviews, and generating research questions. Your responses should be clear, concise, and well-structured."

            },
            {
                "role":"user",
                "content": f"""


        Question: {question}
        Document: {document}
        ans the user question"""
            }
        ]

    )
    return response.choices[0].message.content