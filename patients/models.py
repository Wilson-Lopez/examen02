from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=120)
    specialty = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.specialty})"


class Patient(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    diagnosis = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name="patients")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name