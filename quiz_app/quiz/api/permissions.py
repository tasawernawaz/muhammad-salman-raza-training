from rest_framework import permissions

from quiz.models import Quiz


class QuizViewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            pk = view.kwargs.get("pk")
            quiz = Quiz.objects.get(pk=pk)
        except Quiz.DoesNotExist:
            return False
        return quiz.user == request.user


class QuizPerformPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            permalink = view.kwargs.get("permalink")
            quiz = Quiz.objects.get(permalink_id=permalink)
        except Quiz.DoesNotExist:
            return False

        if not quiz.published or quiz.user == request.user:
            return False

        return True
