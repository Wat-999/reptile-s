from chaojiying import Chaojiying_Client


def cjy():  # 使用超级鹰识别
    chaojiying = Chaojiying_Client('hjl990505', 'hjl5406558', '934599')  # 账号、密码、项目号（这个不用改）
    im = open('a.png', 'rb').read()  # 本地图片文件路径，需要为a.png名字
    code = chaojiying.PostPic(im, 1902)['pic_str']  # 4-6位英文数字用1902
    return code


result = cjy()  # 调用函数，识别代码所在文件夹中的a.png文件，并将返回的结果赋值给result变量
print(result)  # 打印识别的结果
