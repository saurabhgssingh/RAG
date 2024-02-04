import google.generativeai as genai
from src.config import Config
from chromadb import Documents, EmbeddingFunction, Embeddings
import os
class GeminiEmbeddingFunction(EmbeddingFunction):
  def __call__(self, input: Documents) -> Embeddings:
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
      raise ValueError("Gemini API Key not provided. Please provide GEMINI_API_KEY as environment variable")
    genai.configure(api_key = gemini_api_key)
    model = Config.GEMINI_EMBEDDING
    title = "Custom query"
    return genai.embed_content(model=model,
                                content=input,
                                task_type="retrieval_document",
                                title=title)["embedding"]