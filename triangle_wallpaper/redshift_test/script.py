from PIL import Image

def convert(point):
    r = point[0]
    g = point[1]
    b = point[2]
    return tuple((r, 35, 61))

im = Image.open("source.png")
data = list(im.getdata())

# print(data)

newData = []

for point in data:
    n = convert(point)
    # print(point, n)
    newData.append(n)


newIm = Image.new("RGB", im.size)
newIm.putdata(newData)
# newIm.show()
newIm.save("OUTPUT.png")