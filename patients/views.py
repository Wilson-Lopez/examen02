from rest_framework import viewsets, filters
from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by("-id")
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "specialty"]
    ordering_fields = ["id", "name", "specialty", "created_at"]


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.select_related("doctor").all().order_by("-id")
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "diagnosis", "doctor__name"]
    ordering_fields = ["id", "name", "age", "created_at"]
