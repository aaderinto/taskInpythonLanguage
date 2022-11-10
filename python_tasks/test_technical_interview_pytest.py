import technical_interview

def test_upperStringConversion_output():
    assert technical_interview.upperStringConversion('english') == 'ENGLISH'

def test_sentenceCase_output():
    assert technical_interview.sentenceCase('I AM A MAN') == ('I am a man', 'i am a man')

