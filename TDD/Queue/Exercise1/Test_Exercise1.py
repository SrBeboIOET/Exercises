from Exercise1 import sort_queue

def test_sort_queue():
    values=[8, 3, 2, 1]
    expect_values=[1, 2, 3, 8] #arrange

    values= sort_queue(values) #act

    assert values == expect_values #assert
