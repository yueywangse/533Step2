import unittest
import random
import io
import sys
from datetime import datetime
from canvasacademicinsights.canvasaianalyzer import model
from canvasacademicinsights.canvasaianalyzer import grades
from canvasacademicinsights.canvasaianalyzer import organize
from canvasacademicinsights.canvasmain import canvasdataretriever as c 


class TestAIPrompt(unittest.TestCase):
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
    
    def testGrades(self):
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
    
    def testOrganize(self):
        organize.dueDatesAsk(self.courses)
        output = sys.stdout.getvalue()
        self.assertGreater(output.count("\n"), 3)

        organize.studyScheduleAsk(self.courses)
        output = sys.stdout.getvalue()
        self.assertGreater(output.count("\n"), 3)

        organize.studyPlanAsk(self.courses)
        output = sys.stdout.getvalue()
        self.assertGreater(output.count("\n"), 3)
    
    def tearDown(self):
        self.courses = None
        self.ai = None

    @classmethod
    def tearDownClass(cls):
        pass
        
