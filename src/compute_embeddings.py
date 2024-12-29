import faiss
import numpy as np
from uuid import uuid4
from langchain_core.documents import Document
import os
import getpass
from langchain_mistralai import MistralAIEmbeddings
from langchain_mistralai.embeddings import DummyTokenizer
import json

# Set the API key
if not os.getenv("MISTRALAI_API_KEY"):
    os.environ["MISTRALAI_API_KEY"] = getpass.getpass("Bt9sJgE1XLJzpfIvUWs02Hz3ccGxef3t")

# Initialize MistralAI Embeddings with DummyTokenizer
tokenizer = DummyTokenizer()
embeddings = MistralAIEmbeddings(
    model="mistral-embed",
    tokenizer=tokenizer
)

# Define a function to compute embeddings
def compute_embeddings(texts):
    return embeddings.embed_documents(texts)

# Read text files and create documents
def read_files_and_create_documents(file_paths):
    documents = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            document = Document(
                page_content=content,
                metadata={"source": os.path.basename(file_path)},
            )
            documents.append(document)
    return documents

def save_embeddings_and_metadata(file_paths, index_path, metadata_path):
    documents = read_files_and_create_documents(file_paths)
    texts = [doc.page_content for doc in documents]
    embeddings_list = compute_embeddings(texts)

    # Create a FAISS index
    dimension = embeddings_list.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings_list).astype('float32'))

    # Save the FAISS index
    faiss.write_index(index, index_path)

    # Save document IDs and metadata
    uuids = [str(uuid4()) for _ in range(len(documents))]
    document_metadata = {uuid: {"content": doc.page_content, "metadata": doc.metadata} for uuid, doc in zip(uuids, documents)}

    with open(metadata_path, "w") as f:
        json.dump(document_metadata, f)

    print(f"Embeddings and metadata saved to {index_path} and {metadata_path}.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Compute embeddings for stories.')
    parser.add_argument('--input-dir', type=str, required=True, help='Directory containing the story files.')
    parser.add_argument('--index-path', type=str, required=True, help='Path to save the FAISS index.')
    parser.add_argument('--metadata-path', type=str, required=True, help='Path to save the document metadata.')
    args = parser.parse_args()

    file_paths = [
        os.path.join(args.input_dir, "a-mother.txt"),
        os.path.join(args.input_dir, "sorrow.txt"),
        os.path.join(args.input_dir, "the-lantern-keepers.txt"),
        os.path.join(args.input_dir, "the-poor-relations-story.txt"),
        os.path.join(args.input_dir, "the-schoolmistress.txt")
    ]
    save_embeddings_and_metadata(file_paths, args.index_path, args.metadata_path)
