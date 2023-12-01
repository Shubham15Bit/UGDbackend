from rest_framework import serializers
from .models import University, Program, Section, Course, RecognizedCourse

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Program
        fields = '__all__'

class RecognizedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognizedCourse
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True, read_only=True)
    recognized_courses = RecognizedCourseSerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = '__all__'
