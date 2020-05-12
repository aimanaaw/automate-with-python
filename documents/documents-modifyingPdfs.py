import PyPDF2, os

# Can't extract images or media from pdfs. It can extract text

pdfFile = open('meetingminutes1.pdf', 'rb')
# Opened in read binary since pdfs are binary
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader)

print(reader.numPages)
# print(reader.getPage(0))

page = reader.getPage(0)
# print(page.extractText())

# for pageNum in range(reader.numPages):
# 	print(reader.getPage(pageNum).extractText())

pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writerObject = PyPDF2.PdfFileWriter() #blank pdf in computer memory

for pageNum in range(reader1.numPages):
	page = reader1.getPage(pageNum)
	writerObject.addPage(page)

for pageNum in range(reader2.numPages):
	page = reader2.getPage(pageNum)
	writerObject.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')
writerObject.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()