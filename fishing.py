import math
import pyglet
import random
from cocos import layer
from cocos import scene
from cocos import sprite
from cocos import collision_model as collision
from cocos import actions
from cocos.director import director

WIN_WIDTH = 1024
WIN_HEIGHT = 768
fish_width = 55
fish_height = 296/8

class Cannon(sprite.Sprite):
  def __init__(self):
    super(Cannon,self).__init__('images/cannon7_single.png')
    self.position = WIN_WIDTH // 2 , 35
    self.scale = 0.8

  def fire(self,x,y):
    tanX = abs(x - self.position[0]) / float(y)
    radian = math.atan(tanX)
    angle = radian * 180 / math.pi
    if x < WIN_WIDTH // 2:
      angle = -angle
    duration = abs(angle)/200.0
    self.do(actions.RotateTo(angle,duration) + actions.CallFunc(self._fire_net,x = x,y = y))

  def _fire_net(self,x,y):
    #print('fire net x:%s,y:%s' % (x,y))

class Net(sprite.Sprite):
  def __init__(self):
    super(Net,self).__init__('images/web3.png')
    self.scale = 0
    self.position = WIN_WIDTH // 2,0
    self.cshape =  collision.AARectShape(collision.eu.Vector2(0,0),self.width // 2,self.height // 2)
    self.schedule(self._update_cshape)

  def _update_cshape(self,dc):
    self.cshape.center = collision.eu.Vector2(*self.position)

  def fire(self,x,y):
    self.do(actions.MoveTo((x,y),0.5) | actions.ScaleTo(0.5,0.5) + actions.Delay(0.5) + actions.CallFunc(self.explode))

  def explode(self):
    self.stop()
    self.kill()

class Fish(sprite.Sprite):
  def __init__(self):
    fish_pic = pyglet.resource.image('images/fish1.png')
    images = []
    for x in range(0,7):
      fish = fish_pic.get_region(0,fish_height*x,fish_width,fish_height)
      images.append(fish)
    animation = pyglet.image.Animation.from_image_sequence(images,0.05)
    super(Fish,self).__init__(animation)
    #super(Fish,self).__init__('images/fish_single.png')
    self.position = random.randint(self.width //2, WIN_WIDTH - self.width // 2),random.randint(self.height // 2,WIN_HEIGHT - self.height // 2)
    self.scale = 0.5
    self.cshape = collision.AARectShape(collision.eu.Vector2(0,0),self.width // 2,self.height // 2)
    self.schedule(self._update_cshape)

  def _update_cshape(self,dc):
    #self.swim()
    self.cshape.center = collision.eu.Vector2(*self.position)

  def swim(self):
    self.do(actions.MoveTo((-100,self.position[1]),3) + actions.CallFunc(self.explode))

  def explode(self):
    self.stop()
    self.kill()

class BackgroundLayer(layer.Layer):
  is_event_handler = True
  def on_mouse_press(self,x,y,*args,**kwargs):
    print('x:%s,y:%s' % (x,y))
    self.cannon.fire(x,y)
    net = Net()
    net.fire(x,y)
    self.add(net)
    self.nets.append(net)

  def __init__(self):
    super(BackgroundLayer,self).__init__()
    bg = sprite.Sprite('images/game_bg_2_hd.jpg')
    bg.position = WIN_WIDTH // 2,WIN_HEIGHT // 2
    self.cannon = Cannon()
    self.add(bg)
    self.add(self.cannon)
    self.collision_manager = collision.CollisionManager();
    self.fishs = []
    for x in range(1,100):
      fish = Fish()
      self.add(fish)
      self.fishs.append(fish)
    self.nets = []

  def run(self,dt):
    self.collision_manager.clear()
    for fish in self.fishs:
      self.collision_mananger.add(fish)
    for net in self.nets:
      self.collision_manager.add(net)
    result = self.collision_manager.iter_all_collisions()
    for one,two in result:
      if type(one) == type(two):
        continue
      one.explode()
      two.explode()
      #self.score_board.score = 100

def main():
  director.init(width=WIN_WIDTH,height=WIN_HEIGHT)
  game_layer = layer.Layer()
  game_scene = scene.Scene(BackgroundLayer())
  director.run(game_scene)

if __name__ == '__main__':
  main()
