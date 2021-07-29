import pyttsx3
import pdfplumber

PDF_PATH = "./sample.pdf"  # Add pdf path

with pdfplumber.open(PDF_PATH)as pdf:
    book_content = ""
    # Set pyttsx3
    speaker = pyttsx3.init()
    # Speech rate
    speaker.setProperty('rate', 130)
    # Speaker voices
    voices = speaker.getProperty('voices')
    # Setting speaker voice to female
    speaker.setProperty('voice', voices[1].id)
    for page in pdf.pages:
        text = page.extract_text()
        if text is not None:
            book_content += text
    # print(book_content)
    mp3_name = input("Enter mp3 file name:\t")
    speaker.save_to_file(book_content, f"{mp3_name}.mp3")
    speaker.runAndWait()
