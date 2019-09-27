from django import forms
from .models import Interview

class InterviewForm(forms.ModelForm):
	dateTime=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'date'}))
	class Meta:
		model=Interview
		fields=('title','dateTime','interviewee','interviewer',)