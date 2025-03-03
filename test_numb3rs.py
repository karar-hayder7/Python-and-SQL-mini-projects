from numb3rs import validate as va



def test_negative() :
    assert va('-1.1.1.1') == False
    assert va('1.1.1.1') == True



def test_over225() :
    assert va('255.255.256.1') == False
    assert va('255.255.255.1') == True
