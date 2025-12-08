import unittest
import random
import io
import sys
from datetime import datetime
from canvasacademicinsights.canvasaianalyzer import clean
from canvasacademicinsights.canvasaianalyzer import model
from canvasacademicinsights.canvasaianalyzer import grades
from canvasacademicinsights.canvasaianalyzer import organize
from canvasacademicinsights.canvasmain import canvasdataretriever as c 


class TestAI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    
    def setUp(self):
        courses = []
        for j in range(5): 
            gradeList = []
            sampleCourse = [
                "courseid",
                "coursename",
                "courseenrollment",
            ]

            counter = 1
            for i in range(10): 
                counter += 1
                if random.random() > 0.5:
                    gradeList.append(c.QuizGrade(name = f"Test{random.random()}", score = random.random() * 100, total = 100, date = datetime.strptime(f"2025-11-{counter}", "%Y-%m-%d")))
                else:
                    gradeList.append(c.AssignmentGrade(name = f"Test{random.random()}", score = random.random() * 100, total = 100, date = datetime.strptime(f"2025-11-{counter}", "%Y-%m-%d")))
            sampleCourse.append(gradeList)
            courses.append(sampleCourse)
            self.courses = courses
            self.ai = model.AI()
            
    def testCleanData(self):
        clean.cleanCourseData(self.courses)
        self.assertEqual(len(self.courses), 5)
        for c in self.courses:
            self.assertGreater(len(c[0]), 0)
            self.assertGreater(len(c[1]), 0)
            self.assertGreater(len(c[2]), 0)
            self.assertEqual(len(c[3]), 10)
    
    def testAI(self):
        sys.stdout = io.StringIO()

        grades.gradesAsk(self.courses)
        output = sys.stdout.getvalue()
        self.assertGreater(output.count("\n"), 3)

        grades.studyPlanAsk(self.courses)
        output = sys.stdout.getvalue()
        self.assertGreater(output.count("\n"), 3)

        grades.strongCourseAsk(self.courses)
        output = sys.stdout.getvalue()
        self.assertGreater(output.count("\n"), 3)
        
        organize.dueDatesAsk(self.courses)
        output = sys.stdout.getvalue()
        self.assertGreater(output.count("\n"), 3)

        organize.studyScheduleAsk(self.courses)
        output = sys.stdout.getvalue()
        self.assertGreater(output.count("\n"), 3)

        organize.studyPlanAsk(self.courses)
        output = sys.stdout.getvalue()
        self.assertGreater(output.count("\n"), 3)
        
    @classmethod
    def tearDownClass(cls):
        pass
        
