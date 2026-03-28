# contracts/services/ingestion.py

from contracts.models import Contract, Clause
from .cuad_loader import load_cuad


def ingest_cuad_contracts(limit=20):
    data = load_cuad()

    contracts_map = {}

    for example in data[:limit]:
        title = example.get("title", "").strip()

        for para in example.get("paragraphs", []):
            context = para.get("context", "")

            for qa in para.get("qas", []):
                category = qa.get("question", "")

                if title not in contracts_map:
                    contract = Contract.objects.create(name=title)
                    contracts_map[title] = contract
                else:
                    contract = contracts_map[title]

                for ans in qa.get("answers", []):
                    text = ans.get("text", "")
                    start = ans.get("answer_start", 0)

                    Clause.objects.create(
                        contract=contract,
                        category=category,
                        text=text,
                        context=context,          
                        start_index=start         
                    )

            # for qa in para.get("qas", []):
            #     category = qa.get("question", "").strip()

            #     answers = qa.get("answers", [])

            #     # Create contract
            #     if title not in contracts_map:
            #         contract = Contract.objects.create(name=title)
            #         contracts_map[title] = contract
            #     else:
            #         contract = contracts_map[title]

            #     # Save clauses
            #     for ans in answers:
            #         text = ans.get("text", "").strip()

            #         if text:  # VERY IMPORTANT
            #             Clause.objects.create(
            #                 contract=contract,
            #                 category=category,
            #                 text=text,
            #                 confidence_score=1.0
            #             )