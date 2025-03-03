from working import convert
import pytest



def test_bla ():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


def test_v ():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

