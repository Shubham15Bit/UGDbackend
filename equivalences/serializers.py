from rest_framework import serializers
from .models import University, Program, StudyPlan, Equivalence


class UniversityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = "__all__"


class ProgramSerializer(serializers.ModelSerializer):
    study_Plan = StudyPlanSerializer(many=True, read_only=True, source="study_plans")

    class Meta:
        model = Program
        fields = "__all__"


class UniversitySerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = "__all__"


class EquivalenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equivalence
        fields = "__all__"
