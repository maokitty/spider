from PIL import Image,ImageFilter
touxiang = Image.open("../touxiang112.jpeg")
blurryTouxiang = touxiang.filter(ImageFilter.GaussianBlur)
blurryTouxiang.save("touxiang_blured.jpeg")
blurryTouxiang.show()