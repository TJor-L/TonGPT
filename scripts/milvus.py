# -*- coding: utf-8 -*-
# File : milvus.py
# Time : 9/8/2024 5:14 PM 
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
# Description:
from pymilvus import model

from load_md_files import load_md_files

from pymilvus import MilvusClient

client = MilvusClient("milvus_demo.db")

# if client.has_collection(collection_name="demo_collection"):
#     client.drop_collection(collection_name="demo_collection")
# client.create_collection(
#     collection_name="demo_collection",
#     dimension=768,  # The vectors we will use in this demo has 768 dimensions
# )
#
#
# docs = load_md_files("../data/docs")
#
# embedding_fn = model.DefaultEmbeddingFunction()
#
# print(docs)
#
# vectors = embedding_fn.encode_documents(docs)
# print("Dim:", embedding_fn.dim, vectors[0].shape)  # Dim: 768 (768,)
#
# data = [
#     {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"}
#     for i in range(len(vectors))
# ]
#
# print("Data has", len(data), "entities, each with fields: ", data[0].keys())
# print("Vector dim:", len(data[0]["vector"]))


