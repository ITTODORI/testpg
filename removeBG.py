# pip install rembg
# pip install pillow

from rembg import remove
from PIL import Image

og_img = ""
remove_bg = ""

inp = Image.open(og_img)
out = remove(inp)
out.save(remove_bg)

# source --> clcoding.com
import cv2, numpy as np

img = cv2.imread("image.jpg")
mask = np.zeros(img.shape[:2], np.uint8)

bg, fg = np.zeros((1,65)), np.zeros((1,65))
rect =(10, 10, img.shape[1]-20, img.shape[0]-20)

cv2.grabCut(img, mask, rect, bg, fg, 5, cv2.GC_INIT_WITH_RECT)
mask = np.where((mask == 0)|(mask == 2), 0,1).astype("uint8")

cv2.imwrite("output.png", img * mask[:, :, None])