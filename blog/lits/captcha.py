from PIL import Image,ImageDraw,ImageFont
import random


def generate_code():
    '''
    随机生成4个字母
    '''
    code_len = 4
    code_str = ''
    for i in range(code_len):
        # char = chr(random.randint(65,90))
        char = chr(random.randint(48, 71))
        code_str+=char
    return code_str



def generate_captcha():
    img_width=120
    img_height=40

    #定义一张空白的img，并获取画笔对象
    img = Image.new('RGB',(img_width,img_height),(255,255,255))
    draw = ImageDraw.Draw(img)

    #定义验证码的字体和大小
    font_path = 'C:/Users/11324/Desktop/blog/blog/lits/simhei.ttf'
    font_size = 30
    font = ImageFont.truetype(font_path,font_size)

    #在图片上面绘制随机字符串
    code_str = generate_code()
    code_width,code_height = font.getsize(code_str)
    x = (img_width-code_width)/2
    y = (img_height-code_height)/2
    draw.text((x,y),code_str,fill=(0,0,0),font=font)

    # 添加干扰点和线条
    for i in range(20):
        x1 = random.randint(0, img_width)
        y1 = random.randint(0, img_height)
        x2 = random.randint(0, img_width)
        y2 = random.randint(0, img_height)
        draw.line((x1, y1, x2, y2), fill=(255, 0, 0), width=2)
        draw.point((x1, y1), fill=(0, 0, 255))

    # 模糊图片

    return img


captcha_img = generate_captcha()
captcha_img.show()