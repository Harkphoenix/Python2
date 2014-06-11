from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
(2013 ,12        ,76.4    ,77.4    ,75.4),
(2014 ,1        ,78.6    ,80.6    ,76.6),
(2014 ,2        ,80.1    ,83.1    ,77.1),
(2014 ,3        ,82.4    ,87.4    ,77.4),
(2014 ,4        ,83.7    ,88.7    ,78.7),
(2014 ,5        ,83.1    ,89.1    ,77.1),
(2014 ,6        ,82.3    ,89.3    ,75.3)
]

drawing = Drawing(200,300)
pred = [row[2]-40 for row in data]
high = [row[3]-40 for row in data]
low  = [row[4]-40 for row in data]
times = [200 * ((row[0] + row[1]/12.0) - 2013) - 110 for row in data]

drawing.add(PolyLine(zip(times, pred), strokeColor = colors.blue))
drawing.add(PolyLine(zip(times, high), strokeColor = colors.red))
drawing.add(PolyLine(zip(times, low), strokeColor = colors.green))

drawing.add(String(65,115,'Sunports', fontsize = 18, fillColor = colors.red))

renderPDF.drawToFile(drawing, "report3.pdf", 'Sunports')
