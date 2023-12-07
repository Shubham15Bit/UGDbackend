from rest_framework import generics, permissions
from .models import University, Program, StudyPlan, Equivalence
from .serializers import (
    UniversitySerializer,
    ProgramSerializer,
    StudyPlanSerializer,
    EquivalenceSerializer,
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


class StudyPlanListCreateView(generics.ListCreateAPIView):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudyPlanRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    permission_classes = [permissions.IsAuthenticated]


class EquivalenceListCreateView(generics.ListCreateAPIView):
    queryset = Equivalence.objects.all()
    serializer_class = EquivalenceSerializer
    permission_classes = [permissions.IsAuthenticated]


class EquivalenceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equivalence.objects.all()
    serializer_class = EquivalenceSerializer
    permission_classes = [permissions.IsAuthenticated]


class UniversityDataView(generics.RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    lookup_url_kwarg = "university_id"
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print("Queryset:", queryset)
        return super().get(request, *args, **kwargs)
