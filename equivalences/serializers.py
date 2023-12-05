from rest_framework import serializers
from .models import University, Program, StudyPlan,Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class StudyPlanSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = StudyPlan
        fields = "__all__"


class ProgramSerializer(serializers.ModelSerializer):
    study_Plan = StudyPlanSerializer(many=True, read_only=True, source='study_plan')

    class Meta:
        model = Program
        fields = "__all__"


class UniversitySerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True, read_only=True) 

    class Meta:
        model = University
        fields = "__all__"
