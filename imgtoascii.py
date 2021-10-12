import sys
import numpy
import numpy as np
from PIL import Image
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

def main():
    parser = ArgumentParser(description="Image to ASCII converter", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('image', type=str, help="Image input path")
    parser.add_argument('--width', action='store', type=int, default=128, help='Output width')
    parser.add_argument('--height', action='store', type=int, default=128, help='Output height')
    parser.add_argument('--charset', action='store', type=str,
                        default='$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'.',
                        help='Charset for ASCII image generator.')
    args = parser.parse_args()

    image: Image.Image = Image.open(args.image)
    image = image.resize((args.width, args.height), )

    matrix = numpy.array(image)

    if len(matrix.shape) == 3:
        matrix = np.mean(matrix, axis=2)

    matrix -= np.min(matrix)
    matrix = matrix / float(np.max(matrix))
    matrix *= len(args.charset) - 1
    matrix = np.rint(matrix)
    for y in range(matrix.shape[0]):
        for x in range(matrix.shape[1]):
            sys.stdout.write(args.charset[int(matrix[y][x])])
        sys.stdout.write('\n')


if __name__ == '__main__':
    main()
