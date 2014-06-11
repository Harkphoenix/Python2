import urllib
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF


url = "http://www.swpc.noaa.gov/ftpdir/weekly/Predict.txt"
COMMENT_CHARS = '#:'

drawing = Drawing(600,400)
data = []
html = urllib.urlopen(url).readlines()

for line in html:
	if not line.isspace() and not line[0] in COMMENT_CHARS:
		data.append([float(n) for n in line.split()])

pred = [row[2] for row in data]
high = [row[3] for row in data]
low  = [row[4] for row in data]
times = [(row[0] + row[1]/12.0) for row in data]

lp = LinePlot()
lp.x = 100
lp.y = 100
lp.height = 125
lp.width = 300
lp.data = [zip(times, pred), zip(times, high), zip(times, low)]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(350,250,'Subspots', fontsize = 14, fileColor = colors.red))
renderPDF.drawToFile(drawing, "report7.pdf", 'Sunports')