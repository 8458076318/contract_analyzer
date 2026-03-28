from rest_framework.decorators import api_view
from rest_framework.response import Response
from contracts.models import Contract, Clause
from .serializers import ContractSerializer, ClauseSerializer
# from contracts.services.qa_engine import simple_qa
from contracts.services.qa_engine import global_qa

@api_view(['POST'])
def upload_contract(request):
    name = request.data.get('name')

    contract = Contract.objects.create(name=name)

    return Response({"message": "Contract uploaded", "id": contract.id})


@api_view(['GET'])
def get_clauses(request, contract_id):
    clauses = Clause.objects.filter(contract_id=contract_id)
    serializer = ClauseSerializer(clauses, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def ask_question(request, contract_id):

    if request.method == 'GET':
        return Response({
            "message": "Use POST with JSON body: {'question': 'your question'}"
        })

    question = request.data.get('question')

    if not question:
        return Response({"error": "Question is required"}, status=400)

    from contracts.services.qa_engine import simple_qa
    answer = simple_qa(contract_id, question)

    return Response({
        "question": question,
        "answer": answer
    })

@api_view(['GET'])
def list_contracts(request):
    data = []

    for c in Contract.objects.all():
        count = Clause.objects.filter(contract=c).count()
        data.append({
            "id": c.id,
            "name": c.name,
            "clause_count": count
        })

    return Response(data)

@api_view(['POST'])
def ask_global_question(request):
    question = request.data.get('question')

    if not question:
        return Response({"error": "Question is required"}, status=400)

    answer = global_qa(question)

    # return Response(answer)

    return Response({
        "question": question,
        "answer": answer
    })