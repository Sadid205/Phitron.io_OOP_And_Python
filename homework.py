"""
1. calculator class to add,deduct,multiply,divide
2. Pen class. create three object with different instance attributes
3.Exam attend_to_exam get marks
"""

# class Pen:
#     manufactured_in='Bangladesh'

#     def __init__(self,name,color):
#         self.name = name
#         self.color = color


# my_pen = Pen('Econo','Black')
# her_pen=Pen('Matador','Red')
# teacher_pen = Pen('Chcochoco','Blue')

# print(my_pen.name,my_pen.color)
# print(her_pen.name,her_pen.color)
# print(teacher_pen.name,teacher_pen.color)


class Exam:
    
   

    def __init__(self,Marks,Subject):
        self.Marks = Marks
        self.Subject = Subject
        self.Attendance = []

    def Attend(self,Name,Roll,marks):
        student_info = {"Name":Name,"Roll":Roll,"Marks":marks}
        self.Attendance.append(student_info)

    def get_Marks(self,Roll):
       for student in self.Attendance:
           if student['Roll'] == Roll:
               return f'Here is your Marks:{student['Marks']} ' 
           else:
               return 'We can not find your result'


Mid_Term = Exam(100,'Chemistry')
Mid_Term.Attend('Sadid',29,86)
attendance = Mid_Term.get_Marks(29)
print(attendance)
