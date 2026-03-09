import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')


def retrieve_chunks(query, index, chunks, top_k=3):

    # Convert query to embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding)

    # Search FAISS index
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i in indices[0]:
        results.append(chunks[i])

    return results
if __name__ == "__main__":

    chunks = [
        "The Gupta Empire was founded by Sri Gupta.",
        "Chandragupta Maurya founded the Maurya Empire.",
        "The Vedic Age was an early period of Indian history."
    ]

    embeddings = model.encode(chunks)

    import faiss

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    query = "who was the third ruler of gupta empire?"

    results = retrieve_chunks(query, index, chunks)

    print("\nRelevant Chunks:\n")

    for r in results:
        print(r)