
import abc
class A(abc.ABC):#自己定义一个抽象基类,
    @abc.abstractmethod
    def eat(self):
        pass
    
class B(A):#继承抽象基类
    def voice(self):
        pass
        
if __name__ == "__main__":
    a = A() 