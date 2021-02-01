import pyttsx3 as pys
import PyPDF2 as pypdf

# Must enter complete path including book name and extension
bookPath = input("Enter book path : ")
book = open(bookPath, 'rb')
pdfReader = pypdf.PdfFileReader(book)

# pages = pdfReader.numPages
# print(pages)

engine = pys.init()
voices = engine.getProperty("voices")
rate = engine.getProperty("rate")

# print("Male voice : {0}".format(voices[0].id))
# print("Female voice : {0}".format(voices[1].id))
# engine.say("Hey, how's your day?")

# Setting voice and rate of speech
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 275)

# engine.say("Hey, how's your day?")

# Taking starting and ending pages as input
start = int(input("Enter the starting page : "))
end = int(input("Enter the ending page : "))

# Reading through pages
for num in range(start, end) :
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
