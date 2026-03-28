# contracts/services/cuad_manual_loader.py

import json
import os

def load_cuad_manual(limit=20):
    file_path = r"C:\DJANGO\hirathon\contract_analyzer\data\train_separate_questions.json"

    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)

    results = []

    for example in data["data"][:limit]:
        title = example.get("title", "")

        for para in example["paragraphs"]:
            context = para["context"]

            for qa in para["qas"]:
                category = qa["question"]
                answers = [a["text"] for a in qa["answers"]]

                results.append({
                    "title": title,
                    "context": context,
                    "category": category,
                    "answers": answers
                })

    return results