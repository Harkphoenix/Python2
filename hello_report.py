# coding=utf-8
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100,100)    #创建100*100大小的图纸
s = String(50,50,"hello world", textAnchor = "middle")   #在整个图纸的什么位置，如何显示文本
d.add(s)                                             #把文本放置在图纸上
renderPDF.drawToFile(d, 'hello.pdf', 'a simple pdf file')         #在本地目录下输出一个pdf文件