CLAUSE_EXTRACTION_PROMPT = """
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


QA_PROMPT_TEMPLATE = """
You are a legal assistant.

Answer the question based only on the context below.

Context:
{context}

Question:
{question}

Also provide the exact supporting text.
"""