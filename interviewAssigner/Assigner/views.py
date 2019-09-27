from django.shortcuts import render
from django.http import HttpResponse
from .forms import InterviewForm
from .models import Interview

# Create your views here.
def index(request):
	form = InterviewForm()
	return render(request,'Assigner/index.html',{'form' : form })
def new(request):
	if request.POST:
		form = InterviewForm(request.POST)
		if form.is_valid():
			print("Form is valid")
			# Have to check the interview is valid on the given date
			# *************Checking validity**********
			# Get all the interviews
			interviews = Interview.objects.all()
			# Get the current Interview time 
			instance = form.save(commit=False)
			currentInterviewDate = instance.dateTime
			currentInterviewee = instance.interviewee
			print(currentInterviewDate)
			# Check the current Interview Time is within the 2 hour span of the interviews listed
			validInterview = True
			for interview in interviews:
				prevDate = interview.dateTime
				prevInterviewee = interview.interviewee
				if currentInterviewDate == prevDate and prevInterviewee ==currentInterviewee:
					validInterview = False
					break
			if validInterview:
				print("Success")
				form.save()
				return HttpResponse("Created Successfully")
			else:
				return HttpResponse("The Interviewee is not free on this date")
			# If not valid
			# Return Date is not valid try again
			# else
			# Save the form
	else:
		return HttpResponse("Not valid")
# List by Date 
# from collections import defaultdict
def list(request):
	interviews = Interview.objects.all()
	DateMap = []
	# for i in interviews:
	# 	print(i)
	return render(request,'Assigner/list.html',{ 'interviews' : interviews, 'DateMap' : DateMap })
