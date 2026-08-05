import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "School_Mgt_System"))

import app as school_app
import school as school_module
from school import School
from student import Student


class SchoolAppTests(unittest.TestCase):
    def setUp(self):
        school_app.my_school = School("Hazara Public School", "123 Main St")

    def test_save_to_file_uses_app_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
                school = School("Test School", "Test Address")
                school.save_to_file("STUDENT", Student("Ali", "1", "A"))
                expected_path = Path(school_module.__file__).resolve().parent / "school_data.txt"
                self.assertTrue(expected_path.exists())
                self.assertIn("Ali", expected_path.read_text(encoding="utf-8"))
            finally:
                os.chdir(old_cwd)

    def test_teacher_form_accepts_template_field_names(self):
        client = school_app.app.test_client()
        response = client.post(
            "/add_teacher",
            data={"name": "Ada", "id": "7", "subject": "Math"},
            follow_redirects=False,
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(school_app.my_school.teachers), 1)
        self.assertEqual(school_app.my_school.teachers[0].name, "Ada")
        self.assertEqual(school_app.my_school.teachers[0].specialization, "Math")
        self.assertEqual(school_app.my_school.teachers[0].contact, "7")


if __name__ == "__main__":
    unittest.main()
