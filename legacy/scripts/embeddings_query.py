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
# Description: Search embeddings
import faiss
from generate_embeddings import embedding_client
import numpy as np


def search_embedding(query, index, client, text_mapping, k=5):

    response = client.embeddings.create(
        input=query,
        model="text-embedding-ada-002"
    )
    query_embedding = np.array([response.data[0].embedding])

    distances, indices = index.search(query_embedding, k)

    matching_texts = [text_mapping[i] for i in indices[0]]
    return distances, matching_texts


if __name__ == "__main__":

    index = faiss.read_index("../embeddings/faiss_index.index")
    text_mapping = np.load('../embeddings/text_mapping.npy', allow_pickle=True)

    query = "How to write an if statement in FunC"
    distances, matching_texts = search_embedding(query, index, embedding_client, text_mapping)

    print(f"最相似的文本: {matching_texts}")
    print(f"对应的距离: {distances}")
