import imageio.v3 as iio

filenames = ['nyan-cat1.png', 'nyan-cat2.png','nyan-cat3.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('animal.gif', images, duration = 500, loop = 0)