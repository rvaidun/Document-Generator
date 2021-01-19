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
import json
with open('config.json') as f:
    config = json.load(f)
def createDocument(text, title, folder):
    classNames = config["class_names"]
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

    document.save('./' + folder + '/' + title.strip() + '.docx')


if __name__ == "__main__":
    amt = int(sys.argv[1])
    pages = config["wiki_articles"]
    generated = 0
    while generated < amt:
        try:
            page = wikipedia.page(random.choice(pages), auto_suggest=False)
            print("The url for page is " + page.url)
        except wikipedia.exceptions.PageError:
            print("One of the pages could not be found. Please check the pages again")
        page_content = page.content.split("== See also ==")[0]
        page_content = page_content.strip()
        page_content = sent_tokenize(page_content)
        chunked = []
        count = 0
        curstr = ""
        print("Paraphrasing Chunk "+ str(len(chunked)))
        for x in page_content:
            if count == config["num_sentences"]:
                count = 0
                chunked.append(curstr)
                print("Paraphrasing Chunk " + str(len(chunked)))
                curstr = ""
            curstr += paraphrase.paraphrase(x)
            count += 1
        chunked.append(curstr)
        count = 0
        if os.path.exists(page.title) == False:
            try:
                os.mkdir("./" + page.title)
            except OSError:
                print("Creation of the directory failed")

        print("Successfully created the directory")
        for x in chunked:
            print("Writing chunk " + str(count) +" to word doc")
            title = " ".join(nltk.word_tokenize(x)[0:3])
            createDocument(x, title, page.title)
            count += 1
            generated += 1
            if generated > amt:
                break
            else:
                print("Made " + str(generated) + " docs with this article so far. Need " + str(amt-generated) + " docs more.")
    print("Successfully generated " + str(amt) + " documents. Thank you!")
            
