import io
import os

import requests
import tiktoken
from PyPDF2 import PdfReader


def chop(
    text, 
    chunk_size=4000, 
    overlap=200,
):
    encoding = tiktoken.get_encoding("gpt2")

    tokens = encoding.encode(text)
    num_tokens = len(tokens)
    
    chunks = []
    for i in range(0, num_tokens, chunk_size - overlap):
        chunk = tokens[i:i + chunk_size]
        chunks.append(chunk)
    chunks = [encoding.decode(chunk) for chunk in chunks]
    
    return chunks
