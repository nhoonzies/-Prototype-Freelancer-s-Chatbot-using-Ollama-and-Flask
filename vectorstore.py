from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


    texts = [
        "Freelancers should always review the contract for payment terms before accepting.",
        "Most platforms charge a service fee of around 10-20%.",
        "If a client disputes work, provide clear milestones and written proof of deliverables.",
        "Job briefs should be summarized to highlight deliverables, deadlines, and pay."
    ]

    return FAISS.from_texts(texts, embeddings)
