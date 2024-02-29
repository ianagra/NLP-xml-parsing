import xml.dom.minidom as dom
import xml.sax as sax

# Using DOM to extract the AUTHORS
authorsRoot = dom.parse("cf79.xml")
authors = authorsRoot.getElementsByTagName("AUTHOR")
with open("authors.xml", "w") as authorsFile:
    for author in authors:
        authorName = author.firstChild.data
        authorsFile.write(authorName + "\n")

# Using SAX to extract the TITLES
class titleHandler(sax.ContentHandler):
    def __init__(txt):
        super().__init__()
        txt.inside_title = False
        txt.title_text = ""
    def startElement(txt, name, atrib):
        if name == "TITLE":
            txt.inside_title = True
    def characters(txt, content):
        if txt.inside_title:
            txt.title_text += content.strip()
    def endElement(txt, name):
        if name == "TITLE":
            with open("titles.xml", "a") as titlesFile:
                titlesFile.write(txt.title_text.replace("\n", " ") + "\n")
            txt.inside_title = False
            txt.title_text = ""
parser = sax.make_parser()
parser.setFeature(sax.handler.feature_external_ges, False)
handler = titleHandler()
parser.setContentHandler(handler)
parser.parse("cf79.xml")