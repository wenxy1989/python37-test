class Payable:
  def __init__(self,count=0,name='Payable'):
    self._count = count
    self._name = name

  def subtract(self,count):
    if self._count >= count:
      self._count -= count
      return True
    return False

  def plus(self,count):
    self._count += count
	
  def add(self,to):
    self.plus(to._count)
	
  def remove(self,to):
    return self.subtract(to._count)

  def print(self):
    print('%s is %d' % (self._name,self._count))

  def pay(self,t,num):
    if self.subtract(num):
      t.plus(num)
      return True
    return False

class Container:
  
  def __init__(self,payables = []):
    self._payables = dict()
    for x in payables:
      self.add(x)

  def add(self,payable):
    if self._payables.__contains__(payable._name):
      self._payables[payable._name].sum(payable)
    else:
      self._payables[payable._name] = payable

  def print(self):
    for x in self._payables.values():
      x.print()


class Cash(Payable):
  def __init__(self,count=0):
    super(Cash,self).__init__(count,'Cash')

  def getWeight(self):
    return 20

class Coin(Payable):
  def __init__(self,count=0):
    super(Coin,self).__init__(name='Coin',count=count)

  def getWeight(self):
    return 200

class Paper(Payable):

  def getWeight(self):
    return 50


def main():
  container = Container()
  container.add(Cash())
  container.add(Payable())
  container.add(Coin())
  container.print()


if __name__ == '__main__':
  main()
