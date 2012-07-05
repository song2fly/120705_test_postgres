from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file_uploaded  = forms.FileField()

class FileGetterForm(forms.Form):
    get_file_id = forms.IntegerField



