import secrets
import string

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from quiz.api.permissions import QuizPerformPermission, QuizViewPermission
from quiz.models import Quiz
from quiz.serializers import (PerformQuizSerializer, QuizSerializer,
                              ShowAllCompactQuizzesSerializer,
                              ShowFullQuizDetailsSerializer)


class QuizViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    def get_permissions(self, *args, **kwargs):
        if self.action == "list" or self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, QuizViewPermission]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(
        operation_summary="Gets all Quizzes",
        operation_description="This endpoint allows the authenticated user to get all Quizzes made by them",
        responses={status.HTTP_200_OK: ShowAllCompactQuizzesSerializer},
    )
    @extend_schema(
        summary="Gets all Quizzes",
        description="This endpoint allows the authenticated user to get all Quizzes made by them",
        responses={status.HTTP_200_OK: ShowAllCompactQuizzesSerializer},
    )
    def list(self, request):
        quizzes = self.queryset.filter(user=request.user)
        serializer = ShowAllCompactQuizzesSerializer(quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Gets a specific Quiz",
        operation_description="This endpoint allows the authenticated user to get a specific Quiz made by them",
        responses={status.HTTP_200_OK: ShowFullQuizDetailsSerializer},
    )
    @extend_schema(
        summary="Gets a specific Quiz",
        description="This endpoint allows the authenticated user to get a specific Quiz made by them",
        responses={status.HTTP_200_OK: ShowFullQuizDetailsSerializer},
    )
    def retrieve(self, request, pk=None):
        quiz = get_object_or_404(self.queryset, pk=pk)
        serializer = ShowFullQuizDetailsSerializer(quiz, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Create a Quiz",
        description="This endpoint allows the authenticated user to create a quiz",
        responses={
            status.HTTP_200_OK: ShowFullQuizDetailsSerializer,
            status.HTTP_400_BAD_REQUEST: "Bad Request",
        },
    )
    @swagger_auto_schema(
        operation_summary="Create a Quiz",
        operation_description="This endpoint allows the authenticated user to create a quiz",
        responses={
            status.HTTP_200_OK: ShowFullQuizDetailsSerializer,
            status.HTTP_400_BAD_REQUEST: "Bad Request",
        },
    )
    def create(self, request):
        data = request.data
        data["user"] = request.user.id

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Publish a Quiz",
        operation_description="This endpoint allows the authenticated user to publish a quiz made by them. This attaches a permalink_id and sets its published status to true",
        responses={status.HTTP_200_OK: ShowFullQuizDetailsSerializer},
    )
    @extend_schema(
        summary="Publish a Quiz",
        description="This endpoint allows the authenticated user to publish a quiz made by them.. This attaches a permalink_id and sets its published status to true",
        request=None,
        responses={status.HTTP_200_OK: ShowFullQuizDetailsSerializer},
    )
    def update(self, request, pk=None):
        quiz = get_object_or_404(self.queryset, pk=pk)

        if not quiz.permalink_id:
            while True:
                characters = string.ascii_letters + string.digits
                quiz.permalink_id = "".join(
                    secrets.choice(characters) for _ in range(6)
                )

                if not Quiz.objects.filter(permalink_id=quiz.permalink_id).exists():
                    break

        quiz.published = True
        quiz.save()

        serializer = ShowFullQuizDetailsSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Delete a Quiz",
        operation_description="This endpoint allows the user who created the quiz, delete it.",
        responses={status.HTTP_200_OK: ""},
    )
    @extend_schema(
        summary="Delete a Quiz",
        description="This endpoint allows the user who created the quiz, delete it.",
        responses={status.HTTP_200_OK: ""},
    )
    def destroy(self, request, pk=None):
        quiz = get_object_or_404(self.queryset, pk=pk)
        quiz.delete()
        return Response(status=status.HTTP_200_OK)


class PerformQuizViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, QuizPerformPermission]
    serializer_class = PerformQuizSerializer
    serializer_class_full = ShowFullQuizDetailsSerializer
    lookup_field = "permalink"
    queryset = Quiz.objects.all()

    @swagger_auto_schema(
        tags=["Perform"],
        operation_summary="View a Quiz",
        operation_description="This endpoint allows you to view the quiz's details",
        responses={status.HTTP_200_OK: PerformQuizSerializer},
    )
    @extend_schema(
        tags=["Perform"],
        summary="View a Quiz",
        description="This endpoint allows you to view the quiz's details",
    )
    def retrieve(self, request, permalink=None):
        quiz = get_object_or_404(self.queryset, permalink_id=permalink)
        serializer = self.serializer_class(quiz, many=False)
        return Response(serializer.data)

    @extend_schema(
        tags=["Perform"],
        summary="Perform Quiz",
        description="This endpoint allows you to perform a quiz.",
        request=PerformQuizSerializer,
        responses={
            status.HTTP_200_OK: "You scored {No. of correctly answered questions}/{Total questions} questions correctly"
        },
    )
    @action(detail=True, methods=["post"])
    @swagger_auto_schema(
        tags=["Perform"],
        operation_summary="Perform a Quiz",
        operation_description="This endpoint allows you to perform a quiz.",
        request_body=PerformQuizSerializer,
        responses={
            status.HTTP_200_OK: "You scored {No. of correctly answered questions}/{Total questions} questions correctly"
        },
    )
    def perform_quiz(self, request, permalink=None):
        quiz = get_object_or_404(self.queryset, permalink_id=permalink)
        serializer = self.serializer_class_full(quiz, many=False)

        errors = {}

        # This checks whether the number of "questions" provided is the same as the
        # number of questions the quiz has
        user_answers = request.data
        if len(user_answers) != quiz.questions.count():
            errors[
                "answers"
            ] = f"Invalid data. Got answers for {len(user_answers)} questions, expected {quiz.questions.count()}"

        # This checks whether the question indexes are within range
        # Ex: Answers for a quiz with 4 questions should have 0,1,2,3. Not 0,1,3,4 or 1,2,3,4 etc
        expected_question_ids = {str(i) for i in range(quiz.questions.count())}
        provided_question_ids = set(user_answers.keys())
        if expected_question_ids != provided_question_ids:
            errors[
                "formatting"
            ] = f"Provided question IDs do not match the expected IDs: {list(expected_question_ids)}, you provided: {list(provided_question_ids)}"

        if len(errors.keys()):
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        # This checks how many questions the user got right
        valid_data = serializer.data
        questions = valid_data["questions"]
        correct_questions = 0

        for index, question_data in enumerate(questions):
            answers_by_user = set(user_answers[str(index)])
            actual_answers = {
                str(index)
                for index, option in enumerate(question_data["options"])
                if option["is_answer"]
            }

            if answers_by_user == actual_answers:
                correct_questions += 1

        return Response(
            {
                f"You answered {correct_questions}/{quiz.questions.count()} questions correctly"
            },
            status=status.HTTP_200_OK,
        )
