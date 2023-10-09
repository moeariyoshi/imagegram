def zoom(image, width, height):
  imagecopy = copy(image)
  
  for y in range(height//2):
    for x in range(width//2):
      (red,green,blue) = picture.get_pixel(imagecopy, width//4+x, height//4+y)
      for Y in range(height//2):
        for i in range(2):
          for X in range(width//2):
            for j in range(2):
              picture.set_pixel(image, X+j, Y+i,(red,green,blue))
  return image 


def zoom(image, width, height):
  imagecopy = copy(image)
  for y in range(height//4, 3*height//4):
    for x in range(width//4, 3*width//4):
      red,green,blue = picture.get_pixel(imagecopy, x, y)
      for Y in range(height//2):
        for X in range(width//2):
          picture.set_pixel(image, 2*X, 2*Y, (red,green,blue))
          picture.set_pixel(image, 2*X+1, 2*Y,(red,green,blue))
          picture.set_pixel(image, 2*X, 2*Y+1, (red,green,blue))
          picture.set_pixel(image, 2*X+1, 2*Y+1, (red,green,blue))
    
