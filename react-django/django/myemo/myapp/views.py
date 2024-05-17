from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Person
from .serializers import PersonSerializer

class PersonList(ListAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer  

class MalePersonList(APIView):
    def get(self, request):
        male_persons = Person.objects.filter(gender='Male')
        serializer = PersonSerializer(male_persons, many=True)
        return Response(serializer.data)

class FemalePersonList(APIView):
    def get(self, request):
        female_persons = Person.objects.filter(gender='Female')
        serializer = PersonSerializer(female_persons, many=True)
        return Response(serializer.data)

class BirthCountMonthList(APIView):
    def get(self, request, month):
        persons_in_month = Person.objects.filter(date_of_birth__month=month)
        serializer = PersonSerializer(persons_in_month, many=True)
        return Response(serializer.data)

