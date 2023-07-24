from Exercise1 import is_balance_string

def test_is_balance_string():
    string = "(([]))"
    expected_result= True #arrange

    string = is_balance_string(string) #act

    assert string == expected_result #assert
