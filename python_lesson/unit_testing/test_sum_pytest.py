import bodmas

def test_addition_output():
    assert bodmas.add(3, 2) == 5

def test_sub_output():
    assert bodmas.subtraction(7, 6) == 1