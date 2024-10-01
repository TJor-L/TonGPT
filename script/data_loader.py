# -*- coding: utf-8 -*-
# File : data_loader.py
# Time : 9/24/2024 7:12 PM 
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
# Description: This is the data loader for the project

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

documents = SimpleDirectoryReader("./data/docs").load_data()

vector_index = VectorStoreIndex.from_documents(documents)

vector_index.storage_context.persist(persist_dir="./data/index")