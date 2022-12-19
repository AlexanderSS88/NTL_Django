from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        quantity_stud = Course.objects('students')
        if quantity_stud > 20:
            raise ValidationError(
                "You have more than 20 students in group"
                )
        return data

