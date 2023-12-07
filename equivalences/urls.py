from django.urls import path
from .views import (
    UniversityListCreateView, UniversityRetrieveUpdateDestroyView,
    ProgramListCreateView, ProgramRetrieveUpdateDestroyView,
    StudyPlanListCreateView,StudyPlanRetrieveUpdateDestroyView,
    EquivalenceListCreateView,EquivalenceRetrieveUpdateDestroyView,
    UniversityDataView,
)

urlpatterns = [
    path('universities/', UniversityListCreateView.as_view(), name='university-list-create'),
    path('universities/<int:pk>/', UniversityRetrieveUpdateDestroyView.as_view(), name='university-retrieve-update-destroy'),

    path('programs/', ProgramListCreateView.as_view(), name='program-list-create'),
    path('programs/<int:pk>/', ProgramRetrieveUpdateDestroyView.as_view(), name='program-retrieve-update-destroy'),

    path('study-plan/', StudyPlanListCreateView.as_view(), name='course-list-create'),
    path('study-plan/<int:pk>/', StudyPlanRetrieveUpdateDestroyView.as_view(), name='course-retrieve-update-destroy'),

    path('equivalence-data/', EquivalenceListCreateView.as_view(), name='equivalence-list-create'),
    path('equivalences-data/<int:pk>/', EquivalenceRetrieveUpdateDestroyView.as_view(), name='equivalence-retrieve-update-destroy'),
    
    path('university/<int:university_id>/', UniversityDataView.as_view(), name='university-data'),
]
