from rest_framework import generics,permissions
from .models import University, Program, Section, Course, RecognizedCourse
from .serializers import (
    UniversitySerializer,
    ProgramSerializer,
    SectionSerializer,
    CourseSerializer,
    RecognizedCourseSerializer,UniversitySerializer
)



class UniversityListCreateView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProgramListCreateView(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProgramRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAuthenticated]


class SectionListCreateView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [permissions.IsAuthenticated]


class SectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecognizedCourseListCreateView(generics.ListCreateAPIView):
    queryset = RecognizedCourse.objects.all()
    serializer_class = RecognizedCourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecognizedCourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecognizedCourse.objects.all()
    serializer_class = RecognizedCourseSerializer
    permission_classes = [permissions.IsAuthenticated]



class UniversityDataView(generics.RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    lookup_url_kwarg = 'university_id'
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print("Queryset:", queryset)
        return super().get(request, *args, **kwargs)
    
