import picture

def copy(image):

  width = picture.image_width(image)
  height = picture.image_height(image)
  
  imagecopy = picture.blank_image(width,height)

  for y in range(height):
    for x in range(width):
      (red,green,blue) = picture.get_pixel(image, x, y)
      picture.set_pixel(imagecopy, x, y,(red,green,blue))

  return imagecopy
  
def vertflip(image, width, height):
  
  imagecopy = copy(image)

  for y in range(height):
    for x in range(width):
      (red,green,blue) = picture.get_pixel(imagecopy, x, y)
      picture.set_pixel(image, x, height - y -1,(red,green,blue))

'''
def main():
  """
  This is the first function to be called when warmupgram.py is executed. We'll use this function to complete some basic tasks and call our two image filter functions: grayscale() and vertflip().
  """
  
  # Let's begin by loading a JPEG image into memory using the picture module. This will only load the image, we will display it later using a separate function.
  image = picture.load_image("crayons.jpg")

  width = int(picture.image_width(image))
  height = int(picture.image_height(image))
  
  vertflip(image, width, height)
  
  
  picture.new_picture(width, height)
  picture.draw_image(0, 0, image)
  picture.run()


# The following line tells Python to execute the main() function when the file is called from the command line.
if __name__ == "__main__":
  main()

'''