from django.db import models

# Create your models here.
class Interview(models.Model):
	title = models.CharField(max_length=1000)
	dateTime = models.DateField()
	# time = models.TimeField(blank=True,null=True)
	interviewee = models.CharField(max_length=1000)
	interviewer = models.CharField(max_length=1000)
