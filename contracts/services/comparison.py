# services/comparison.py

def compare_clauses(contract_ids, category):
    results = {}

    for cid in contract_ids:
        clause = Clause.objects.filter(
            contract_id=cid,
            category=category
        ).first()

        results[cid] = clause.text if clause else "Not Found"

    return results