from django.conf import settings

from students.models import Course, Student
from rest_framework.test import APIClient
from model_bakery import baker
import pytest



@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_add_one_course(client, course_factory):
    #Arrange
    new_course = course_factory(_quantity=1)
    #Act
    response = client.get('/courses/')
    #Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == new_course[0].name


@pytest.mark.django_db
def test_add_list_of_courses(client, course_factory):
    # Arrange
    new_courses = course_factory(_quantity=10)
    # Act
    response = client.get('/courses/')
    # Assert
    assert response.status_code == 200
    data = response.json()
    for i, m in enumerate(data):
        assert m['name'] == new_courses[i].name


@pytest.mark.django_db
def test_add_courses_and_id_filter(client, course_factory):
    # Arrange
    new_courses = course_factory(_quantity=10)
    # Act
    response = client.get(f'/courses/?id={new_courses[7].id}')
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == new_courses[7].id


@pytest.mark.django_db
def test_add_courses_and_name_filter(client, course_factory):
    # Arrange
    new_courses = course_factory(_quantity=10)
    # Act
    response = client.get(f'/courses/?name={new_courses[5].name}')
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == new_courses[5].name


@pytest.mark.django_db
def test_create_one_course(client):
    # Arrange
    new_course = {'name': 'NETOLOGY', 'students': []}
    # Act
    response = client.post('/courses/', data=new_course)
    # Assert
    assert response.status_code == 201
    data = response.json()
    for pos in new_course:
        assert (data[pos] == new_course[pos])


@pytest.mark.django_db
def test_update_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)
    position = 'NETOLOGY'
    # Act
    response = client.patch(f'/courses/{course[5].id}/', data={'name': position, 'students': []})
    # Assert
    new_name = client.get(f'/courses/{course[5].id}/').json()
    assert response.status_code == 200
    assert new_name['name'] == position


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)
    # Act
    response = client.delete(f'/courses/{course[8].id}/')
    new_quantity_courses = client.get('/courses/').json()
    response2 = client.delete(f'/courses/{course[8].id}/')
    # Assert
    assert response.status_code == 204
    assert response2.status_code == 404
    for pos in new_quantity_courses:
        assert course[8].id != pos['id']
    assert len(new_quantity_courses) == len(course) - 1




@pytest.mark.parametrize(
    ,course_factory(_quantity=10))
# @pytest.fixture
# def max_students_number(settings):
#     settings.MAX_STUDENTS_PER_COURSE = 20
#     assert settings.MAX_STUDENTS_PER_COURSE
#
# def course_factory():
#     def factory(*args, **kwargs):
#         return baker.make(Course, *args, **kwargs)
#     return factory
#
# def test_add_max_students(course_factory, max_students_number):
#     # Arrange
#     new_course = course_factory(_quantity=1)
#     title_course = new_course[0].name
#     for id in range(15):
#         baker.make(title_course)
#         @pytest.mark.parametrize(
#     )
#     course_factory(_quantity=15, name=title_course)
#     # Act
#     response = client.get('/courses/')
#     assert response.status_code == 200
#     data = response.json()
#     assert len(data) == 1
#     for pos in data[0]:
#         print (pos['students'])
#     assert data[0]['name'] == new_course[0].name


    # students_bjects = student_factory(_quantity=10)
    # assert max_students_number <= len(students_bjects)
    #
