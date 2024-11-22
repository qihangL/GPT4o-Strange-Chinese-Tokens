import os

import regex as re
import requests


def remove_punctuation(x):
    return x.str.replace(r"^[\W_]+|[\W_]+$", "", regex=True).str.strip()


def keep_chinese(x):
    han_pattern = re.compile(r"\p{sc=Han}")
    kana_pattern = re.compile(r"[\u3040-\u30FF\uFF65-\uFF9F]")
    return x[x.apply(lambda s: bool(han_pattern.search(s))) & ~x.apply(lambda s: bool(kana_pattern.search(s)))]


def min_length(x):
    return x[x.str.len() >= 2]


def download_stopwords(url, filepath):
    response = requests.get(url)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(response.text)


def load_stopwords(filepath):
    stopwords = set()
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            stopwords.add(line.split()[0])
    return stopwords


def remove_stopwords(x):
    stopwords = set()
    stopwords_files = {
        "dict.txt.big": "https://raw.githubusercontent.com/fxsjy/jieba/refs/heads/master/extra_dict/dict.txt.big",
        "idf.txt.big": "https://raw.githubusercontent.com/fxsjy/jieba/refs/heads/master/extra_dict/idf.txt.big",
    }
    for filename, url in stopwords_files.items():
        filepath = os.path.join("./downloaded", filename)
        if not os.path.exists(filepath):
            download_stopwords(url, filepath)
        stopwords.update(load_stopwords(filepath))
    return x[~x.isin(stopwords)]


def deduplicate(x):
    return x.drop_duplicates()
