import picture 

def greyscale(image, width, height):
  """
  This function accepts an RGB image and its dimensions as input and returns a grayscale version of the image.
  """
  
  for y in range(height):
    for x in range(width):
      red = picture.get_red(image, x, y)
      green = picture.get_green(image, x, y)
      blue = picture.get_blue(image, x, y)
      grey = (red + green + blue)//3
      picture.set_pixel(image,x,y,(grey,grey,grey))
  return image 
  
'''
def main():
  """
  This is the first function to be called when warmupgram.py is executed. We'll use this function to complete some basic tasks and call our two image filter functions: grayscale() and vertflip().
  """
  
  # Let's begin by loading a JPEG image into memory using the picture module. This will only load the image, we will display it later using a separate function.
  image = picture.load_image("crayons.jpg")

  width = int(picture.image_width(image))
  height = int(picture.image_height(image))

  grayscale(image, width, height)
  
  
  picture.new_picture(width, height)
  picture.draw_image(0, 0, image)
  picture.run()


# The following line tells Python to execute the main() function when the file is called from the command line.
if __name__ == "__main__":
  main()

'''