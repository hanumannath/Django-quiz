from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class ExamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        exam_id = self.kwargs['exam_id']
        return Section.objects.filter(exam_id=exam_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        section_id = self.kwargs.get('section_id')
        return Topic.objects.filter(section_id=section_id)

    def list(self, request, section_id=None):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, section_id=None):
        queryset = self.get_queryset()
        topic = queryset.filter(pk=pk).first()
        if topic:
            serializer = self.serializer_class(topic)
            return Response(serializer.data)
        return Response({'message': 'Topic not found'}, status=404)


class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        topic_id = self.kwargs.get('topic_id')
        return Quiz.objects.filter(topic_id=topic_id)

    def list(self, request, topic_id=None):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, topic_id=None):
        queryset = self.get_queryset()
        quiz = queryset.filter(pk=pk).first()
        if quiz:
            serializer = self.serializer_class(quiz)
            return Response(serializer.data)
        return Response({'message': 'Quiz not found'}, status=404)

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        quiz_id = self.kwargs.get('quiz_id')
        return Question.objects.filter(quiz_id=quiz_id)

    def list(self, request,quiz_id=None):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, quiz_id=None):
        queryset = self.get_queryset()
        question = queryset.filter(pk=pk).first()
        if question:
            serializer = self.serializer_class(question)
            return Response(serializer.data)
        return Response({'message': 'Questions not found'}, status=404)



