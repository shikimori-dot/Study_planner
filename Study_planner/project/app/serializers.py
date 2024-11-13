# serializers.py
from rest_framework import serializers
from .models import StudyAnalytics, StudyPlan

class StudyAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyAnalytics
        fields = '__all__'  # Include all fields of the model (or specify a list of fields)

class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = '__all__'  # Include all fields of the model (or specify a list of fields)
