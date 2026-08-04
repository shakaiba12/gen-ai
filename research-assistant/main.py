from tools import search_document
from llm.think import think
from llm.answer import answer

question = input("Ask: ")

decision = think(question)
print(decision)

if decision["type"] == "tool":
    query = decision["args"]["query"]

    result = search_document(query)
    print(result)

    final_answer = answer(question, result["text"])
    print(final_answer)