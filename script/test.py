# -*- coding: utf-8 -*-
# File : test.py
# Time : 9/24/2024 8:11 PM 
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
#
import os

from llama_index.core import SimpleDirectoryReader

from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple, reasoning, multi_context
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.settings import Settings

from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)

from ragas.integrations.llama_index import evaluate


# Load documents
documents = SimpleDirectoryReader("./data/docs").load_data()

# generator with openai models
generator_llm = OpenAI(model="gpt-3.5-turbo-16k", api_key=os.getenv("OPENAI_API_KEY"))
critic_llm = OpenAI(model="gpt-4", api_key=os.getenv("OPENAI_API_KEY"))
embeddings = OpenAIEmbedding()

generator = TestsetGenerator.from_llama_index(
    generator_llm=generator_llm,
    critic_llm=critic_llm,
    embeddings=embeddings,
)
testes = generator.generate_with_llamaindex_docs(
    documents,
    test_size=5,
    distributions={simple: 0.5, reasoning: 0.25, multi_context: 0.25},
)

df = testes.to_pandas()
print(df.head())

vector_index = VectorStoreIndex.from_documents(documents)

query_engine = vector_index.as_query_engine()

df = testes.to_pandas()
print(df["question"][0])

response_vector = query_engine.query(df["question"][0])

print(response_vector)

metrics = [
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
]

evaluator_llm = OpenAI(model="gpt-4-turbo", api_key=os.getenv("OPENAI_API_KEY"))

ds = testes.to_dataset()

ds_dict = ds.to_dict()
print(ds_dict["question"])
print(ds_dict["ground_truth"])

result = evaluate(
    query_engine=query_engine,
    metrics=metrics,
    dataset=ds_dict,
    llm=evaluator_llm,
    embeddings=OpenAIEmbedding(),
)

print(result)

result.to_pandas()