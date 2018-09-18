from PIL import Image

def cutPng(src,out,x,y,width,height):
  image_src = Image.open(src)
  box = (x,y,width,height)
  image_out = image_src.crop(box)
  image_out.save(out,'PNG')

if __name__ == '__main__':
  #cutPng('images/fish1.png','images/fish_single.png',0,0,55,296/8)

  cutPng('images/cannon7.png','images/cannon7_single.png',0,0,74,470/5)
