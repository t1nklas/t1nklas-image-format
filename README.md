# t1nklas image converter and viewer

this project consists of two python scripts for handling a custom image format called `.t1nklas`.

## files

- `convert.py`: converts common image formats (png, jpg, jpeg, bmp, gif) to `.t1nklas`. uses tkinter for file dialogs and pillow for image processing.
- `viewer.py`: loads and displays `.t1nklas` images using pygame. supports window resizing and centers the image.

## usage

1. run `convert.py` to convert an image to `.t1nklas`.
2. run `viewer.py` to view a `.t1nklas` image.

## requirements

- python 3.x
- pillow (`pip install pillow`)
- pygame (`pip install pygame`)

## notes

- `.t1nklas` is a simple custom format storing rgba pixel data.
- the viewer scales images to fit the window while maintaining aspect ratio.
