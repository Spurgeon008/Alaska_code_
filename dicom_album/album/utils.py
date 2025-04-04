import pydicom
from album.models import DicomMetadata
from .models import Album, DicomMetadata

import os
import pydicom
from .models import DicomImage
from datetime import datetime

def import_dicom_file(file_path):
    try:
        ds = pydicom.dcmread(file_path)

        patient_name = str(ds.get("PatientName", "Unknown"))
        study_date = str(ds.get("StudyDate", "Unknown"))

        dicom_image = DicomImage.objects.create(
            patient_name=patient_name,
            study_date=study_date,
            file_path=file_path
        )

        return {
            "patient_name": patient_name,
            "study_date": study_date,
            "file_path": file_path
        }

    except Exception as e:
        print("Error reading DICOM:", e)
        return None

def create_album(name, dicom_ids):
    album = Album.objects.create(name=name)
    images = DicomMetadata.objects.filter(id__in=dicom_ids)
    album.images.set(images)
    album.save()
    return album
