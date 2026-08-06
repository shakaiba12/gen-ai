from tools import search_document
from llm.think import think
from llm.answer import answer
from agents.orchestrator import orchestrator
from agents.search_agent import search_agent
from agents.writer_agent import writer_agent


question = input("Ask: ")

decision = orchestrator(question)
print(decision)

# if decision["type"] == "tool":
#     query = decision["args"]["query"]

#     result = search_documents(query)
#     print(result)

#     final_answer = answer(question, result["text"])
#     print(final_answer)

if decision["next_agent"] == "search_agent":
    result = search_agent(question)
    print(result)
    
    final_answer = writer_agent(question, result["text"])
    print(final_answer)