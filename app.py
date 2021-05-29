!python -m spacy download en_core_web_sm
import streamlit as st
from PIL import Image
import spacy
import en_core_web_sm
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy
from word2number import w2n
data_dir = "/streamlit-hatefulmemedection/"
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

##================================Preloading function=======================================
nlp = spacy.load("en_core_web_sm")
tuples_nums  = {
                         "single":1,
                         "double":2,
                         "triple":3,
                         "quadruple":4,
                         "quintuple":5,
                         "sextuple":6,
                         "septuple":7,
                         "octuple":8,
                         "nonuple":9,
                         "decuple":10
                      } 



@st.cache(allow_output_mutation=True)
def Multiplier(text):
    text_splits =text.split()
    doc=nlp(text)
    matcher = Matcher(nlp.vocab)
    pattern = [{'TEXT':{"REGEX":"(?:single|double|triple)"}, 'POS': 'ADJ'}, 
                {'POS':{'NOT_IN': ['VERB','AUX','ADJ','PRON','ADV']}}]
    matcher.add("Matching", None, pattern)
    matches = matcher(doc)
    indicies = []
    multiplier_words = [(str(doc[start:end].text), start, end) for id, start, end in matches]
    i = 0
    for words, start,end in multiplier_words:
      indicies.append(start-i)
      words_split = words.split()
      if words_split[0].lower() in tuples_nums.keys():
        text_splits[end-1] = tuples_nums[words_split[0].lower()]*words_split[1]
      else:
        text_splits = text_splits

      i+=1

    for z in indicies:
        del text_splits[z]

    return ' '.join(text_splits)


@st.cache(allow_output_mutation=True)
def MoneyConvertor(money_ls):
  currency=["dollars", "dollar", "euro", "euros", "yens", "yen", "rupee", "rupees", "pound", "pounds"]
  money=[]
  for a in money_ls:
        a=a.lower()
        a=a.split()
        b=[word for word in a if word in set(currency)]
        b=' '.join(b)
        if b=="dollars" or b=="dollar":
            symbol="$"
        elif b=="euros" or b=="euro":
            symbol="€"
        elif b=="yens" or b=="yen":
            symbol="¥"
        elif b=="pound" or b=="pounds":
            symbol="£"
        else:
            symbol=""
        a=[word for word in a if word not in set(currency)]
        a=' '.join(a)
        p=symbol+str(w2n.word_to_num(a))
        money.append(p)
  return money


@st.cache(allow_output_mutation=True)
def QunatityConvetor(quan_ls):
    quantity=["pounds","kilograms","grams"]
    quan=[]
    for a in quan_ls:
        a=a.lower()
        a=a.split()
        b=[word for word in a if word in set(quantity)]
        b=' '.join(b)
        if b=="pounds":
            symbol=" lbs"
        elif b=="kilograms":
            symbol=" kg"
        elif b=="grams":
            symbol=" gm"
        else:
            symbol=""
        a=[word for word in a if word not in set(quantity)]
        a=' '.join(a)
        quan.append(str(str(w2n.word_to_num(a))+symbol))

    return quan




@st.cache(allow_output_mutation=True)
def QuantityMoneyTranslate(text):
    doc = nlp(text)

    money_ls=[]
    quan_ls=[]
    for x in doc.ents:
      if x.label_ =='MONEY':
          money_ls.append(str(x))
      if x.label_ == 'QUANTITY':
          quan_ls.append(str(x))
    money = MoneyConvertor(money_ls)
    quan = QunatityConvetor(quan_ls)
    
    j = 0
    k = 0
    final_str= []
    for Y in doc:
        if Y.ent_iob_ =='B' and Y.ent_type_ =='QUANTITY':
            final_str.append(str(quan[j]))
            j=j+1
        elif Y.ent_iob_ =='I' and Y.ent_type_ =='QUANTITY':
            final_str=final_str
        else:
            final_str.append(str(Y))
        
    final_text=' '.join(final_str)

    doc=final_text
    doc=nlp(final_text)

    k=0
    final_str_1=[]
    for Y in doc:
        if Y.ent_iob_ =='B' and Y.ent_type_ =='MONEY':
            final_str_1.append(str(money[k]))
            k=k+1
        elif Y.ent_iob_ =='I' and Y.ent_type_ =='MONEY':
            final_str_1=final_str_1
        else:
            final_str_1.append(str(Y))
        
    final_text_1=' '.join(final_str_1)
    return final_text_1



#========================== text Uploader ===================================

user_input = st.text_area("Paragraph here", "")

#================================= Predict Button ============================
st.text("""""")
submit = st.button("👉🏼 Translate")


##=================prediction================================================#
def generate_result(prediction):
	st.write("""
	## 🎯 RESULT
		""")
	st.write(prediction)

#=========================== Predict Button Clicked ==========================
if submit:
  	
  # Predicting
  st.write("👁️ Translate...")
  translated_text = QuantityMoneyTranslate(Multiplier(para))
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
