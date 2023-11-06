from django.urls import include, path
from rest_framework.routers import DefaultRouter

from quiz.api.views import PerformQuizViewset, QuizViewSet

router = DefaultRouter()
router.register(r"perform", PerformQuizViewset, basename="perform-quiz")
router.register(r"", QuizViewSet, basename="quiz")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "perform/<str:permalink>/perform_quiz/",
        PerformQuizViewset.as_view({"post": "perform_quiz"}),
        name="perform-quiz-action",
    ),
]
