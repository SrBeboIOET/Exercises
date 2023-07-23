from Exercise3 import get_average_note_class, get_average_notes_student, students

def test_get_average_notes_student(): #function to test the function get_average_notes_student
    average=0
    average_expected=8.267 #arrange

    average=sum(students["Juan"].values())/len(students["Juan"].values()) #act

    assert round(average,3) == average_expected #assert 

def test_get_average_note_class(): #function to test the function get_average_note_class
    average=0
    average_expected=8.156

    average= sum(get_average_notes_student(student) for student in students)/len(students)

    assert round(average,3) == average_expected
