import pyttsx3 as pys
import PyPDF2 as pypdf

book = open('clash.pdf', 'rb')
pdfReader = pypdf.PdfFileReader(book)

# pages = pdfReader.numPages
# print(pages)

engine = pys.init()
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")

# print("Male voice : {0}".format(voices[0].id))
# print("Female voice : {0}".format(voices[1].id))
# engine.say("Hey, how's your day?")

engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 275)

# engine.say("Hey, how's your day?")

start = int(input("Enter the starting page : "))
end = int(input("Enter the ending page : "))
for num in range(start, end) :
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
