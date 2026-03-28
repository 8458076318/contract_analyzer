# contracts/models.py

from django.db import models

class Contract(models.Model):
    name = models.CharField(max_length=255)
    file_path = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

# class Clause(models.Model):
#     contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
#     category = models.CharField(max_length=100)
#     text = models.TextField()
#     page_number = models.IntegerField(null=True)
#     confidence_score = models.FloatField(default=0.0)

class Embedding(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    chunk_text = models.TextField()
    embedding = models.JSONField()  # or pgvector field

class Clause(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    category = models.TextField()
    text = models.TextField()

    context = models.TextField(null=True, blank=True)   # 🔥 add this
    start_index = models.IntegerField(null=True, blank=True)

    confidence_score = models.FloatField(default=1.0)