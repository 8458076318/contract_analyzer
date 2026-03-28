import re
from contracts.models import Clause

def clean_text(text):
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()


def extract_category_from_text(text):
    match = re.search(r'"(.*?)"', text)
    if match:
        return match.group(1).lower().strip()
    return None


def global_qa(question):
    question = clean_text(question).lower()

    clauses = Clause.objects.all()

    for clause in clauses:
        category = extract_category_from_text(clause.category)

        if not category:
            continue

        if category in question:
            return {
                "answer": clean_text(clause.text),
                "source_context": clean_text((clause.context or "")[:300]),
                "contract": clause.contract.name
            }

    return {"answer": "No relevant clause found"}

# def global_qa(question):
#     question_clean = clean(question)

#     clauses = Clause.objects.all()

#     for clause in clauses:
#         extracted_category = extract_category_from_text(clause.category)

#         if not extracted_category:
#             continue

#         category_clean = clean(extracted_category)

#         # flexible matching
#         if category_clean in question_clean:
#             return clause.text

#     return "No relevant clause found"