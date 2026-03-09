import os
from pypdf import PdfReader

CHUNK_SIZE = 500


def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content

    return text


def chunk_text(text, chunk_size):
    chunks = []
    
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
        
    return chunks


folder_path = "DATA"

all_chunks = []

for file in os.listdir(folder_path):

    if file.endswith(".pdf"):

        file_path = os.path.join(folder_path, file)

        print(f"\nProcessing file: {file}\n")

        text = load_pdf(file_path)

        chunks = chunk_text(text, CHUNK_SIZE)

        for i, chunk in enumerate(chunks):

            chunk_data = {
                "heading": file,
                "chunk_number": i + 1,
                "content": chunk
            }

            all_chunks.append(chunk_data)

            print(f"Heading: {file}")
            print(f"Chunk Number: {i+1}")
            print(chunk[:200])
            print("-"*50)