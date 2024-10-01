# -*- coding: utf-8 -*-
# File : generate_embeddings.py.py
# Time : 9/8/2024 12:14 PM 
# Author : Dijkstra Liu
# Email : l.tingjun@wustl.edu
# 
# 　　　    /＞ —— フ
# 　　　　　| `_　 _ l
# 　 　　　ノ  ミ＿xノ
# 　　 　 /　　　 　|
# 　　　 /　 ヽ　　ﾉ
# 　 　 │　　|　|　\
# 　／￣|　　 |　|　|
#  | (￣ヽ＿_ヽ_)__)
# 　＼_つ
#
# Description: Generate embeddings for markdown files

from openai import OpenAI
import numpy as np
from load_md_files import load_md_files
import os
from dotenv import load_dotenv

load_dotenv()

embedding_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"))


def split_text(text, max_chunk_size=4000):
    chunks = []
    current_chunk = ""
    for sentence in text.split('. '):
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks


def get_embeddings_for_chunks(chunks):
    embeddings = []
    for chunk in chunks:
        print(chunk)
        response = embedding_client.embeddings.create(
            input=chunk,
            model="text-embedding-ada-002"
        )
        embeddings.append(response.data[0].embedding)
    return embeddings


def get_embeddings_with_mapping(texts, max_chunk_size=4000):
    all_embeddings = []
    text_mapping = []

    for text in texts:
        print(text)
        chunks = split_text(text, max_chunk_size)
        embeddings = get_embeddings_for_chunks(chunks)

        all_embeddings.extend(embeddings)
        text_mapping.extend(chunks)

    return all_embeddings, text_mapping


def get_embeddings(texts, max_chunk_size=4000):
    all_embeddings = []

    for text in texts:
        print(text)
        chunks = split_text(text, max_chunk_size)
        embeddings = get_embeddings_for_chunks(chunks)
        all_embeddings.extend(embeddings)
    return all_embeddings


if __name__ == "__main__":
    md_files = load_md_files("../data/docs")
    contents = [file["content"] for file in md_files]

    embeddings, text_mapping = get_embeddings_with_mapping(contents)

    np.save('../embeddings/embeddings.npy', embeddings)
    np.save('../embeddings/text_mapping.npy', text_mapping)
    print(f"Generated embeddings for {len(embeddings)} chunks of markdown files.")
