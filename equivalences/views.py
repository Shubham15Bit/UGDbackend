from rest_framework import generics, permissions
from .models import University, Program, StudyPlan, Equivalence, Student
from .serializers import (
    UniversityListSerializer,
    UniversitySerializer,
    ProgramSerializer,
    StudyPlanSerializer,
    EquivalenceSerializer,
    StudentSerializer,
)

from .data import dataUGD,ugdCourse2,dataUniversities
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from io import BytesIO
from django.core.files.base import ContentFile
import json
from equivalences.mail import send_query_creation_email
from datetime import datetime





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





class StudyPlanCreate(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        # Assuming 'program' with id=1 already exists in the database
        program_id = 1
        program_instance = Program.objects.get(pk=program_id)

        for study_plan_data in dataUGD:
            study_plan_data['program'] = program_instance.id  # Set program to the desired program ID
            serializer = StudyPlanSerializer(data=study_plan_data)
            
            if serializer.is_valid():
                serializer.save()
            else:
                # If any data is not valid, return the error response
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Study Plans created successfully"}, status=status.HTTP_201_CREATED)



class StudyPlanRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    permission_classes = [permissions.IsAuthenticated]






# class EquivalenceCreate(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         destination_university_id = 1  # Set the destination university ID
#         destination_university = University.objects.get(pk=destination_university_id)

#         for equivalence_data in dataUniversities:
#             # Check if any required field is empty
#             if (
#                 not equivalence_data["destination_course_code"]
#                 or not equivalence_data["destination_name"]
#                 or equivalence_data["destination_program"] is None
#                 or not equivalence_data["origin_course_name"]
#                 or equivalence_data["origin_university"] is None
#             ):
#                 # Skip to the next entry if any field is empty
#                 continue

#             # Additional check for origin_course_name
#             if not equivalence_data["origin_course_name"]:
#                 # Skip to the next entry if origin_course_name is empty
#                 continue

#             equivalence_data["destination_university"] = destination_university.id
#             serializer = EquivalenceSerializer(data=equivalence_data)

#             if serializer.is_valid():
#                 serializer.save()
#             else:
#                 # If any data is not valid, log the error and continue with the next entry
#                 print(f"Error creating equivalence: {serializer.errors}")

#         return Response({"message": "Equivalences created successfully"}, status=status.HTTP_201_CREATED)



# class EquivalenceCreate(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         destination_university_id = 1  # Set the destination university ID
#         destination_university = University.objects.get(pk=destination_university_id)

#         for equivalence_data in dataUniversities:
#             # Check if any required field is empty
#             if (
#                 not equivalence_data["destination_course_code"]
#                 or not equivalence_data["destination_name"]
#                 or equivalence_data["destination_program"] is None
#                 or not equivalence_data["origin_course_name"]
#                 or equivalence_data["origin_university"] is None
#             ):
#                 # Skip to the next entry if any field is empty
#                 continue

#             # Additional check for origin_course_name
#             if not equivalence_data["origin_course_name"]:
#                 # Skip to the next entry if origin_course_name is empty
#                 continue

#             # Check if destination_course_code is in the specified list
#             if equivalence_data["destination_course_code"] in ["LCNI2", "LCNI9", "LCNI6", "LCNI40", "LCNI25", "LCNI36", "LCNI34", "LCNI11", "LCNI10", "LCNI23", "LCNI42"]:
#                 # Set destination_program to 2
#                 equivalence_data["destination_program"] = 2

#             equivalence_data["destination_university"] = destination_university.id
#             serializer = EquivalenceSerializer(data=equivalence_data)

#             if serializer.is_valid():
#                 serializer.save()
#             else:
#                 # If any data is not valid, log the error and continue with the next entry
#                 print(f"Error creating equivalence: {serializer.errors}")

#         return Response({"message": "Equivalences created successfully"}, status=status.HTTP_201_CREATED)


class EquivalenceCreate(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        destination_university_id = 1  # Set the destination university ID
        destination_university = University.objects.get(pk=destination_university_id)

        for equivalence_data in dataUniversities:
            # Check if destination_course_code is equal to "Código"
            if equivalence_data.get("destination_course_code") == "Código":
                # Skip to the next entry if destination_course_code is "Código"
                continue

            # Check if any required field is empty
            if (
                not equivalence_data["destination_course_code"]
                or not equivalence_data["destination_name"]
                or equivalence_data["destination_program"] is None
                or not equivalence_data["origin_course_name"]
                or equivalence_data["origin_university"] is None
            ):
                # Skip to the next entry if any field is empty
                continue

            # Additional check for origin_course_name
            if not equivalence_data["origin_course_name"]:
                # Skip to the next entry if origin_course_name is empty
                continue

            # Check if destination_course_code is in the specified list
            if equivalence_data["destination_course_code"] in ["LCNI2", "LCNI9", "LCNI6", "LCNI40", "LCNI25", "LCNI36", "LCNI34", "LCNI11", "LCNI10", "LCNI23", "LCNI42"]:
                # Set destination_program to 2
                equivalence_data["destination_program"] = 2

            equivalence_data["destination_university"] = destination_university.id
            serializer = EquivalenceSerializer(data=equivalence_data)

            if serializer.is_valid():
                serializer.save()
            else:
                # If any data is not valid, log the error and continue with the next entry
                print(f"Error creating equivalence: {serializer.errors}")

        return Response({"message": "Equivalences created successfully"}, status=status.HTTP_201_CREATED)



class EquivalenceListCreateView(generics.ListCreateAPIView):
    queryset = Equivalence.objects.all()
    serializer_class = EquivalenceSerializer
    permission_classes = [permissions.IsAuthenticated]


class EquivalenceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equivalence.objects.all()
    serializer_class = EquivalenceSerializer
    permission_classes = [permissions.IsAuthenticated]


class EquivalenceListView(generics.ListAPIView):
    serializer_class = EquivalenceSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        origin_university_id = self.kwargs["origin_university_id"]
        return Equivalence.objects.filter(origin_university=origin_university_id)


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
    student_serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def draw_program_details(self, p, program, start_y):
        p.drawString(80, start_y, f"Program Name: {program['name']}")
        start_y -= 20  # Adjust the vertical space as needed

        # Add study plan details
        for study_plan in program["study_Plan"]:
            course_info = (
                f"Course Code: {study_plan['code']} - Course Name: {study_plan['name']}"
            )
            p.setFontSize(10)  # Adjust the font size if necessary
            p.drawString(
                100, start_y, course_info
            )  # Adjust the starting position to shift left
            start_y -= 20  # Adjust the vertical space as needed

        return start_y

    def generate_pdf_response(self, response_data, student_instance):
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="output.pdf"'
        # Create an in-memory buffer for the PDF content
        buffer = BytesIO()

        # Create PDF document with frames
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []

        # Header
        university_name = "UGD"
        header_style = ParagraphStyle(
            "HeaderStyle",
            parent=getSampleStyleSheet()["Heading1"],
            spaceAfter=12,
            alignment=1,
        )  # Alignment 1 is for center
        header_text = f"<font size=16>{university_name}</font>"
        story.append(Paragraph(header_text, header_style))

        # Student information (in bold)
        student_info = (
            f"<b>Student:</b> {response_data['student']['name']} {response_data['student']['last_name']}<br/>"
            f"<b>Phone:</b> {response_data['student']['phone']}<br/>"
            f"<b>Email:</b> {response_data['student']['email']}"
        )
        student_style = ParagraphStyle(
            "StudentStyle",
            parent=getSampleStyleSheet()["BodyText"],
            spaceAfter=12,
            fontName="Helvetica-Bold",
        )
        story.append(Paragraph(student_info, student_style))

        # Approved Destinations
        destination_info = "<b>Approved Destinations:</b><br/>" + "<br/>".join(
            f"- {dest}" for dest in response_data["approved_destination_name"]
        )
        destination_style = ParagraphStyle(
            "DestinationStyle", parent=getSampleStyleSheet()["BodyText"], spaceAfter=12
        )
        story.append(Paragraph(destination_info, destination_style))

        # Programs
        program_style = ParagraphStyle(
            "ProgramStyle", parent=getSampleStyleSheet()["BodyText"], spaceAfter=12
        )
        study_plan_style = ParagraphStyle(
            "StudyPlanStyle",
            parent=getSampleStyleSheet()["BodyText"],
            spaceAfter=6,
            leftIndent=20,
        )
        story.append(Paragraph("<b>Programs:</b>", program_style))
        for program in response_data["programs"]:
            story.append(
                Paragraph(f"<b>Program Name:</b> {program['name']}", program_style)
            )
            for study_plan in program["study_Plan"]:
                course_info = f"Course Code: {study_plan['code']} - Course Name: {study_plan['name']}"
                story.append(Paragraph(course_info, study_plan_style))

        # Footer
        currentDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        signature = f"Digitally Signed By UGD {currentDateTime}"
        query_id = f"Query ID: {response_data['student']['id']}"
        footer_style = ParagraphStyle(
            "FooterStyle",
            parent=getSampleStyleSheet()["BodyText"],
            spaceBefore=12,
            fontName="Helvetica-Bold",
        )
        footer_text = f"<b>{signature}</b><br/>{query_id}"
        story.append(Paragraph(footer_text, footer_style))

        # Build PDF document with automatic pagination
        doc.build(
            story, onFirstPage=self.add_page_number, onLaterPages=self.add_page_number
        )
        buffer.seek(0)

        student_instance.report.save(
            f"{student_instance.id}_output.pdf", ContentFile(buffer.read())
        )

        # Get the URL of the saved PDF file
        pdf_url = student_instance.report.url
        print(pdf_url)

        buffer.close
        return pdf_url

    def add_page_number(self, canvas, doc):
        """
        Add the page number at the bottom of each page.
        """
        page_num = canvas.getPageNumber()
        text = f"Page {page_num}"
        canvas.drawRightString(letter[0] - 10, 10, text)

    # def post(self, request, *args, **kwargs):
    #     destination_university = request.data.get("destination_university", None)
    #     origin_university = request.data.get("origin_university", None)
    #     origin_course_names = request.data.get("origin_course_names", None)
    #     student_id = request.data.get("student_id", None)

    #     if not (destination_university and origin_university):
    #         return Response(
    #             {"error": "Missing required parameters."},
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )

    #     try:
    #         destination_university_instance = University.objects.get(
    #             id=destination_university
    #         )
    #     except University.DoesNotExist:
    #         return Response(
    #             {"error": "Invalid university ID."},
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )

    #     queryset = Equivalence.objects.filter(
    #         destination_university=destination_university,
    #         origin_university=origin_university,
    #     )

    #     # Conditionally filter by origin_course_names if not "All"
    #     if origin_course_names and origin_course_names != "All":
    #         queryset = queryset.filter(origin_course_name__in=origin_course_names)

    #     serializer = self.serializer_class(queryset, many=True)

    #     # Retrieve student data based on student_id
    #     try:
    #         student_instance = Student.objects.get(id=student_id)
    #         student_serializer = self.student_serializer_class(student_instance)
    #     except Student.DoesNotExist:
    #         return Response(
    #             {"error": "Invalid student ID."},
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )

    #     mapped_queryset = Equivalence.objects.filter(
    #         destination_university=destination_university,
    #         origin_university=origin_university,
    #     )
    #     mapped_serializer = self.serializer_class(mapped_queryset, many=True)
    #     #  Extract all destination names from mapped data
    #     all_mapped_data = mapped_serializer.data
    #     all_destination_names = [item["destination_name"] for item in all_mapped_data]
    #     # Filter approved_destination_name based on mapping with origin_course_names
    #     approved_destination_name = [
    #         item["destination_name"]
    #         for item in serializer.data
    #         if item["destination_name"] in all_destination_names
    #     ]
        
        
    #     print(approved_destination_name)
        
    
    #     programs_queryset = Program.objects.filter(
    #         university=destination_university_instance
    #     )
    #     programs_serializer = self.program_serializer_class(
    #         programs_queryset, many=True
    #     )

    #     for program_data in programs_serializer.data:
    #         program_data["study_Plan"] = [
    #             study_plan
    #             for study_plan in program_data["study_Plan"]
    #             if study_plan["name"] not in approved_destination_name
    #         ]

    #     response_data = {
    #         "student": student_serializer.data,
    #         "approved_destination_name": approved_destination_name,
    #         "programs": programs_serializer.data,
    #     }
    #     pdf_url = self.generate_pdf_response(response_data, student_instance)
    #     response_data.update(
    #         {
    #             "pdf_url": "http://127.0.0.1:8000" + pdf_url,
    #         }
    #     )
    #     return Response({"destination_name": response_data})
    
