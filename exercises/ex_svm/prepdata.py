import numpy as np
import pickle
from PIL import Image
import glob

images = []
labels = []

for filename in glob.glob('img50x50/1-stop/*.png'):
    im=Image.open(filename)
    imnp = np.array(im)
    images.append(imnp)
    labels.append(1)

for filename in glob.glob('img50x50/2-warn/*.png'):
    im=Image.open(filename)
    imnp = np.array(im)
    images.append(imnp)
    labels.append(2)

for filename in glob.glob('img50x50/0-nosign/*.png'):
    im=Image.open(filename)
    imnp = np.array(im)
    images.append(imnp)
    labels.append(0)

alldata = {
    "images" : images,
    "labels" : labels
}

with open('data.p', 'wb') as handle:
    pickle.dump(alldata, handle, protocol=2)

print 'saved ' + str(len(alldata['images'])) + ' in data.p'
