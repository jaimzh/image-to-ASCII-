import PIL.Image

def main():
    # laod image  
    try:
        image = PIL.Image.open('Among us color.jpg')
    except:
        print( "Unable to find image ")
        
    #resize image
    def resize_image(image, new_width):
        width, height = image.size
        aspect_ratio = height / width
        new_height = int(new_width * aspect_ratio * 0.45)
        return image.resize((new_width, new_height))
        
    #next up we greyscale resized image
    def greyscalify_image(image):
        return image.convert("L")
    
    # now the hard part we map the image pixels to ascii characters
    def image_to_ascii(image):
        # ascii_chars = "@%#*+=-:. "
        ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]       
        pixels = image.getdata()
        ascii_str = ''
        for i, pixel in enumerate (pixels):
            ascii_str += ASCII_CHARS[pixel // 25]   
            if (i + 1) % image.width == 0:
                ascii_str += '\n'
            
        return ascii_str
        
    
    ascii_image=image_to_ascii(greyscalify_image(resize_image(image, 100)))
    
    print(ascii_image)
    
    #saving in a txt
    with open("ascii_text_created2.txt", "w") as file:
        file.write(ascii_image)
        
        
  
  
        
if __name__ == "__main__":
    main()