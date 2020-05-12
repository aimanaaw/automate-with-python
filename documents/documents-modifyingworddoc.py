import docx

documentObject = docx.Document('demo.docx')
print(documentObject)
print(documentObject.paragraphs[0].text)

p = documentObject.paragraphs[1]
print(p.runs)
# Each change in text is a run
# A plain paragraph having some bold and some italic. => 4 runs in this object
print(p.runs[0].text)
# p.runs[1].bold = True

p.runs[3].underline = True
p.runs[3].text = 'italic and underlined'
documentObject.save('demo2.docx')