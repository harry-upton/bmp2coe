# bmp2coe

Used to convert bitmap image files to coe files for use with an FPGA. This script can convert individual images or spritesheets, and currently only supports palletised images (both 16 and 256 colour). 2 files will be outputted, one for the palette and one for the image data.

For spritesheets, the sprites will be stored sequentially in memory, from left to right and top to bottom in the spritesheet. Pixels in the sprites are stored left to right, top to bottom.

## Usage

Run `python bmp2coe.py --help` for info on how to run the script.

## Resources

- https://docs.python.org/3/library/struct.html
- https://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm
- https://stackoverflow.com/questions/47003833/how-to-read-bmp-file-header-in-python
