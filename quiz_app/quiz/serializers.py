from rest_framework import serializers

from .models import Quiz, Question, Option


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ["option", "is_answer"]


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(many=True)

    def validate(self, data):
        question = data["question"]
        options = data["options"]

        if len(options) == 0:
            raise serializers.ValidationError(
                f"You provided no options for the question: {question}"
            )

        correct_answers = [option["is_answer"] for option in options]
        if correct_answers.count(True) == 0:
            raise serializers.ValidationError(
                f"The question '{question}' must have atleast one correct answer."
            )

        return data

    class Meta:
        model = Question
        fields = ["question", "options"]


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ["title", "questions", "user"]

    def validate(self, data):
        questions = data["questions"]
        if len(questions) == 0:
            raise serializers.ValidationError(
                "There must be atleast one question, you have provided none."
            )

        return data

    def create(self, validated_data):
        questions_data = validated_data.pop("questions")
        quiz = Quiz.objects.create(**validated_data)

        for question_data in questions_data:
            options_data = question_data.pop("options")
            question = Question.objects.create(quiz=quiz, **question_data)

            for option_data in options_data:
                Option.objects.create(question=question, **option_data)
        return quiz


class ShowAllCompactQuizzesSerializer(serializers.ModelSerializer):
    quiz_id = serializers.ReadOnlyField(source="id")

    class Meta:
        model = Quiz
        fields = ["title", "permalink_id", "quiz_id", "published"]


class ShowFullQuizDetailsSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ["title", "questions", "permalink_id", "published"]


class PerformOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ["option"]


class PerformQuestionSerializer(serializers.ModelSerializer):
    options = PerformOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["question", "options"]


class PerformQuizSerializer(serializers.ModelSerializer):
    questions = PerformQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ["title", "questions"]
