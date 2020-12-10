from django import forms
from students.models import Students


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = [
            "f_name",
            "l_name",
            "email",
        ]
