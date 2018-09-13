import payable as pay


class Human:
  
  def __init__(this,name='Human'):
    this._name = name
    this.object_dict = dict()
    this.action_dict = dict()
    
  def hit(self,obj):
    print('hit %s',obj.to_string())

  
  def give(self,to,obj):
    if self.remove_object(obj):
      to.add_object(obj)
      return True
    return False

  def add_object(self,obj):
    if self.object_dict.__contains__(obj._name):
      self.object_dict[obj._name].add(obj)
    else:
      self.object_dict[obj._name] = obj
  
  def remove_object(self,obj):
    if self.object_dict.__contains__(obj._name):
      return self.object_dict[obj._name].remove(obj)
    return False

  def print(self):
    print('Human %s' % self._name)
    for x in self.object_dict.values():
      x.print()
        

class Cat:

  def __init__(this,name='Cat'):
    self._name = name

def main():
  person = Human('person')
  p2 = Human('person 2')

  coin = pay.Coin(100)
  
  person.add_object(coin)
  person.print()
  p2.print()

  result = person.give(p2,pay.Coin(99))
  print('%s give %s result %s' % (person._name,p2._name,result))
  
  person.print()
  p2.print()
  
if __name__ == '__main__':
  main()
