import os

def search_document(query):

    print("Searching for:", query)

    for filename in os.listdir("documents"):

        print("Checking:", filename)

        path = os.path.join("documents", filename)

        with open(path, "r") as file:
            text = file.read()

        print(text)   

        if query.lower() in text.lower().split():
            return {
                "filename": filename,
                "text": text
            }

    return {
        "filename": None,
        "text": "nothing found"
    }