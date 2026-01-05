# pip install rembg
# pip install pillow

from rembg import remove
from PIL import Image

og_img = ""
remove_bg = ""

inp = Image.open(og_img)
out = remove(inp)
out.save(remove_bg)