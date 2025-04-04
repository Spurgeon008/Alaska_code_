from django import forms

class DicomUploadForm(forms.Form):
    dicom_file = forms.FileField(label='Upload DICOM file')
