from src.doc_loader import PDFLoader
from src.utils import split_text
from src.chroma import Chroma
from src.prompts import make_rag_prompt
from src.config import Config
from src.embedding_function import GeminiEmbeddingFunction

N_RESULTS=3
def create_index_pdf(file_path):
    pdf_loader = PDFLoader(file_path=file_path)
    text = pdf_loader.load().content

    # split/chunk the text
    chunked_text = split_text(text)

    #create index
    chroma_instance = Chroma(embedding_function=GeminiEmbeddingFunction())
    collection_name = chroma_instance.add(text)
    return collection_name

def query_text(collection_name,query,n_results):
    chroma_instance = Chroma(collection_name=collection_name,embedding_function=GeminiEmbeddingFunction())
    response = chroma_instance.query_text(query=query,n_results=n_results)
    return response

def query_gemini(prompt,**kwargs):
    import google.generativeai as genai
    model = genai.GenerativeModel(Config.GEMINI_MODEL)
    answer = model.generate_content(prompt)
    return(answer.text)


def generate_response(query):
    response =query_text(Config.DEFAULT_COLLECTION_NAME,query,N_RESULTS)
    rag_prompt = make_rag_prompt(query=query,relevant_passage='\n'.join(response))
    answer = query_gemini(rag_prompt)
    return answer






