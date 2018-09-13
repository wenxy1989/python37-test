class Substance:

  def __init__(self,name='Substance'):
    self._name = name
    self._substance = dict()

  def _contains(self,key):
    return self._substance.__contains__(key)

  def _create(self,key,value):
    self._substance[key] = value

  def plus(self,key,count):
    if self._contains(key):
      self._substance[key] += count
    else:
      self._create(key,count)

  def subtract(self,key,count):
    if self._contains(key):
      if self._substance[key] >= count:
        self._substance[key] -= count
        return True
    return False

  def pay(self,substance,key,count):
    if self.subtract(key,count):
      substance.plus(key,count)
      return True
    return False

  def accept(self,substance,key,count):
    return substance.pay(self,key,count)

  def request(self,substance,key,count):
    pay_number = substance.get_number(key)
    if pay_number >= count:
      pay_number = count
    substance.pay(self,key,pay_number)

  def response(self,substance,key,count):
    return substance.request(self,key,count)

  def get_value(self,key):
    if self._contains(key):
      return self._substance[key]
    return None

  def get_number(self,key):
    v = self.get_value(key)
    if v:
      return v
    return 0

  def weight(self):
    w = 0
    for x in self._substance.values():
      if type(x) == type(0):
        w += x
    return w

  def __str__(self):
    return 'name:%s,substanc:%s' % (self._name,self._substance)
    
	

class Solid(Substance):
  def __init__(self,name='Solid'):
    super(Solid,self).__init__(name)
    self.plus('name',name)

class Water(Solid):
  def __init__(self,count=0):
    super(Water,self).__init__('Water')
    self.plus('H2O',0.97*count)
    self.plus('Salt',0.03*count)

class Plant(Substance):
  def __init__(self,name='Plant'):
    super(Plant,self).__init__(name)
    self.plus('Wood',100)
    self.plus('H20',1100)

  def absorb(self,obj):
    key = 'H2O'
    count = 60
    self.request(obj,key,count)
    print('absorb %s %d' %(key,count))


def main():
  water = Water(1000)
  grass = Plant('Grass')
  print(water)
  print('grass : %s' % grass)
  grass.absorb(water)
  grass.absorb(water)
  print('grass : %s' % grass)
  print(water)

if __name__ == '__main__':
  main()
