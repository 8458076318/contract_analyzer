# services/extraction.py

CLAUSE_PROMPT = """
Extract the following clause types from the contract:

- Governing Law
- Termination for Convenience
- Cap on Liability
- Non-Compete
- IP Ownership

Return JSON:
{
  "clauses": [
    {
      "category": "",
      "text": "",
      "confidence": 0-1
    }
  ]
}
"""

def extract_clauses(chunk):
    response = llm_call(CLAUSE_PROMPT + chunk)
    return parse_json(response)