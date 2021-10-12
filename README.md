# imgtoascii

imgtoascii is a simple image to ASCII converter written in Python

## Usage
```
usage: imgtoascii.py [-h] [--width WIDTH] [--height HEIGHT] [--charset CHARSET] image

Image to ASCII converter

positional arguments:
  image              Image input path

optional arguments:
  -h, --help         show this help message and exit
  --width WIDTH      Output width (default: 128)
  --height HEIGHT    Output height (default: 128)
  --charset CHARSET  Charset for ASCII image generator. (default: "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`)
```

## Requirements
* Pillow==8.3.2
* numpy==1.21.2
