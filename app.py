import streamlit as st
from PIL import Image
import SpokenToWritten
import spacy
##from spacy.matcher import Matcher
##from spacy.tokens import Span
##from spacy import displacy
##from word2number import w2n
import webbrowser # inbuilt module


#=================================== Title ===============================
st.title("""
Spoken English to Written English Translator
	""")

#================================= Title Image ===========================
st.text("""""")
image = Image.open("static/image_1.jpg")
st.image(
	        image,
	        use_column_width=True,
	    )

#================================= About =================================
st.write("""
## 1️⃣ About
	""")
st.write("""
Hi all, Welcome to this project. It is a Spoken English to Written English Translator!!!
	""")
st.write("""
You have to write the spoken english in the text box!!!
	""")

#============================ How To Use It ===============================
st.write("""
## 2️⃣ How To Use It
	""")
st.write("""
Well, it's pretty simple!!!
- Please write or copy paste the spoken english in the text box below.
- Press the **👉🏼 Translate** button to see the magic!!!

🔘 **NOTE : ** * This translator is basic and not advanced one* 
	""")

#============================ Behind The Scene ==========================
st.write("""
## 5️⃣ Behind The Scene
	""")
st.write("""
To see how it works, please click the button below!
	""")
st.text("""""")
github = st.button("👉🏼 Click Here To See How It Works")
if github:
	github_link = "https://github.com/praveen-jalaja/streamlit-hatefulmemedection"
	try:
		webbrowser.open(github_link)
	except:
		st.write("""
    		⭕ Something Went Wrong!!! Please Try Again Later!!!
    		""")

#======================== Time To See The Magic ===========================
st.write("""
## 👁️‍🗨️ Time To See the Translation 🌀
	""")

##================================Intiating the object function=======================================

trans = SpokenToWritten.spk2wrt()

#========================== text Uploader ===================================

user_input = st.text_area("Paragraph here", "")

#================================= Predict Button ============================
st.text("""""")
submit = st.button("👉🏼 Translate")


##=================prediction================================================#
def generate_result(translated_text):
	st.write("""
	## 🎯 RESULT
		""")
	st.write(translated_text)

#=========================== Predict Button Clicked ==========================
if submit:
  	
  # Predicting
  st.write("👁️ Translate...")
  translated_text = trans.translate(user_input)
  generate_result(translated_text)

#=============================== Copy Right ==============================
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.text("""""")
st.write("""
### ©️ Created By Praveen Jalaja
	""")
