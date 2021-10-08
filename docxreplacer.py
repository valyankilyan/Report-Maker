from docx import Document
from config import replace_dictionary

document = Document("title_template.docx")

for p in document.paragraphs:
    if p.text != '':
        for c in replace_dictionary:
            if p.text.find(c) >= 0:
                for i in range(len(p.runs)):
                    if c in p.runs[i].text:
                        p.runs[i].text = p.runs[i].text.replace(
                            c, replace_dictionary[c])

document.save("title.docx")
