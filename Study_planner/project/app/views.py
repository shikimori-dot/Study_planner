# views.py
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudyAnalytics, StudyPlan, Timetable
from .serializers import StudyAnalyticsSerializer, StudyPlanSerializer

# Study Analytics View (Fetch analytics for the user)
class StudyAnalyticsView(APIView):
    def get(self, request):
        # Fetch all study analytics records
        analytics = StudyAnalytics.objects.all()
        # Serialize the data
        serializer = StudyAnalyticsSerializer(analytics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new study analytics record
        serializer = StudyAnalyticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Study Plan (Timetable) View (Fetch all study plans)
class StudyPlanView(APIView):
    def get(self, request):
        # Fetch all study plans
        study_plans = StudyPlan.objects.all()
        # Serialize the data
        serializer = StudyPlanSerializer(study_plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new study plan (Timetable)
        serializer = StudyPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import TimetableForm

def home(request):
    return render(request, 'home.html')

def timetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable')  # Redirect to the timetable page to show the updated timetable
    else:
        form = TimetableForm()

    timetable_entries = Timetable.objects.all()  # Retrieve all saved timetable entries
    return render(request, 'timetable.html', {'form': form, 'timetable_entries': timetable_entries})

def analytics(request):
    return render(request, 'analytics.html')
