from CursoBase import Curso
class PdfCourse(Curso):
    def __init__(self, titulo, instructor, precio, clases, pages):
        super().__init__(titulo, instructor, precio, clases)
        self.pages = pages