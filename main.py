import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.Client()

collection = client.create_collection(
    name="faq_collection"
)

questions = [
    "What is Python?",
    "What is React?",
    "Which planet is the largest?",
    "What is a virtual environment?"
     
]

answers = [
    "Python is a programming language.",
    "React is a frontend JavaScript library.",
    "Jupiter is the largest planet in our solar system.",
    "A virtual environment isolates project dependencies."
     
]

embeddings = model.encode(
    questions
).tolist()

collection.add(
    embeddings=embeddings,
    documents=answers,
    ids=["1", "2", "3", "4"]
)

query = input("Ask your question: ")

query_embedding = model.encode(
    query
).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

print("\nAnswer:")
print(results["documents"][0][0])