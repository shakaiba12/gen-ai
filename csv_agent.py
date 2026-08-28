from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import pandas as pd
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

df = pd.read_csv("employees.csv")

state= {
    "current_file": "employees.csv",
    "dataframe": df ,
    "history": [],
    "last_question" :"",
    "last_answer": "",
    }

def highest_salary():
    df = state["dataframe"]
    max_salary = df["Salary"].max()
    highest_paid = df[df["Salary"] == max_salary]
    return highest_paid

def avg_salary():
    df = state["dataframe"]
    avg_sal = df["Salary"].mean()
    return {
        "average_salary": float(df["Salary"].mean())
    }

def employee_count():
    df = state["dataframe"]
    total_count = len(df)
    return {
        "employee_count": len(df)
    }

def filter_department(department):
    df = state["dataframe"]
    dep = df[df["Department"] == department]
    return dep

TOOLS={
    "highest_salary": highest_salary,
    "avg_salary": avg_salary,
    "employee_count": employee_count,
    "filter_department": filter_department 
}


SYSTEM_PROMPT = """
    you are a csv assistant 
    available tools are :
    highest_salary,
    avg_salary,
    employee_count,
    filter_department(department)

    respond should be in jason format only with type and tool and args if needed
    user can asked who has the highest salary, what is the average salary, how many employees are there, or filter by department
    { 
      "type":"tool",
      "tool": highest_salary,
      "args":{}
    }
    """ 

def think(question):
    response = client.chat.completions.create(
        temperature=0,
        model="llama-3.3-70b-versatile",
        messages =[
            {
                "role": "system",
                "content": SYSTEM_PROMPT

            },
            {
                "role" : "user",
                "content": question          
            }
        ]
    )
    return json.loads(
        response.choices[0].message.content
    )

question = input("Ask a question: ")
decision = think(question)
result = TOOLS[decision["tool"]]()
print(result)


