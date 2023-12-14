from rest_framework import generics, permissions
from .models import University, Program, StudyPlan, Equivalence
from .serializers import (
    UniversityListSerializer,
    UniversitySerializer,
    ProgramSerializer,
    StudyPlanSerializer,
    EquivalenceSerializer,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class UniversityListAPIView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer
    permission_classes = [permissions.AllowAny]


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
    program_serializer_class = ProgramSerializer

    def post(self, request, *args, **kwargs):
        destination_university = request.data.get("destination_university", None)
        origin_university = request.data.get("origin_university", None)
        origin_course_name = request.data.get("origin_course_name", None)

        if not (destination_university and origin_university and origin_course_name):
            return Response(
                {"error": "Missing required parameters."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            destination_university_instance = University.objects.get(
                id=destination_university
            )
            print(destination_university_instance)
        except University.DoesNotExist:
            return Response(
                {"error": "Invalid university ID."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        queryset = Equivalence.objects.filter(
            destination_university=destination_university,
            origin_university=origin_university,
            origin_course_name=origin_course_name,
        )
        serializer = self.serializer_class(queryset, many=True)

        approved_destination_name = [
            item["destination_name"] for item in serializer.data
        ]
        programs_queryset = Program.objects.filter(
            university=destination_university_instance
        )
        programs_serializer = self.program_serializer_class(
            programs_queryset, many=True
        )

        mapped_queryset = Equivalence.objects.filter(
            destination_university=destination_university,
            origin_university=origin_university,
        )
        mapped_serializer = self.serializer_class(mapped_queryset, many=True)

        # Extract all destination names from mapped data
        all_destination_names = [
            item["destination_name"] for item in mapped_serializer.data
        ]

        for program_data in programs_serializer.data:
            program_data["study_Plan"] = [
                study_plan
                for study_plan in program_data["study_Plan"]
                if study_plan["name"] not in all_destination_names
            ]
        response_data = {
            "approved_destination_name": approved_destination_name,
            "programs": programs_serializer.data,
        }
        return Response({"destination_name": response_data})
