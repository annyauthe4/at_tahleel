from django.test import TestCase
from .models import StudentProfile, User

class StudentTestCase(TestCase):
    def test_create_student(self):
        user = User.objects.create(username='Seun', is_student=True)
        student = StudentProfile.objects.create(user=user, admission_number='ATL001', dob='2005-01-01')
        self.assertEqual(student.admission_number, 'ATL001')
