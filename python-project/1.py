import ddddocr
ocr = ddddocr.DdddOcr()
with open('imagescode0.jpg', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
print(type(res))