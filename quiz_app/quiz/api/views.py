import secrets
import string

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from quiz.models import Quiz
from quiz.serializers import (
    QuizSerializer,
    ShowFullQuizDetailsSerializer,
    ShowAllCompactQuizzesSerializer,
    PerformQuizSerializer,
)

from quiz.api.permissions import QuizViewPermission, QuizPerformPermission


class QuizCreate(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuizSerializer

    def post(self, request):
        data = request.data
        data["user"] = request.user.id

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllQuizzes(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ShowAllCompactQuizzesSerializer

    def get(self, request):
        quizzes = Quiz.objects.filter(user=request.user)
        serializer = self.serializer_class(quizzes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ShowQuizDetails(APIView):
    permission_classes = [IsAuthenticated, QuizViewPermission]
    serializer_class = ShowFullQuizDetailsSerializer

    def get(self, request, pk):
        try:
            quiz = Quiz.objects.get(pk=pk)
            serializer = self.serializer_class(quiz, many=False)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PublishQuiz(APIView):
    permission_classes = [IsAuthenticated, QuizViewPermission]
    serializer_class = ShowFullQuizDetailsSerializer

    def get(self, request, pk):
        try:
            quiz = Quiz.objects.get(pk=pk)
            serializer = self.serializer_class(quiz, many=False)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        try:
            quiz = Quiz.objects.get(pk=pk)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

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

        serializer = self.serializer_class(quiz, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteQuiz(APIView):
    permission_classes = [IsAuthenticated, QuizViewPermission]

    def post(self, request, pk):
        try:
            quiz = Quiz.objects.get(pk=pk)
            quiz.delete()
            return Response(status=status.HTTP_200_OK)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PerformQuiz(APIView):
    permission_classes = [IsAuthenticated, QuizPerformPermission]
    serializer_class = PerformQuizSerializer
    serializer_class_full = ShowFullQuizDetailsSerializer

    def get(self, request, permalink):
        try:
            quiz = Quiz.objects.get(permalink_id=permalink)
            serializer = self.serializer_class(quiz, many=False)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, permalink):
        try:
            quiz = Quiz.objects.get(permalink_id=permalink)
            serializer = self.serializer_class_full(quiz, many=False)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

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
