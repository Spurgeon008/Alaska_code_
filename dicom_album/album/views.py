
import os
from django.conf import settings
from django.shortcuts import render,redirect
from .utils import import_dicom_file
from .models import DicomImage


def upload_file(request):
    context = {}

    if request.method == 'POST':
        dicom_file = request.FILES.get('dicom_file')
        if dicom_file:
            media_root = 'media'
            os.makedirs(media_root, exist_ok=True)

            file_path = os.path.join(media_root, dicom_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in dicom_file.chunks():
                    destination.write(chunk)

            dicom_info = import_dicom_file(file_path)
            if dicom_info:
                
                request.session['patient_name'] = dicom_info['patient_name']
                request.session['study_date'] = dicom_info['study_date']
                request.session['file_path'] = dicom_info['file_path']
                return redirect('dicom_list')
            else:
                context['error'] = 'Failed to read and save DICOM file.'
        else:
            context['error'] = 'No file uploaded.'

    return render(request, 'album/upload.html', context)



def dicom_list(request):
    context = {
        'patient_name': request.session.get('patient_name'),
        'study_date': request.session.get('study_date'),
        'file_path': request.session.get('file_path'),
    }
    return render(request, 'album/list.html', context)