from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(chunks):
    embeddings = model.encode(chunks)
    return embeddings


# TEST CODE
if __name__ == "__main__":

    sample_chunks = [
        "The Gupta Empire was founded by Sri Gupta.",
        "Chandragupta Maurya founded the Maurya Empire.",
        "The Vedic Age was an important period in Indin history."
    ]

    embeddings = create_embeddings(sample_chunks)

    print("Total embeddings:", len(embeddings))
    print("Embedding vector size:", len(embeddings[0]))