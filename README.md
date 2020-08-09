
 # Description of Module
In this module I have developed a class Qualean  class that is inspired by Boolean+Quantum concepts.
 We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place.   

 Various functions are as below

## __init__:

This is a default Constuctor for the class Qualean. It takes (-1,0,1) or Boolean True or False. Any values other than these are
not allowed and should throw ValueError

## __add__: 
    
    This function takes anothe Qualean object as argument and returns sum as a new Qualean object

## __eq__:

This function takes another Qualean object as argument and returns true if real and imaginary parts are equal else return False

## __ float__:

This method returns the float value of real part of the Qualean object

## __mul__:
    
    This function takes anothe Qualean object as argument and returns multiplication of the both the objects as a new Qualean object 
## __ge__ :

This method takes another Qualean object and returns true if the current object is greater than or equal to input object

## __gt__ :

This method takes another Qualean object and returns true if the current object is greater than the input object

## __le__ :

This method takes another Qualean object and returns true if the current object is less than or equal to input object

## __gt__ :

This method takes another Qualean object and returns true if the current object is less than the input object


## __invertsign__

This method inverts teh sign of both real and imaginary part of Qualean object

## sqrt:

This method finds the square root of the given Qualean object. In case real part is negative, it populates the imaginary part of object


## __and__:

This method takes anotehr object as argument and performs return Boolean value of and operation

## __bool__:

This method returns the boolean value of the object


In addition to verifying individual functions, unit test is performed for 

- Sum object 100 times should be equal to times of real value of object
- Million times sum should not be close to 0



 
 
 
 
 

    
    
    
    