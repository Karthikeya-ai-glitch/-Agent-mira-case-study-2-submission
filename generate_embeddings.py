import pandas as pd
import numpy as np
from google import genai
from google.genai import types

API_KEY = "AIzaSyCxdmJaqvlJ4VqCCQ4fkFdoGzUO2inTC1g"
client = genai.Client(api_key=API_KEY)

# Load property data from Excel
df = pd.read_excel(
    "Case Study 2 Data.xlsx",
    sheet_name="Property Data"
)

# Keep only required columns
df = df[
    ["Property ID", "Price", "Bedrooms", "Bathrooms", "Qualitative Description"]
].dropna().reset_index(drop=True)

# Save CSV (used by Flask)
df.to_csv("property_data.csv", index=False)

# Gemini embedding function
def get_embedding(text):
    result = client.models.embed_content(
        model="text-embedding-004",
        contents=text,
        config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT")
    )
    return np.array(result.embeddings[0].values, dtype=np.float16)

# Generate embeddings
embeddings = np.array(
    [get_embedding(t) for t in df["Qualitative Description"]],
    dtype=np.float16
)

# Save embeddings
np.save("property_embeddings.npy", embeddings)

print("✅ CSV and embeddings generated")
