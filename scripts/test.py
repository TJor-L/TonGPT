# -*- coding: utf-8 -*-
# File : test.py
# Time : 9/8/2024 7:20 PM 
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
# Description: test the openai chat API
import faiss
import numpy as np
from openai import OpenAI

from embeddings_query import search_embedding
from generate_embeddings import embedding_client
from dotenv import load_dotenv
import os

load_dotenv()

chat_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"))


def direct_openai_response(user_input):
    test_client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"))
    completion = test_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    return completion.choices[0].message.content


def RAG_openai_response(user_input):
    completion = chat_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
                You are TonGPT, a specialized assistant focused on understanding and assisting with TON (The Open Network). 
                When a user asks a question, your primary goal is to break down and summarize the key components of the query to identify the most relevant areas for further research in the TON documentation. 
                Focus on highlighting the specific technical concepts, tools, or keywords related to the query, 
                and prepare a summary of what should be searched in the TON documentation to provide an accurate and informative response.
                
                You should answer in following format (one sentence summary of the query):
                My Query Statement is: <Your query statement>
                """

            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    print(completion.choices[0].message.content)

    response_text = completion.choices[0].message.content

    query_statement = response_text.replace("My Query Statement is: ", "")
    print(f"Query statement: {query_statement}")
    index = faiss.read_index("../embeddings/faiss_index.index")
    text_mapping = np.load('../embeddings/text_mapping.npy', allow_pickle=True)

    distances, matching_texts = search_embedding(query_statement, index, embedding_client, text_mapping, k=3)

    relevant_info = "\n\n".join(matching_texts[:3])
    print(f"Most relevant information: {relevant_info}")

    final_completion = chat_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
                You are TonGPT, an expert assistant in TON (The Open Network). 
                Based on the user's question and the relevant information retrieved from the TON documentation, your role is to provide a clear, concise, and accurate answer. 
                Ensure that your response is grounded in the information found in the documents, combining it with your expertise to guide users on topics like smart contracts, staking, DApps, or network architecture. 
                Prioritize delivering well-informed, actionable solutions or explanations.
                """
            },
            {
                "role": "system",
                "content": f"""
                The most relevant information from the TON documentation is:
                {relevant_info}
                """
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    final_response = final_completion.choices[0].message.content
    print("RAG response:")
    return final_response


if __name__ == "__main__":
    user_input = "Introduction of TVM in TON"
    print(RAG_openai_response(user_input))

    print("\nDirect response:")
    print(direct_openai_response(user_input))
