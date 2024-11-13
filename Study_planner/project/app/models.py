from django.db import models
from django.contrib.auth.models import User

# Study Subject Model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Study Plan Model (Timetable)
class StudyPlan(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject.name} from {self.start_time} to {self.end_time}'

# Analytics for Study Time and Performance
class StudyAnalytics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)
    time_spent = models.DurationField()  # Duration of study in minutes or hours
    performance = models.IntegerField()  # Track performance (0-100 scale)
    feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.study_plan.subject.name}'

# User Profile (optional for custom fields)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    timezone = models.CharField(max_length=100, default='UTC')

    def __str__(self):
        return self.user.username

class Timetable(models.Model):
    subject = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.subject} on {self.day_of_week} from {self.start_time} to {self.end_time}"
