import numpy as np
from contracts.models import Embedding


def save_embedding(contract, chunk_text, embedding):
    Embedding.objects.create(
        contract=contract,
        chunk_text=chunk_text,
        embedding=embedding
    )


def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def search_similar_chunks(query_embedding, top_k=5):
    results = []

    all_embeddings = Embedding.objects.all()

    for emb in all_embeddings:
        score = cosine_similarity(query_embedding, emb.embedding)
        results.append((score, emb))

    results.sort(reverse=True, key=lambda x: x[0])

    return [item[1] for item in results[:top_k]]