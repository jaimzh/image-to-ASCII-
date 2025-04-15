from ascii_magic import AsciiArt

my_art = AsciiArt.from_image('Among us color.jpg')

my_art.to_file(monochrome=True, path='ascii_output.txt')

