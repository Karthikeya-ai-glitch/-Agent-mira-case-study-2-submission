## Live Demo

**https://verdant-khapse-2373d6.netlify.app/**

![Property Matching UI](property_ui_preview.png)

---

# Property Matching System (Embeddings + FAISS)

An AI-driven property matching system that combines **semantic search on property descriptions** with **numerical preference scoring** (budget, bedrooms, bathrooms).

---

## Files

- **embeddings_generator.py**  
  Generates Gemini embeddings for property descriptions and saves structured data.

- **faiss_setup.py**  
  Builds a FAISS index for fast semantic similarity search.

- **app.py**  
  Flask API that:
  - Embeds user queries
  - Retrieves top semantic matches
  - Applies priority-based hybrid scoring

- **property_data.csv**  
  Cleaned property metadata.

- **property_embeddings.npy**  
  Precomputed text embeddings.

- **faiss.index**  
  FAISS vector index.


