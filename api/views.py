from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Question
from api.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
