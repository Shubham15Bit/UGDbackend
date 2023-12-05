from django.urls import path
from .views import (
    UniversityListCreateView, UniversityRetrieveUpdateDestroyView,
    ProgramListCreateView, ProgramRetrieveUpdateDestroyView,
    StudyPlanListCreateView,StudyPlanRetrieveUpdateDestroyView,UniversityDataView,
    SubjectList,SubjectDetail,
)

urlpatterns = [
    path('universities/', UniversityListCreateView.as_view(), name='university-list-create'),
    path('universities/<int:pk>/', UniversityRetrieveUpdateDestroyView.as_view(), name='university-retrieve-update-destroy'),

    path('programs/', ProgramListCreateView.as_view(), name='program-list-create'),
    path('programs/<int:pk>/', ProgramRetrieveUpdateDestroyView.as_view(), name='program-retrieve-update-destroy'),

    path('study-plan/', StudyPlanListCreateView.as_view(), name='course-list-create'),
    path('study-plan/<int:pk>/', StudyPlanRetrieveUpdateDestroyView.as_view(), name='course-retrieve-update-destroy'),

    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    
    path('university/<int:university_id>/', UniversityDataView.as_view(), name='university-data'),
]
