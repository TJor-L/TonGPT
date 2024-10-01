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
# Description: Save embeddings to disk
import faiss
import numpy as np

if __name__ == "__main__":
    embeddings = np.load('../embeddings/embeddings.npy')

    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    faiss.write_index(index, "../embeddings/faiss_index.index")

    print(f"FAISS index stored with {index.ntotal} embeddings.")
