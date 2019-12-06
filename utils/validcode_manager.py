# coding:utf-8
import base64
from io import BytesIO
import random

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from utils.cache_manager import CacheManager
from utils.constants import Constants


class ValidCodeManager(object):
    def __init__(self, width, height, font_size=36, point_count=50, line_count=5, img_format='PNG'):
        self.cache_manager = CacheManager()
        self.operators = [Constants.multiplication, Constants.addition, Constants.subtraction]
        self.equal_mark = 61
        self.question_mark = 63
        self.width = width
        self.height = height
        self.font_size = font_size
        self.point_count = point_count
        self.line_count = line_count
        self.img_format = img_format
        self.calculation_results = ''
        self.charArray = None

    def getCodeImg(self, uuid):
        """
        获取随即图形验证码
        :return:
        """
        codeValue = self.cache_manager.get(uuid)
        return codeValue

    def getRandomColor(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def getRandomStr(self):
        random_num1 = random.randint(0, 9)
        random_num2 = random.randint(0, 9)
        random_operater = random.choice(self.operators)
        strs = (str(random_num1), chr(random_operater), str(random_num2), chr(self.equal_mark), chr(self.question_mark))
        self.charArray = (random_num1, random_operater, random_num2, self.equal_mark, self.question_mark)
        return strs

    def drawPoint(self, draw):
        for i in range(self.point_count):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            draw.point((x, y), fill=self.getRandomColor())

    def drawLine(self, draw):
        for i in range(self.line_count):
            x1 = random.randint(0, self.width)
            x2 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            y2 = random.randint(0, self.height)
            draw.line((x1, y1, x2, y2), fill=self.getRandomColor())

    def generateCodeImg(self):
        """
        生成图形验证码
        :return:
        """
        bg_color = self.getRandomColor()
        # 创建一张随机背景色的图片 white color

        img = Image.new(mode="RGB", size=(self.width, self.height), color=(255, 255, 255))
        # 获取图片画笔，用于描绘字
        draw = ImageDraw.Draw(img)
        # 修改字体
        font = ImageFont.truetype(font="arial.ttf", size=36)
        # 获取随机字符数组
        chars = self.getRandomStr()

        for i in range(5):
            txt_color = self.getRandomColor()
            # 避免文字颜色和背景色一致重合
            while txt_color == bg_color:
                txt_color = self.getRandomColor()
            # 根据坐标填充文字
            draw.text((10 + 30 * i, 3), text=chars[i], fill=txt_color, font=font)
        # 画干扰线点
        self.drawLine(draw)
        self.drawPoint(draw)
        output_buffer = BytesIO()
        img.save(output_buffer, format=self.img_format)
        byte_data = output_buffer.getvalue()
        base64_str = base64.b64encode(byte_data).decode()
        return base64_str

    def getCodeResult(self):
        """
        获取验证码值
        :return:
        """
        if self.charArray is None:
            self.getRandomStr()
        operater = self.charArray[1]
        num1 = int(self.charArray[0])
        num2 = int(self.charArray[2])
        if operater == Constants.addition:
            result = str(num1 + num2)
        elif operater == Constants.subtraction:
            result = str(num1 - num2)
        else:
            result = str(num1 * num2)
        return result

    def saveCodeImg(self):
        """
        使用redis 缓存图形验证码
        :return:
        """
        pass

    def deleteCodeImg(self):
        """
        删除图形验证码
        :return:
        """
        pass


class ImageResult(object):
    def __init__(self, img, uuid):
        self.img = img
        self.uuid = uuid
