from django.urls import path
from .views import (
    UniversityListCreateView, UniversityRetrieveUpdateDestroyView,
    ProgramListCreateView, ProgramRetrieveUpdateDestroyView,
    SectionListCreateView, SectionRetrieveUpdateDestroyView,
    CourseListCreateView, CourseRetrieveUpdateDestroyView,
    RecognizedCourseListCreateView, RecognizedCourseRetrieveUpdateDestroyView,UniversityDataView
)

urlpatterns = [
    path('universities/', UniversityListCreateView.as_view(), name='university-list-create'),
    path('universities/<int:pk>/', UniversityRetrieveUpdateDestroyView.as_view(), name='university-retrieve-update-destroy'),

    path('programs/', ProgramListCreateView.as_view(), name='program-list-create'),
    path('programs/<int:pk>/', ProgramRetrieveUpdateDestroyView.as_view(), name='program-retrieve-update-destroy'),

    path('sections/', SectionListCreateView.as_view(), name='section-list-create'),
    path('sections/<int:pk>/', SectionRetrieveUpdateDestroyView.as_view(), name='section-retrieve-update-destroy'),

    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='course-retrieve-update-destroy'),

    path('recognized-courses/', RecognizedCourseListCreateView.as_view(), name='recognized-course-list-create'),
    path('recognized-courses/<int:pk>/', RecognizedCourseRetrieveUpdateDestroyView.as_view(), name='recognized-course-retrieve-update-destroy'),
    path('university/<int:university_id>/', UniversityDataView.as_view(), name='university-data'),
]
