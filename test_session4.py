import pytest
import random
import string
import session4
import os
import inspect
import re
import math
from decimal import Decimal

README_CONTENT_CHECK_FOR = [
    'Qualean',
    'init',
    'add',
    'or',
    'bool',
    'eq',
    'float',
    'sqrt',
    'repr',
    'str',
    'le',
    'lt',
    'gt',    
    'ge',
    'mul',  
    'invertsign'  
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10
    
def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    missing = []
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            missing.append(c)
            #pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file" + str(missing)

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"        

def test_function_create_qualean_valid_input():    
    q1= session4.Qualean(1)
    q2 = session4.Qualean(0)
    q3 = session4.Qualean(-1)
    q4 = session4.Qualean(True)
    q5 = session4.Qualean(False)    
    assert q1 is not None and q2 is not None and q3 is not None and q4 is not None and q5 is not None
    

def test_function_create_qualean_invalid_input():    
    with pytest.raises(ValueError):
        session4.Qualean(1.1)
    with pytest.raises(ValueError):
        session4.Qualean("abc")
    
def test_function_add_valid_input():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(-1)
    q3 = q1 + q2
    assert math.isclose(q3.real, q1.real + q2.real)
    
def test_function_add_invalid_input():
    with pytest.raises(ValueError):
        session4.Qualean(1) + "abc" 

def test_function_add_decimal():
    q1 = session4.Qualean(1)
    q2 = Decimal(0.5)
    q3 = q1 + q2
    assert math.isclose(q3.real, q1.real + float(q2)) 

def test_repr():
    q1 = session4.Qualean(1)
    assert "Real: " + str(q1.real) + " Imaginary: " + str(q1.img) == str(q1) 
        
def test_str():
    q1 = session4.Qualean(1)    
    assert "Real: " + str(q1.real) + " Imaginary: " + str(q1.img) == str(q1)
    
def test_eq():
    q1 = session4.Qualean(1) 
    q2 = q1    
    assert q1==q2
    
def test_not_eq():
    q1 = session4.Qualean(1) 
    q2 = session4.Qualean(0)    
    assert not(q1==q2)
    
def test_invalid_eq():
    q1 = session4.Qualean(1) 
    q2 = "abc"
    assert not(q1==q2)
    
def test_ge():
    q1 = session4.Qualean(1)
    q1.real = abs(q1.real)
    q1.img = abs(q1.img)     
    q2 = session4.Qualean(0) 
    assert q1 >= q2
    
def test_gt():
    q1 = session4.Qualean(1)
    q1.real = abs(q1.real)
    q1.img = abs(q1.img)    
    q2 = session4.Qualean(0) 
    assert q1 > q2
    
def test_le():
    q1 = session4.Qualean(1)
    q1.real = abs(q1.real)
    q1.img = abs(q1.img)
    q2 = session4.Qualean(0) 
    assert q2 <= q1
    
def test_lt():
    q1 = session4.Qualean(1)
    q1.real = abs(q1.real)
    q1.img = abs(q1.img)
    q2 = session4.Qualean(0) 
    assert q2 < q1
    
def test_sqrt():
    q1 = session4.Qualean(1)
    q1.real = -abs(q1.real)
    q2 = q1.__sqrt__()    
    assert q2.img != 0.0    
    
def test_function_mul_valid_input():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(-1)
    q3 = q1 * q2
    assert math.isclose(q3.real, q1.real * q2.real)
    
def test_function_mul_invalid_input():
    with pytest.raises(ValueError):
        session4.Qualean(1) * "abc" 

def test_invert_sign():
    q1 = session4.Qualean(1)
    q2 = q1.__invertsign__()
    assert q2.real == -q1.real and q2.img == -q1.img, "invert_sign operation changes sign of both real and imaginary parts"
    
def test_float():
    q1 = session4.Qualean(1)
    val = float(q1)
    assert q1.real == val, " Float value of object must be equal to real value"

def test_sum_100_times():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    for _ in range(100):
        q2 = q2 + q1        
    assert math.isclose(q2.real, 100*q1.real)
    
def test_sum_million_times():
    q1 = session4.Qualean(0)
    for _ in range(1000000):
        q1 = q1 + session4.Qualean(random.choice([-1,0,1]))       
    assert math.isclose(q1.real, 0.0, rel_tol=500.0)    

def test_bool():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    assert q1 
    assert not(q2)    
    
def test_and():
    q1 = session4.Qualean(0)
    q2 = session4.Qualean(1)
    assert not(q1 and q2)
    
def test_or():
    q1 = session4.Qualean(0)
    q2 = session4.Qualean(1)
    assert q1 or q2

def test_sqrt_decimal():
    q1 = session4.Qualean(1)
    q1.real = abs(q1.real)
    q2 = q1.__sqrt__()
    q3 =  math.sqrt(Decimal(q1.real))    
    assert math.isclose(q2, q3)

def test_mixed_operation():
    q1 = session4.Qualean(1)
    q2 = session4.Qualean(0)
    q3 = session4.Qualean(-1)        
    assert q1*q2+q3==q3
   

        

    
    

    

       
    
    
  
    

    
    

        
   