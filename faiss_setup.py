import numpy as np
import faiss

# Load embeddings
embeddings = np.load("property_embeddings.npy").astype("float32")

# Normalize for cosine similarity
faiss.normalize_L2(embeddings)

# Build FAISS index (flat, CPU-safe)
index = faiss.IndexFlatIP(768)
index.add(embeddings)

# Save index
faiss.write_index(index, "faiss.index")

print("✅ FAISS index built")
