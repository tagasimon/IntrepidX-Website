"""Colour treatment for the site photographs.

Keeps the photo's own colour but pulls it toward the brand navy, so pictures
from different photographers sit together. Output: <out>.jpg and <out>.webp.
"""
from PIL import Image, ImageEnhance, ImageOps
import numpy as np, sys

def _ramp(stops):
    lut = np.zeros((256, 3))
    for i in range(256):
        t = i / 255
        for (p0, c0), (p1, c1) in zip(stops, stops[1:]):
            if p0 <= t <= p1:
                f = (t - p0) / (p1 - p0) if p1 > p0 else 0
                lut[i] = [c0[k] + (c1[k] - c0[k]) * f for k in range(3)]
                break
    return lut.astype(np.uint8)

def _hex(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

NAVY = _ramp([(0, _hex('#020a17')), (0.4, _hex('#0b2a52')), (0.75, _hex('#8fa0b8')), (1, _hex('#f6f3ec'))])

def treat(src, out, tint=0.38, sat=0.62, contrast=1.06, bright=0.96, crop=None, width=1800):
    im = Image.open(src).convert('RGB')
    if crop:
        w, h = im.size
        im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    col = ImageEnhance.Color(im).enhance(sat)
    col = ImageEnhance.Contrast(col).enhance(contrast)
    col = ImageEnhance.Brightness(col).enhance(bright)
    g = ImageOps.autocontrast(im.convert('L'), cutoff=0.5)
    duo = Image.fromarray(NAVY[np.asarray(g)], 'RGB')
    o = Image.blend(col, duo, tint)
    o.save(out + '.jpg', quality=82, optimize=True, progressive=True)
    o.save(out + '.webp', quality=78, method=6)
    return o.size

if __name__ == '__main__':
    print(treat(sys.argv[1], sys.argv[2]))
