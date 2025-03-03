from twttr import shorten
import pytest



def test_shorten():
    assert shorten("KARRAR") == "KRRR"  # Preserves uppercase
    assert shorten("hello") == "hll"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("Python") == "Pythn"
    assert shorten("12345") == "12345"  # Numbers remain unchanged
    assert shorten("AEIOUaeiou") == ""  # All vowels removed
    assert shorten("CS50") == "CS50"  # No vowels removed
    assert shorten("CS,50") == "CS,50"  # No vowels removed
