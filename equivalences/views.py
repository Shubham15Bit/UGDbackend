from rest_framework import generics, permissions
from .models import University, Program, StudyPlan, Equivalence
from .serializers import (
    UniversitySerializer,
    ProgramSerializer,
    StudyPlanSerializer,
    EquivalenceSerializer,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


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
        return super().get(request, *args, **kwargs)


class GetOriginCoursesView(APIView):
    serializer_class = EquivalenceSerializer

    def post(self, request, *args, **kwargs):
        destination_university = request.data.get("destination_university", None)
        origin_university = request.data.get("origin_university", None)
        destination_course_name = request.data.get("destination_course_name", None)

        # Validate the input parameters
        if not (
            destination_university and origin_university and destination_course_name
        ):
            return Response(
                {"error": "Missing required parameters."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Query the Equivalence model to get the matching origin course names
        queryset = Equivalence.objects.filter(
            destination_university=destination_university,
            origin_university=origin_university,
            destination_course_name=destination_course_name,
        )

        serializer = self.serializer_class(queryset, many=True)
        origin_course_names = [item["origin_course_name"] for item in serializer.data]

        return Response({"origin_course_names": origin_course_names})
