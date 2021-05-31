**pixd** is a tool for visualizing binary data using a colour palette.  It is
in a lot of ways akin to a hexdump tool, except using coloured squares to
represent each octet.

*pixd* uses 24-bit color SGR escape sequences.  For a list of terminal
emulators with support for these, see [XVilka's list of supporting terminal
emulators][1].

#### pixd_image

Only a small script has been added to this fork, which makes it easy to render the output of pixd as an image. In order to be able to use the script, the requirement [`Pillow`](https://pypi.org/project/Pillow/) must be installed via` pip3`. 

*Example usage:*
```
./pixde -r-0x2000 ./binary | tee -a ./pixd.txt
python3 ./pixd_png.py -i ./pixd.txt -o ./pixd.png -p 20
```

Keep in mind to keep the pixd output small - to create a picture of a big firmware, this script has to be vastly improved.

## Screenshot
![Screenshot](meta/examples.png "Example output for 8 different filetypes")

## License
MIT license.  Enjoy!

## See also
* [hexd](http://github.com/FireyFly/hexd):
  more conventional hexdump tool with colourful output, and also what *pixd*'s
  code is based on.

[1]: https://gist.github.com/XVilka/8346728
