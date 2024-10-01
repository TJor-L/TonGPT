# -*- coding: utf-8 -*-
# File : query.py
# Time : 9/24/2024 7:21 PM 
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
from llama_index.core import StorageContext, load_index_from_storage, Settings, get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool
import os


storage_context = StorageContext.from_defaults(persist_dir="./data/index")

index = load_index_from_storage(storage_context)

# configure retriever
retriever = VectorIndexRetriever(
    index=index,
    similarity_top_k=5,
)

response_synthesizer = get_response_synthesizer()

query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
    node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.7)],
)

Settings.llm = OpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7)

query_tool = QueryEngineTool.from_defaults(
    query_engine,
    name="Ton_FunC_Query_Tool",
    description="A RAG engine with knowledge of Ton and FunC documentation",
)

agent = ReActAgent.from_tools(
    [query_tool], verbose=True
)

response = agent.chat("If statement in FunC")