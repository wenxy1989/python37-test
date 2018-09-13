class X(object):
  def f(self):
    print('x')

class A(X):
  def f(self):
    print('a')

  def extral(self):
    print('extral a')

class B(X):
  def f(self):
    print('b')

  def extral(self):
    print('extral b')
 
class C(A,B,X):
  def f(self):
    super(C,self).f()
    print('c')

def main():
  print(C.mro())

  c = C()
  c.f()
  c.extral()

if __name__ == '__main__':
  main()
