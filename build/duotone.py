from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import numpy as np, sys
def ramp(stops):
    # stops: list of (pos 0..1, (r,g,b))
    lut=np.zeros((256,3))
    for i in range(256):
        t=i/255
        for (p0,c0),(p1,c1) in zip(stops,stops[1:]):
            if p0<=t<=p1:
                f=(t-p0)/(p1-p0) if p1>p0 else 0
                lut[i]=[c0[k]+(c1[k]-c0[k])*f for k in range(3)]
                break
    return lut.astype(np.uint8)
def hexc(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
NAVY=ramp([(0,hexc('#020a17')),(0.35,hexc('#0a2447')),(0.7,hexc('#8d97a6')),(1,hexc('#f4efe4'))])
def duo(src, out, lut=NAVY, contrast=1.15, gamma=1.0, crop=None, width=1600):
    im=Image.open(src).convert('L')
    if crop: 
        w,h=im.size; im=im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
    im=ImageOps.autocontrast(im, cutoff=0.5)
    im=ImageEnhance.Contrast(im).enhance(contrast)
    if gamma!=1.0:
        arr=np.asarray(im)/255.0; im=Image.fromarray((np.power(arr,gamma)*255).astype(np.uint8))
    if im.width>width: im=im.resize((width,int(im.height*width/im.width)), Image.LANCZOS)
    arr=np.asarray(im); rgb=lut[arr]
    o=Image.fromarray(rgb,'RGB')
    o.save(out+'.jpg', quality=82, optimize=True, progressive=True)
    o.save(out+'.webp', quality=78, method=6)
    return o.size
if __name__=='__main__':
    print(duo(sys.argv[1], sys.argv[2]))
