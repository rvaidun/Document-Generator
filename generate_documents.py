import requests
from bs4 import BeautifulSoup
import bs4
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt
import nltk
from nltk.tokenize import sent_tokenize
import paraphrase
import wikipedia
import sys
import os
import names
import random
def createDocument(text, title):
    classNames = ["HISTORY 100," "RELIGION 100", "HISTORY 101,", "HIST 100", "HISTORY 150", "REL 101", "RELIGION 100"]
    document = Document()
    # Name
    obj_styles = document.styles
    obj_charstyle = obj_styles.add_style('NameStyle', WD_STYLE_TYPE.CHARACTER)
    obj_font = obj_charstyle.font
    obj_font.size = Pt(12)
    obj_font.name = 'Times New Roman'
    name = document.add_paragraph()
    className = document.add_paragraph()
    name.add_run(names.get_full_name(), style='NameStyle')
    className.add_run(random.choice(classNames), style='NameStyle')
    # Heading
    obj_styles = document.styles
    obj_charstyle = obj_styles.add_style(
        'CommentsStyle', WD_STYLE_TYPE.CHARACTER)
    obj_font = obj_charstyle.font
    obj_font.size = Pt(16)
    obj_font.name = 'Times New Roman'
    paragraph = document.add_paragraph()
    paragraph.add_run(title, style='CommentsStyle').bold = True
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # Content
    paragraph = document.add_paragraph(text)

    document.save(f'./{sys.argv[1]}/{title.strip()}.docx')


if __name__ == "__main__":
    try:
        page = wikipedia.page(sys.argv[1], auto_suggest=False)
        print(f"The url for page is {page.url}")
    except wikipedia.exceptions.PageError:
        print(
            f" The page {sys.argv[1]} could not be found. Please try another page")
    page_content = page.content.split("== See also ==")[0]

    page_content = page_content.strip()
    page_content = sent_tokenize(page_content)
    chunked = []
    count = 0
    curstr = ""
    print(f"Paraphrasing Chunk {len(chunked)}")
    for x in page_content:
        if count == 25:
            count = 0
            chunked.append(curstr)
            print(f"Paraphrasing Chunk {len(chunked)}")
            curstr = ""
        curstr += paraphrase.paraphrase(x)
        count += 1
    chunked.append(curstr)
    count = 0
    try:
        os.mkdir(f"./{sys.argv[1]}")
    except OSError:
        print("Creation of the directory failed")
    else:
        print("Successfully created the directory")
    for x in chunked:
        print(f"Writing chunk {count} to word doc")
        title = " ".join(nltk.word_tokenize(x)[0:3])
        createDocument(x, title)
        count += 1
