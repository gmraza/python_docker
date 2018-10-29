import pgmagick as pg
from os import listdir
from os.path import isfile, join
mypath = './input'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(files)
def trans_mask_sobel(img, color="magenta"):
    """ Generate a transparency mask for a given image """
    image = pg.Image(img)
    # Find object
    image.negate()
    image.edge()
    image.blur(1)
    image.threshold(24)
    image.adaptiveThreshold(5, 5, 5)
    # Fill background
    image.fillColor(color)
    w, h = image.size().width(), image.size().height()
    image.floodFillColor('0x0', color)
    image.floodFillColor('0x0+%s+0' % (w-1), color)
    image.floodFillColor('0x0+0+%s' % (h-1), color)
    image.floodFillColor('0x0+%s+%s' % (w-1, h-1), color)
    image.transparent(color)
    return image
def alpha_composite(image, mask):
    """ Composite two images together by overriding one opacity channel """
    compos = pg.Image(mask)
    compos.composite(
        image,
        image.size(),
        pg.CompositeOperator.CopyOpacityCompositeOp
    )
    return compos
def remove_background(filename):
    """ Remove the background of the image in 'filename' """
    img = pg.Image('input/' + filename)
    transmask = trans_mask_sobel(img)
    img = alpha_composite(transmask, img)
    img.trim()
    img.write('out-'+ filename +'.png')
for file_name in files:
    remove_background(file_name)