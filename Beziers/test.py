from PIL import Image
from main import linearBezier
from main import quadraticBezier
from main import cubicBezier
import numpy as np

testImage = Image.new('RGB', (500, 500), (0,0,0))
curveColor = (66, 135, 245)

for t in np.arange(start=0, stop=1, step=(1/10000)):
    testImage.putpixel(cubicBezier((15, 56), (430, 56), (1, 1), (420, 420), t), curveColor)

testImage.show()