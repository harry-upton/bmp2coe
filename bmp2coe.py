import struct
import argparse
import math

def main (args):
    bmp = open(args.filename, 'rb')
    # Read the first 14 bytes - header
    file_type = bmp.read(2).decode()
    file_size = struct.unpack('I', bmp.read(4))
    bmp.read(4) # Read 4 reserved bytes
    offset = struct.unpack('I', bmp.read(4))

    # Read the next 40 bytes - info header
    dib_header_size = struct.unpack('I', bmp.read(4))[0]
    image_width = struct.unpack('I', bmp.read(4))[0]
    image_height = struct.unpack('I', bmp.read(4))[0]
    colour_planes = struct.unpack('H', bmp.read(2))[0]
    bits_per_pixel = struct.unpack('H', bmp.read(2))[0]
    compression = struct.unpack('I', bmp.read(4))[0]
    image_size = struct.unpack('I', bmp.read(4))[0]
    h_resolution = struct.unpack('I', bmp.read(4))[0]
    v_resolution = struct.unpack('I', bmp.read(4))[0]
    actual_colours = struct.unpack('I', bmp.read(4))[0]
    important_colours = struct.unpack('I', bmp.read(4))[0]

    print('Type:', file_type)
    print('Size: %s' % file_size)
    print('Offset: %s' % offset)
    print('DIB Header Size: %s' % dib_header_size)
    print('Width: %s' % image_width)
    print('Height: %s' % image_height)
    print('Colour Planes: %s' % colour_planes)
    print('Bits per Pixel: %s' % bits_per_pixel)
    print('Compression Method: %s' % compression)
    print('Raw Image Size: %s' % image_size)
    print('Horizontal Resolution: %s' % h_resolution)
    print('Vertical Resolution: %s' % v_resolution)
    print('Actual Number of Colours: %s' % actual_colours)
    print('Important Colours: %s' % important_colours)

    if file_type != 'BM':
        print('Filetype must be bitmap (.bmp)')
        return
    if compression != 0:
        print('File must be uncompressed (compression = 0)')
        return
    if bits_per_pixel != 4 and bits_per_pixel != 8:
        print('Bitmap image must be palletised (bits per pixel = 4 or 8)')
        return
    
    num_colours = 0
    if bits_per_pixel == 8:
        num_colours = 256
    else:
        num_colours = 16

    # Read the next num_colours bytes - color table
    for i in range(num_colours): # 0-15 or 0-255
        blue = struct.unpack('B', bmp.read(1))[0] # BGR ?
        green = struct.unpack('B', bmp.read(1))[0]
        red = struct.unpack('B', bmp.read(1))[0]
        unused = struct.unpack('B', bmp.read(1))[0]
        print("Color %d: %d %d %d %d" % (i, red, green, blue, unused))

    # Read image data
    sprite_size = 34 # 16x16 sprites, 34 FOR TESTING THIS SPRITE
    sprites_x = math.floor(image_width / sprite_size)
    sprites_y = math.floor(image_height / sprite_size)

    image_bytes = []
    if bits_per_pixel == 8:
        for i in range((sprites_x*sprite_size)*(sprites_y*sprite_size)):
            pixel = struct.unpack('B', bmp.read(1))[0]
            image_bytes.append(pixel)

    else:
        for i in range(int((sprites_x*sprite_size)*(sprites_y*sprite_size)/2)):
            two_pixels = struct.unpack('B', bmp.read(1))[0]
            high, low = two_pixels >> 4, two_pixels & 0x0F
            image_bytes.append(high)
            image_bytes.append(low)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args)