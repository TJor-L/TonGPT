# -*- coding: utf-8 -*-
# File : load_md_files.py.py
# Time : 9/8/2024 12:13 PM 
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
# Description: Load mk files from a directory
import os


def load_md_files(directory):
    md_files_content = []
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                md_files_content.append({"filename": filename, "content": content})
    return md_files_content


if __name__ == "__main__":
    md_files = load_md_files("../data")
    print(f"Loaded {len(md_files)} markdown files.")
