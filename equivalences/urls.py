from django.urls import path
from .views import (
    UniversityListCreateView, UniversityRetrieveUpdateDestroyView,
    ProgramListCreateView, ProgramRetrieveUpdateDestroyView,
    StudyPlanListCreateView,StudyPlanRetrieveUpdateDestroyView,
    EquivalenceListCreateView,EquivalenceRetrieveUpdateDestroyView,EquivalenceListView,
    UniversityDataView,GetOriginCoursesView,UniversityListAPIView,
    StudentListCreateView,StudentRetrieveUpdateDestroyView,
    StudyPlanCreate,EquivalenceCreate
)

urlpatterns = [
    path('universities/', UniversityListCreateView.as_view(), name='university-list-create'),
    path('universities/<int:pk>/', UniversityRetrieveUpdateDestroyView.as_view(), name='university-retrieve-update-destroy'),
    path('universities-list/', UniversityListAPIView.as_view(), name='university-list'),

    path('programs/', ProgramListCreateView.as_view(), name='program-list-create'),
    path('programs/<int:pk>/', ProgramRetrieveUpdateDestroyView.as_view(), name='program-retrieve-update-destroy'),

    path('study-plan/', StudyPlanListCreateView.as_view(), name='course-list-create'),
    path('study-plan/<int:pk>/', StudyPlanRetrieveUpdateDestroyView.as_view(), name='course-retrieve-update-destroy'),

    path('equivalence-data/', EquivalenceListCreateView.as_view(), name='equivalence-list-create'),
    path('equivalences-data/<int:pk>/', EquivalenceRetrieveUpdateDestroyView.as_view(), name='equivalence-retrieve-update-destroy'),
    path('equivalences/<int:origin_university_id>/', EquivalenceListView.as_view(), name='equivalence-list'),
    
    path('university/<int:university_id>/', UniversityDataView.as_view(), name='university-data'),

    path('get_destination_courses/', GetOriginCoursesView.as_view(), name='get_origin_courses'),

    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),

    path('study-plan-create/', StudyPlanCreate.as_view(), name='course-create'),
    path('equivalences-data-create/', EquivalenceCreate.as_view(), name='equivalence-create')
]
