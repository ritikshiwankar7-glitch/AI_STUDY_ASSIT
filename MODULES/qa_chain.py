from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

def generate_answer(question, retrieved_chunks):

    context = "\n".join(retrieved_chunks)

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}

Give a clear answer.
"""

    response = llm.invoke(prompt)

    return response


if __name__ == "__main__":

    chunks = [
        "The Gupta Empire was founded by Sri Gupta.",
        "Chandragupta I expanded the empire.",
        "The Gupta period is known as the Golden Age of India."
    ]

    question = "Who founded the Gupta Empire?"

    answer = generate_answer(question, chunks)

    print("\nAnswer:\n")
    print(answer)