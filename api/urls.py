from django.urls import path
from api.views import QuestionViewSet

urlpatterns = [
    path("questions/", QuestionViewSet.as_view(), name="questions"),
]
