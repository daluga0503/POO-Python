from VideoCourse import VideoCourse
from PdfCourse import PdfCourse
from CursoBase import Curso


curso1 = VideoCourse('Curso 1', 'Instructor 1', 25, 5, 150)
curso2 = PdfCourse('Curso 2 ', 'Instructor 2', 10, 1, 200)


curso1.new_user_enrolled('Daniel')
curso1.new_user_enrolled('Ana')
curso2.new_user_enrolled('Luis')
curso2.new_user_enrolled('Maria')
curso1.received_a_rating(4)
curso1.received_a_rating(5)
curso2.received_a_rating(3)
curso2.received_a_rating(4)

print(Curso.seach_course_by_name('Curso 1'))
print(Curso.seach_course_by_name('Curso 2 '))
print(Curso.seach_course_by_name('Curso 3'))
print(Curso.show_details())