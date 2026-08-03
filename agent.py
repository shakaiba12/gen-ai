from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# TOOLS

def calculator(expression: str):
    return eval(expression)


def weather(city: str):
    return {
        "city": city,
        "temperature": 36,
        "condition": "Sunny"
    }


TOOLS = {
    "calculator": calculator,
    "weather": weather
}

# ==========================================
# MEMORY
# ==========================================

state = {
    "goal": "",
    "history": []
}

# ==========================================
# SYSTEM PROMPT
# ==========================================

SYSTEM_PROMPT = """
You are an AI Agent.

You have two tools.

1. calculator(expression)
2. weather(city)

Rules:

- Think before answering.
- If a tool is needed, return ONLY valid JSON.
- Do NOT use markdown.
- Do NOT wrap JSON in ```.

Tool format:

{
"type":"tool",
"tool":"calculator",
"args":{
"expression":"5+5"
}
}

Final format:

{
"type":"final",
"answer":"The answer is 10."
}
"""

# ==========================================
# THINK
# ==========================================

def think(goal):

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
                "content": f"""
Goal:

{goal}

History:

{json.dumps(state["history"], indent=2)}
"""
            }
        ]
    )

    content = response.choices[0].message.content

    print("\n========== RAW MODEL RESPONSE ==========")
    print(content)
    print("========================================\n")

    # Remove markdown if model returns ```json
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    try:
        return json.loads(content)

    except json.JSONDecodeError:

        print("Model returned invalid JSON.")
        print(content)

        return {
            "type": "final",
            "answer": content
        }

# AGENT LOOP

def run_agent(goal):

    state["goal"] = goal

    MAX_STEPS = 5

    for step in range(MAX_STEPS):

        print(f"\n========== STEP {step+1} ==========\n")

        decision = think(goal)

        print("Decision:")
        print(json.dumps(decision, indent=4))

        if decision["type"] == "final":

            print("\n========== FINAL ANSWER ==========\n")
            print(decision["answer"])
            return

        tool_name = decision["tool"]

        args = decision["args"]

        if tool_name not in TOOLS:

            print(f"Unknown tool: {tool_name}")
            return

        result = TOOLS[tool_name](**args)

        print("\nTool Result:")
        print(result)

        state["history"].append({
            "tool": tool_name,
            "args": args,
            "result": result
        })

    print("\nStopped after maximum steps.")

# MAIN

if __name__ == "__main__":

    goal = input("Enter Goal: ")

    run_agent(goal)
