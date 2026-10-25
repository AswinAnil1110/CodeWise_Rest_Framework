from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionDb,SubmissionDb
from Repository.serializers import QuestionsSerializer,SubmissionSerializer

# Create your views here.
class QuestionList_CreationView(APIView):
    def get(self,request):
        #Retrieve all questions from QuestionDb
        qs = QuestionDb.objects.all()
        serializer_instance = QuestionsSerializer(qs, many=True)
        return Response(data = serializer_instance.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = QuestionsSerializer(data=form_data)
        if serializer_instance.is_valid():
            original_data = serializer_instance.validated_data
            QuestionDb.objects.create(**original_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
            
class QuestionRetriveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs = QuestionDb.objects.get(id=pk)
        serializer_instance = QuestionsSerializer(qs)
        return Response(data=serializer_instance.data)
        
    def put(self,request,pk):
        form_data = request.data
        serializer_instance = QuestionsSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            QuestionDb.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        
    def delete(self,request,pk):
        QuestionDb.objects.filter(id=pk).delete()
        return Response({"message":"Question Deleted Successfully"})

class SubmissionListCreateView(APIView):
    def get(self,request):
        qs = SubmissionDb.objects.all()
        serializer_instance = SubmissionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    
    def post(self,request):
        form_data = request.data
        serializer_instance = SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            SubmissionDb.objects.create(**actual_data)
            return Response({"Message":"Answer Submitted Successfully"})
        else:
            return Response(data=serializer_instance.errors)
    
class SubmissionRetriveUpdateDelete(APIView):
    def get(self,request,pk):
        # qs = SubmissionDb.objects.get(id=pk)
        qs = get_object_or_404(SubmissionDb,id=pk)
        serializer_instance = SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)
    
    def put(self,request,pk):
        form_data = request.data
        serializer_instance = SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            SubmissionDb.objects.filter(id=pk).update(**actual_data)
            return Response({"Message":"Submission Updated Successfully"})
        else:
            return Response(data= serializer_instance.errors)

    def delete(self,request,pk):
        qs = SubmissionDb.objects.filter(id=pk).delete()
        return Response({"Message":"Submission Deleted Successfully"})
        
class EvaluateSubmissionView(APIView):
    def put(self,request,pk):
        form_data = request.data
        SubmissionDb.objects.filter(id=pk).update(**form_data)
        return Response(data={"Message":"Updated...!"})