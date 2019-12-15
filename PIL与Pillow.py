



from PIL import Image,ImageFilter


img = Image.open("img/erweima.jpg")
# img.show()    # 查看图片
print(img.size)   # 图片尺寸
print(img.format)   # 图像（文件格式）
w,h = img.size
# 缩放操作
img.thumbnail((w//2,h//2))
# 保存缩放的图像
img.save('img/thumbnail.jpg','JPEG')

# 旋转90°
img.transpose(Image.ROTATE_90).save('img/rotate_90.jpg','JPEG')
# 左右翻转
img.transpose(Image.FLIP_LEFT_RIGHT).save('img/left_right.jpg','JPEG')
# 上下翻转
img.transpose(Image.FLIP_TOP_BOTTOM).save('img/top_bottom.jpg','JPEG')
# 不同的滤镜
img.filter(ImageFilter.DETAIL).save('img/detail.jpg')


# 裁剪图像
img.crop((0,0,w//2,h//2)).save('img/crop.jpg')  # 根据指定的参数指定区域裁剪图像

# 创建新图片
img2 = Image.new('RGBA',(500,500),(255,255,0))
img2.save('img/new.png','PNG')  # 创建一个500*500纯色图片
img2.paste(img,(10,10))   # img粘贴至指定位置
img2.save('img/combine.png')