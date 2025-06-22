import unittest
from main import calculate_gpa, calculate_cgpa

class TestTranscriptFunctions(unittest.TestCase):

    def test_gpa_calculation(self):
        # AA and BB -> should average around 3.43
        courses = [
            {'code': 'CS101', 'name': 'Intro CS', 'grade': 'AA', 'credits': 3},
            {'code': 'MATH101', 'name': 'Math', 'grade': 'BB', 'credits': 4}
        ]
        self.assertAlmostEqual(calculate_gpa(courses), 3.43, places=2)

    def test_gpa_calculation2(self):
        # Just testing one course
        courses = [
            {'code': 'CS101', 'name': 'Intro', 'grade': 'BA', 'credits': 5}
        ]
        self.assertEqual(calculate_gpa(courses), 3.5)

    def test_gpa_calculation_ex(self):
        # grade W should be ignored
        courses = [
            {'code': 'CS101', 'name': 'Intro', 'grade': 'W', 'credits': 3},
            {'code': 'CS102', 'name': 'Next', 'grade': 'AA', 'credits': 3}
        ]
        self.assertEqual(calculate_gpa(courses), 4.0)

    def test_gpa_calculation_error(self):
        # Unknown grade should count as 0
        courses = [
            {'code': 'X101', 'name': 'Unknown', 'grade': 'ZZ', 'credits': 2},
            {'code': 'Y101', 'name': 'Normal', 'grade': 'CC', 'credits': 3}
        ]
        self.assertAlmostEqual(calculate_gpa(courses), 1.2, places=1)

    def test_gpa_calculation_empty(self):
        # empty list
        self.assertEqual(calculate_gpa([]), 0.0)

    def test_gpa__calculation_all_ex(self):
        # all W or EX
        courses = [
            {'code': 'A', 'name': 'Test1', 'grade': 'EX', 'credits': 3},
            {'code': 'B', 'name': 'Test2', 'grade': 'W', 'credits': 2}
        ]
        self.assertEqual(calculate_gpa(courses), 0.0)

    def test_cgpa_calculation(self):
        semesters = [
            {'name': 'Fall', 'courses': [
                {'code': 'A', 'name': 'A', 'grade': 'AA', 'credits': 2},
                {'code': 'B', 'name': 'B', 'grade': 'BB', 'credits': 3}
            ]},
            {'name': 'Spring', 'courses': [
                {'code': 'C', 'name': 'C', 'grade': 'CC', 'credits': 2}
            ]}
        ]
        # CGPA should be 3.0
        self.assertAlmostEqual(calculate_cgpa(semesters), 3.0, places=2)

    def test_cgpa_calculation_repeated_courses(self):
        # FF first, BB later -> BB should count
        semesters = [
            {'name': 'Fall', 'courses': [
                {'code': 'CS101', 'name': 'Intro', 'grade': 'FF', 'credits': 4}
            ]},
            {'name': 'Spring', 'courses': [
                {'code': 'CS101', 'name': 'Intro', 'grade': 'BB', 'credits': 4}
            ]}
        ]
        self.assertEqual(calculate_cgpa(semesters), 3.0)

    def test_cgpa_calculation_all_error(self):
        semesters = [
            {'name': 'Only', 'courses': [
                {'code': 'Z', 'name': 'Dummy', 'grade': 'I', 'credits': 2}
            ]}
        ]
        self.assertEqual(calculate_cgpa(semesters), 0.0)

if __name__ == "__main__":
    print("Running test cases...\n")
    unittest.main()
