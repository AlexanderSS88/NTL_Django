from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        model = Course.objects.filter(name=data['name'])
        quantity_std_in_db = 0
        for pos in model:
            quantity_std_in_db = pos.students.count()
        if (self.context['request'].method in ['POST']
            and len(data['students']) > 20):
            raise ValidationError(
                "You have more than 20 students on one course"
            )
        elif (self.context['request'].method in ['PATCH']
            and quantity_std_in_db + len(data['students']) > 20):
                raise ValidationError(
                    "You want to add more than 20 students on one course"
                    )
        return data


