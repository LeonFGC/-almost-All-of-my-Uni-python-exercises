from user import User
from materia import Subject
from subjectmanajer import SubjectManager
from view import View

view = View()
subject_manager = SubjectManager()

subject1 = Subject("quimica 1")
subject2 = Subject("quimica 2", prerequisites=[subject1])
subject3 = Subject("quimica 3", prerequisites=[subject2])

subject_manager.add_subject(subject1)
subject_manager.add_subject(subject2)
subject_manager.add_subject(subject3)

user = User("juan")

user.complete_subject(subject1)

view.display("Materias disponibles:")
for subject in subject_manager.subjects:
    subject_status = "Aprobada" if subject in user.completed_subjects else "No aprobada"
    view.display(f"{subject.name}: {subject_status}")

subject_choice = input("Ingresar la materia a inscribirse: ")
subject_choice=subject_choice.lower()

chosen_subject = subject_manager.get_subject(subject_choice)

if chosen_subject:
    if chosen_subject in user.completed_subjects:
        view.display("Esta materia ya esta aprobada.")
    else:
        prerequisites_completed = all(prereq in user.completed_subjects for prereq in chosen_subject.prerequisites)
        if prerequisites_completed:
            user.complete_subject(chosen_subject)
            view.display("Inscripcion exitosa.")
        else:
            view.display("Inscripcion fallida, falta completar correlativas.")
else:
    view.display("Opcion invalida.")