class GetOriginCoursesView(APIView):
    serializer_class = EquivalenceSerializer
    program_serializer_class = ProgramSerializer
    student_serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]
    def draw_program_details(self, p, program, start_y):
        p.drawString(80, start_y, f"Program Name: {program['name']}")
        start_y -= 20  # Adjust the vertical space as needed
        # Add study plan details
        for study_plan in program["study_Plan"]:
            course_info = (
                f"Course Code: {study_plan['code']} - Course Name: {study_plan['name']}"
            )
            p.setFontSize(10)  # Adjust the font size if necessary
            p.drawString(
                100, start_y, course_info
            )  # Adjust the starting position to shift left
            start_y -= 20  # Adjust the vertical space as needed
        return start_y
    def generate_pdf_response(self, response_data, student_instance):
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="output.pdf"'
        # Create an in-memory buffer for the PDF content
        buffer = BytesIO()
        # Create PDF document with frames
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []
        # Header
        university_name = "UGD"
        header_style = ParagraphStyle(
            "HeaderStyle",
            parent=getSampleStyleSheet()["Heading1"],
            spaceAfter=12,
            alignment=1,
        )  # Alignment 1 is for center
        header_text = f"<font size=16>{university_name}</font>"
        story.append(Paragraph(header_text, header_style))
        # Student information (in bold)
        student_info = (
            f"<b>Student:</b> {response_data['student']['name']} {response_data['student']['last_name']}<br/>"
            f"<b>Phone:</b> {response_data['student']['phone']}<br/>"
            f"<b>Email:</b> {response_data['student']['email']}"
        )
        student_style = ParagraphStyle(
            "StudentStyle",
            parent=getSampleStyleSheet()["BodyText"],
            spaceAfter=12,
            fontName="Helvetica-Bold",
        )
        story.append(Paragraph(student_info, student_style))
        # Approved Destinations
    
        
        
        # destination_info = "<b>Asignaturas que te serán reconocidas en UGD para la Carrera:</b><br/>" + "<br/>".join(
        #     f"- {dest}" for dest in response_data["approved_destination_name"]
        # )
        
        destination_info = "<b>Asignaturas que te serán reconocidas en UGD para la Carrera:</b><br/>" + "<br/>".join(
            f"- {dest['destination_name']}" for dest in response_data["approved_destination_name"]
        )
        
        
        
        
        destination_style = ParagraphStyle(
            "DestinationStyle", parent=getSampleStyleSheet()["BodyText"], spaceAfter=12
        )
        story.append(Paragraph(destination_info, destination_style))
        # Programs
        program_style = ParagraphStyle(
            "ProgramStyle", parent=getSampleStyleSheet()["BodyText"], spaceAfter=12
        )
        study_plan_style = ParagraphStyle(
            "StudyPlanStyle",
            parent=getSampleStyleSheet()["BodyText"],
            spaceAfter=6,
            leftIndent=20,
        )
        story.append(Paragraph("<b>Asignaturas que te quedan pendientes para la Carrera:</b>", program_style))
        for program in response_data["programs"]:
            story.append(
                Paragraph(f"<b>Program Name:</b> {program['name']}", program_style)
            )
            for study_plan in program["study_Plan"]:
                course_info = f"Course Code: {study_plan['code']} - Course Name: {study_plan['name']}"
                story.append(Paragraph(course_info, study_plan_style))
        # Footer
        signature = "UGD"
        query_id = f"Query ID: {response_data['student']['id']}"
        footer_style = ParagraphStyle(
            "FooterStyle",
            parent=getSampleStyleSheet()["BodyText"],
            spaceBefore=12,
            fontName="Helvetica-Bold",
        )
        footer_text = f"<b>{signature}</b><br/>{query_id}"
        story.append(Paragraph(footer_text, footer_style))
        # Build PDF document with automatic pagination
        doc.build(
            story, onFirstPage=self.add_page_number, onLaterPages=self.add_page_number
        )
        buffer.seek(0)
        student_instance.report.save(
            f"{student_instance.id}_output.pdf", ContentFile(buffer.read())
        )
        # Get the URL of the saved PDF file
        pdf_url = student_instance.report.url
        print(pdf_url)
        buffer.close
        return pdf_url
    def add_page_number(self, canvas, doc):
        """
        Add the page number at the bottom of each page.
        """
        page_num = canvas.getPageNumber()
        text = f"Page {page_num}"
        canvas.drawRightString(letter[0] - 10, 10, text)
        
    def post(self, request, *args, **kwargs):
        destination_university = request.data.get("destination_university", None)
        origin_university = request.data.get("origin_university", None)
        origin_course_names = request.data.get("origin_course_names", None)
        student_id = request.data.get("student_id", None)
        if not (destination_university and origin_university):
            return Response(
                {"error": "Missing required parameters."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            destination_university_instance = University.objects.get(
                id=destination_university
            )
        except University.DoesNotExist:
            return Response(
                {"error": "Invalid university ID."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        queryset = Equivalence.objects.filter(
            destination_university=destination_university,
            origin_university=origin_university,
        )
        # Conditionally filter by origin_course_names if not "All"
        if origin_course_names and origin_course_names != "All":
            queryset = queryset.filter(origin_course_name__in=origin_course_names)
        serializer = self.serializer_class(queryset, many=True)
        # Retrieve student data based on student_id
        try:
            student_instance = Student.objects.get(id=student_id)
            student_serializer = self.student_serializer_class(student_instance)
        except Student.DoesNotExist:
            return Response(
                {"error": "Invalid student ID."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        mapped_queryset = Equivalence.objects.filter(
            destination_university=destination_university,
            origin_university=origin_university,
        )
        mapped_serializer = self.serializer_class(mapped_queryset, many=True)
        #  Extract all destination names from mapped data
        all_mapped_data = mapped_serializer.data
        all_destination_names = [item["destination_name"] for item in all_mapped_data]
        print("Serializer Data:", serializer.data)
        print("All Destination Names:", all_destination_names)
        
        
        
        # for filtering based on origin_course_names
        
        approved_destination_names = [
            item["destination_name"]
            for item in serializer.data
            if item["destination_name"] in all_destination_names
        ]
        
        
        
        
        # Filter approved_destination_name based on mapping with origin_course_names
        approved_destination_name = [
            {
                "destination_name": item["destination_name"],
                "destination_program": {
                    "id": item["destination_program"],
                    "name": Program.objects.get(id=item["destination_program"]).name,
                },
            }
            for item in serializer.data
            if item["destination_name"] in all_destination_names
        ]
        programs_queryset = Program.objects.filter(
            university=destination_university_instance
        )
        programs_serializer = self.program_serializer_class(
            programs_queryset, many=True
        )
        
        
        
        
        for program_data in programs_serializer.data:
            program_data["study_Plan"] = [
                study_plan
                for study_plan in program_data["study_Plan"]
                if study_plan["name"] not in approved_destination_names  
            ]
            
        
        response_data = {
            "student": student_serializer.data,
            "approved_destination_name": approved_destination_name,
            "programs": programs_serializer.data,
        }
        pdf_url = self.generate_pdf_response(response_data, student_instance)
        response_data.update(
            {
                "pdf_url": " https://virtual.ugd.edu.ar" + pdf_url,
            }
        )
        return Response({"destination_name": response_data})









class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 201:
            student_instance = response.data

            send_query_creation_email(sender=None, instance=student_instance)

        return response


class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]
