# contracts/services/cuad_loader.py

import json

def load_cuad():
    file_path = r"C:\DJANGO\hirathon\contract_analyzer\data\train_separate_questions.json"

    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)

    return data["data"]