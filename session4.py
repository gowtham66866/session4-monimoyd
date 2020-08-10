import random
import math
from decimal import Decimal
class Qualean:
    def __init__(self, val):
        input = None
        try:
            input = float(val)
        except:
            raise ValueError("Check the type for constructor of Qualean")
            
        if input == 0.0 or input == 1.0 or input == -1.0:
            self.input = input
        else:
            raise ValueError("Input to class must be True/ False or 0/1/-1")
        if input == 0.0:
            self.real = 0.05
            self.real = 0.0
        else:
            self.real = float(round(self.input * random.uniform(-1.0, 1.0), 10))
        self.img = 0.0
        
    def __add__(self, obj):
        if obj is None:
            raise ValueError(" argument to add must not be None")
        if isinstance(obj, Qualean):
            q = Qualean(0)
            q.real = self.real + obj.real
            #print("self.real =", self.real,  " obj.real=", obj.real, " q.real=",q.real)
            q.img = float(self.img + obj.img)
            return q
        elif isinstance(obj, float) or isinstance(obj, int):
            q = Qualean(0)
            q.real = self.real + obj            
            return q
        elif isinstance(obj, Decimal):
            q = Qualean(0)
            q.real = self.real + float(obj)
            return q
        else:
            raise ValueError(" argument to add must be Qualean, Decimal, float, int")
    
    def __bool__(self):
        return self.real != 0.0
    
    def __and__(self, obj):
        return self.__bool__() and bool(obj)
        
    def __or__(self, obj):
        return self.__bool__() or bool(obj)
        
    def __repr__(self):
        return "Real: {0} Imaginary: {1}".format(self.real, self.img)
        
    def __str__(self):
        return "Real: {0} Imaginary: {1}".format(self.real, self.img)        
            
    def __eq__(self, obj):
        if obj is None:
            return False
        if isinstance(obj, Qualean):
            return math.isclose(self.real, obj.real) and math.isclose(self.img, obj.img) 
        else:
            return False    
    
    def __float__(self):
        return self.real        
    
    def __ge__(self, obj):
        if obj is None:
            raise ValueError(" Argument to __ge__ can not be None")
        if isinstance(obj, Qualean):
            return self.real >= obj.real
        else:
            raise ValueError(" Argument to __add__ must be instance of Qualean")
            
    def __gt__(self, obj):
        if obj is None:
            raise ValueError(" Argument to __ge__ can not be None")
        if isinstance(obj, Qualean):
            return self.real > obj.real
        else:
            raise ValueError(" Argument to __add__ must be instance of Qualean")
        
    def __invertsign__(self):
        q2 = Qualean(0)
        q2.real = -self.real 
        q2.img = -self.img
        return q2        
    
    def __ge__(self, obj):
        if obj is None:
            raise ValueError(" Argument to __ge__ can not be None")
        if isinstance(obj, Qualean):
            return self.real >= obj.real
        else:
            raise ValueError(" Argument ge must be instance of Qualean")
            
    def __le__(self, obj):
        if obj is None:
            raise ValueError(" Argument to __ge__ can not be None")
        if isinstance(obj, Qualean):
            return self.real <= obj.real
        else:
            raise ValueError(" Argument to __le__ must be instance of Qualean")            
    
    def __lt__(self, obj):
        if obj is None:
            raise ValueError(" Argument to __ge__ can not be None")
        if isinstance(obj, Qualean):
            return self.real < obj.real
        else:
            raise ValueError(" Argument to __add__ must be instance of Qualean")            
            
    def __sqrt__(self):
        q2 = Qualean(0)
        if self.real >= 0.0:
            q2.real = math.sqrt(self.real)
        else:
            q2.img = math.sqrt(-self.real)
            q2.real = 0.0             
        return q2            
    
    def __mul__(self, obj):
        if obj is None:
            raise ValueError(" argument to add must not be None")
        if isinstance(obj, Qualean):
            q = Qualean(0)
            q.real = self.real * obj.real
            #print("self.real =", self.real,  " obj.real=", obj.real, " q.real=",q.real)
            q.img = float(self.img * obj.img)
            return q
        elif isinstance(obj, float) or isinstance(obj, int):
            q = Qualean(0)
            q.real = self.real * obj            
            return q
        elif isinstance(obj, Decimal):
            q = Qualean(0)
            q.real = self.real * float(obj)
            return q
        else:
            raise ValueError(" argument to add must be Qualean, Decimal, float, int") 

          
            


 