# 1\ METHODE
# pip install rembg
# pip install pillow

from rembg import remove
from PIL import Image

og_img = "Generated.jpg"
remove_bg = "Generated.png"

try:
    inp = Image.open(og_img)
    out = remove(inp)
    out.save(f"Succes {remove_bg}")

except FileNotFoundError:
    print("Error: file not found! pls check it.")

# 2\ source --> clcoding.com
import cv2, numpy as np #install pip install opencv-python numpy

img = cv2.imread("Generated.jpg")
mask = np.zeros(img.shape[:2], np.uint8)

bg, fg = np.zeros((1,65)), np.zeros((1,65))
rect =(10, 10, img.shape[1]-20, img.shape[0]-20)

cv2.grabCut(img, mask, rect, bg, fg, 5, cv2.GC_INIT_WITH_RECT)
mask = np.where((mask == 0)|(mask == 2), 0,1).astype("uint8")

cv2.imwrite("output.png", img * mask[:, :, None])

# 3\ METHODE REMOVE
# from rembg import remove
# from PIL import Image
# import os

# img = "Generated.jpg"
# png = "Generated.png"

# def removeBG():
#     if not os.path.exists(img):
#         print(f"Error > FIle '{img}' not found")
#         return
#     print("Loading . . . (Proccesing Program)")

#     try:
#         inp = Image.open(img)
#         out = remove(inp)
#         out.save(png)
#         print(f"Done! Saved in : {png}")
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     remove_background()