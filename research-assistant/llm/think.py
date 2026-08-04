from prompts import SYSTEM_PROMPT
from llm.client import client
import json
def think(question):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }

        ]
    )
    content = response.choices[0].message.content
    print(content)

    return json.loads(content)

