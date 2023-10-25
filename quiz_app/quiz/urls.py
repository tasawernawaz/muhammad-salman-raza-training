from django.urls import path

from quiz.api.views import (
    QuizCreate,
    AllQuizzes,
    PublishQuiz,
    DeleteQuiz,
    ShowQuizDetails,
    PerformQuiz,
)

urlpatterns = [
    path("", AllQuizzes.as_view(), name="all-quizzes"),
    path("create/", QuizCreate.as_view(), name="create-quiz"),
    path("details/<str:pk>/", ShowQuizDetails.as_view(), name="quiz-details"),
    path("publish/<str:pk>/", PublishQuiz.as_view(), name="publish-quiz"),
    path("delete/<str:pk>/", DeleteQuiz.as_view(), name="delete-quiz"),
    path("perform/<str:permalink>/", PerformQuiz.as_view(), name="perform-quiz"),
]
