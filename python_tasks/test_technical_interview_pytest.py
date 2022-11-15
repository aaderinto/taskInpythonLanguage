import technical_interview

def test_upperStringConversion_output():
    assert technical_interview.upperStringConversion('english') == 'ENGLISH'

def test_sentenceCase_output():
    assert technical_interview.sentenceCase('I AM A MAN') == ('I am a man', 'i am a man')

def test_powerN_output():
    assert technical_interview.powerN(7,5) == 16807

def test_checkIfStringIsPalindrome_output():
    assert technical_interview.checkIfStringIsPalindrome('MADAM') == "The string is a Palindrome"
    assert technical_interview.checkIfStringIsPalindrome('Hello') == "The string is not a Palindrome"

