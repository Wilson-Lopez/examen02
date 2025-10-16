from rest_framework import serializers
from .models import Doctor, Patient

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id", "name", "specialty", "created_at"]


class PatientSerializer(serializers.ModelSerializer):
    #relacio con id
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(), source="doctor", write_only=True
    )

    # este es el campo del doctor
    doctor_name = serializers.CharField(source="doctor.name", read_only=True)
    doctor_specialty = serializers.CharField(source="doctor.specialty", read_only=True)

    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "age",
            "diagnosis",
            "doctor_id",
            "doctor_name",
            "doctor_specialty",
            "created_at",
        ]

    
    def validate_age(self, value):
        if value > 120:
            raise serializers.ValidationError("La edad no debe ser mas de 120 años.")
        return value
