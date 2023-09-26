import pyttsx3
import PyPDF2

hikaye = open("deep-learning.pdf", "rb")
pdfOkuyucu = PyPDF2.PdfReader(hikaye)

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
for sayfa_numarasi in range(0, len(pdfOkuyucu.pages)):
    sayfa = pdfOkuyucu.pages[sayfa_numarasi]
    yazi = sayfa.extract_text()
    engine.say(yazi)

engine.runAndWait()
