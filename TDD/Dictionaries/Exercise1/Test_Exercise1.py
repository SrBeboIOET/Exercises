from Functions_exercise1 import get_name_path_file
import os

def test_get_name_path_file():
    result = get_name_path_file("Notas.txt") #arrange

    expected_output = "The name of file is: Notas.txt\nThe path of file is: " + os.path.abspath("Notas.txt") #act

    assert result == expected_output #assert
