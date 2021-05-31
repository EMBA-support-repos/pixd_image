from PIL import Image, ImageDraw
import sys
import getopt
import re


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o:p:", ["ifile=", "ofile=", "psize="])
    except getopt.GetoptError:
        print("pixd_png.py -i <inputfile> -o <outputfile> -p <pixelsize>")
        sys.exit(2)

    input_file = ""
    output_file = "./output.png"
    pixel_size = 10
    im = Image
    im_draw = ImageDraw

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("pixd_png.py -i <inputfile> -o <outputfile> -p <pixelsize>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-p", "--psize"):
            pixel_size = (arg)

    print(input_file)

    try:
        line_count = 0
        with open(input_file) as f:
            for i, l in enumerate(f):
                pass
            line_count = i + 1

        with open(input_file) as fp:
            lines = fp.readlines()
            for i, line in enumerate(lines):
                line_arr = re.split('\033\[|m\0{9600}|m', line)
                line_one_arr = []
                line_two_arr = []
                for elem in line_arr:
                    if ";" in elem:
                        color_arr = re.split(';', elem)
                        if color_arr[0] == "38":
                            line_one_arr.append((int(color_arr[2]), int(color_arr[3]), int(color_arr[4])))
                        elif color_arr[0] == "48":
                            line_two_arr.append((int(color_arr[2]), int(color_arr[3]), int(color_arr[4])))
                if i == 0:
                    mode = 'RGB'
                    print(i, len(line_one_arr) * int(pixel_size), int(pixel_size) * line_count * 2)
                    size = (int(pixel_size) * len(line_one_arr), int(pixel_size) * line_count * 2)
                    color = (33, 33, 33)

                    im = Image.new(mode, size, color)
                    im_draw = ImageDraw.Draw(im)

                pos_y = int(pixel_size) * (i * 2)
                for j, elem in enumerate(line_one_arr):
                    pos_x = int(pixel_size) * j
                    im_draw.rectangle((pos_x, pos_y, pos_x+int(pixel_size), pos_y+int(pixel_size)), fill=elem)
                pos_y = int(pixel_size) * ((i * 2) + 1)
                for k, elem in enumerate(line_two_arr):
                    pos_x = int(pixel_size) * k
                    im_draw.rectangle((pos_x, pos_y, pos_x+int(pixel_size), pos_y+int(pixel_size)), fill=elem)

        im.save(output_file, quality=95)

    except IOError:
        print("Input file not accessible")


if __name__ == "__main__":
    main(sys.argv[1:])
