from django.db import models

class DicomMetadata(models.Model):
    file_path = models.CharField(max_length=500)
    patient_name = models.CharField(max_length=100, null=True, blank=True)
    study_date = models.CharField(max_length=20, null=True, blank=True)
    modality = models.CharField(max_length=50, null=True, blank=True)
    study_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.patient_name} - {self.study_date}"



class Album(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(DicomMetadata, related_name='albums')

    def __str__(self):
        return self.name


class DicomImage(models.Model):
    patient_name = models.CharField(max_length=255)
    study_date = models.DateField()
    file_path = models.TextField()

    def __str__(self):
        return f"{self.patient_name} - {self.study_date}"
