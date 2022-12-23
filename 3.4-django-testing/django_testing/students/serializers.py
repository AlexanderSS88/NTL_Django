from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        model = Course.objects.filter(name=data['name'])
        quan_std_db = 0
        for pos in model:
            quan_std_db = pos.students.count()
        if (self.context['request'].method in ['POST']
            and (len(data['students']) >
                 settings.MAX_STUDENTS_PER_COURSE)):
            raise ValidationError(
                "You have more than 20 students on one course"
            )
        elif ((quan_std_db + len(data['students']) >
               settings.MAX_STUDENTS_PER_COURSE)
            and (self.context['request'].method in ['PATCH'])):
                raise ValidationError(
                    "You want to add more than 20 students on one course"
                    )
        return data


