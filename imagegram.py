# imagegram.py

import picture

def negative(image, width, height):
  for y in range(height):
    for x in range(width):
      red = picture.get_red(image, x, y)
      green = picture.get_green(image, x, y)
      blue = picture.get_blue(image, x, y)
      picture.set_pixel(image,x,y,(255-red,255-green,255-blue))
  return image 

def greyscale(image, width, height):
  for y in range(height):
    for x in range(width):
      red = picture.get_red(image, x, y)
      green = picture.get_green(image, x, y)
      blue = picture.get_blue(image, x, y)
      grey = (red + green + blue)//3
      picture.set_pixel(image,x,y,(grey,grey,grey))
  return image 
  
def copy(image):
  width = picture.image_width(image)
  height = picture.image_height(image)
  imagecopy = picture.blank_image(width, height)
  for y in range(height):
    for x in range(width):
      (red,green,blue) = picture.get_pixel(image, x, y)
      picture.set_pixel(imagecopy, x, y,(red,green,blue))

  return imagecopy

def flip(image, width, height):
  
  imagecopy = copy(image)

  for y in range(height):
    for x in range(width):
      (red,green,blue) = picture.get_pixel(imagecopy, x, y)
      picture.set_pixel(image, x, height -y-1,(red,green,blue))
  return image

def scroll(image, width, height):
  imagecopy = copy(image)
  scroll = int(input("How much would you like to scroll? "))
  for y in range(height):
    for x in range(width):
      (red,green,blue) = picture.get_pixel(imagecopy, x, y)
      picture.set_pixel(image, (x + scroll) % width, y,(red,green,blue))
  return image    

def zoom(image, width, height):
  imagecopy = copy(image)
  for y in range(height):
    for x in range(width):
      X = width//4 + x//2
      Y = height//4 + y//2
      red,green,blue = picture.get_pixel(imagecopy, X, Y)
      picture.set_pixel(image, x, y, (red, green, blue))
  return image

def contrast(image, width, height):
  for y in range(height):
    for x in range(width):
      red,green,blue = picture.get_pixel(image, x, y)
      newRed = (128 + 2 * (red - 128))
      if newRed > 255:
        newRed = 255
      if newRed < 0:
        newRed = 0
      newGreen = (128 + 2 * (green - 128))
      if newGreen > 255:
        newGreen = 255
      if newGreen < 0:
        newGreen = 0
      newBlue = (128 + 2 * (blue - 128))
      if newBlue > 255:
        newBlue = 255
      if newBlue < 0:
        newBlue = 0
      picture.set_pixel(image,x,y,(newRed,newGreen,newBlue))
  return image 

def posterize(image, width, height):
  for y in range(height):
    for x in range(width):
      red,green,blue = picture.get_pixel(image, x, y)
      newRed = (red//64)*64
      newGreen = (green//64)*64
      newBlue = (blue//64)*64
      picture.set_pixel(image, x, y, (newRed, newGreen, newBlue))
  return image

def blur(image, width, height):
  for y in range(1, height-1):
    for x in range(1, width -1):
      r1,g1,b1 = picture.get_pixel(image, x-1, y-1) 
      r2,g2,b2 = picture.get_pixel(image, x, y-1)
      r3,g3,b3 = picture.get_pixel(image, x+1, y-1) 
      
      r4,g4,b4 = picture.get_pixel(image, x-1, y)
      r5,g5,b5 = picture.get_pixel(image, x, y)
      r6,g6,b6 = picture.get_pixel(image, x+1, y)

      r7,g7,b7 = picture.get_pixel(image, x-1, y+1)
      r8,g8,b8 = picture.get_pixel(image, x, y+1)
      r9,g9,b9 = picture.get_pixel(image, x+1, y+1)

      newRed = (r1+r2+r3+r4+r5+r6+r7+r8+r9)//9
      newGreen = (g1+g2+g3+g4+g5+g6+g7+g8+g9)//9
      newBlue = (b1+b2+b3+b4+b5+b6+b7+b8+b9)//9

      picture.set_pixel(image, x, y, (newRed, newGreen, newBlue))

  return image
  
def main():

  print()
  print("Welcome to Imagegram!")
  print()
  
  try:
  
    imagename = input("Please enter a file name: ")
    image = picture.load_image(imagename)
    width = int(picture.image_width(image))
    height = int(picture.image_height(image))
  
    done = False 

  except:
    print("File Not Found")
    
  while (not done):
      print()
      print("Which of the following filters would you like to apply?: ")
      print("1. Make Negative")
      print("2. Make Greyscale")
      print("3. Flip Vertically")
      print("4. Scroll Horizontally")
      print("5. Zoom")
      print("6. Contrast")
      print("7. Posterize")
      print("8. Blur")
      print("0. Quit")
      print()
      select = input("Choice: ")

      if select == "1":
        negative(image, width, height)
        picture.new_picture(width, height)
        picture.draw_image(0, 0, image)
        picture.display()

      if select == "2":
        greyscale(image, width, height)
        picture.new_picture(width, height)
        picture.draw_image(0, 0, image)
        picture.display()
  
      if select == "3":
        flip(image, width, height)
        picture.new_picture(width, height)
        picture.draw_image(0, 0, image)
        picture.display()
  
      if select == "4":
        scroll(image, width, height)
        picture.new_picture(width, height)
        picture.draw_image(0, 0, image)
        picture.display()
  
      if select == "5":
        zoom(image, width, height)
        picture.new_picture(width, height)
        picture.draw_image(0, 0, image)
        picture.display()
  
      if select == "6":
        contrast(image, width, height)
        picture.new_picture(width, height)
        picture.draw_image(0, 0, image)
        picture.display()
  
      if select == "7":
        posterize(image, width, height)
        picture.new_picture(width, height)
        picture.draw_image(0, 0, image)
        picture.display()
  
      if select == "8":
        blur(image, width, height)
        picture.new_picture(width, height)
        picture.draw_image(0, 0, image)
        picture.display()
  
      if select == "0":
        done = True
        print("Goodbye!")


try: 
  
  if __name__ == "__main__":
    main()

except: 
  print("Sorry!")