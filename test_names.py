from names import make_full_name, extract_family_name, extract_given_name
import pytest

def main():
    test_make_full_name()
    test_extract_family_name()



def test_make_full_name():
    
    A = make_full_name("Hunter", "Bird")

    assert A == "Bird;Hunter", "HERE"

    print(f"{A}")




def test_extract_family_name():

    preA = make_full_name("Hunter", "Bird")

    A = extract_family_name(preA)

    assert A == "Bird", "HERE2"

    print(f"{A}")



def test_extract_given_name():
    
    preA = make_full_name("Hunter", "Bird")

    A = extract_given_name(preA)

    assert A == "Hunter", "Here3"



main()



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
