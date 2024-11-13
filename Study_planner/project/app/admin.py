from django.contrib import admin
from .models import StudyPlan, Subject, StudyAnalytics, UserProfile

admin.site.register(StudyAnalytics)
admin.site.register(StudyPlan)
admin.site.register(Subject)
admin.site.register(UserProfile)