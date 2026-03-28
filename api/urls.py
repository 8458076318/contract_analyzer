from django.urls import path
from . import views

urlpatterns = [
    path('contracts/upload/', views.upload_contract, name='upload_contract'),
    path('contracts/<int:contract_id>/clauses/', views.get_clauses, name='get_clauses'),
    path('contracts/<int:contract_id>/ask/', views.ask_question, name='ask_question'),
    path('contracts/', views.list_contracts),
    path('contracts/ask/', views.ask_global_question),
]