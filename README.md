# Spoken English to Written English Translator
 Description - A Translator app which translates the spoken Raw text into Written English Translator.
 
 For example, Triple B will be translated into BBB.
 six thousand dollars will be translated into $6000.
 
 
 
- Using Spacy, all the tuple in the text, quantity, numbers in letters are converted using basic logic.
- other features like abbrevation are have to be implemented later. 
- I have used spacy pattern matching and entity modulue to translate the spoken english to written English


Instructions to use this web-app.

- Go the app: [spoken2writtenapp](https://spoken2writtenapp.herokuapp.com/)
- Insert the text in the text box and click on transalte.
- And the result will be displayed.

Instruction to use it as library:

```
Install spacy, word2number as dependecies

```
Clone the repository on the local machine with the below code.
```
##Clone this repository
git clone https://github.com/praveen-jalaja/TranslatorApp/edit/main/README.md
```

```
from TranslatorApp.SpokenToWritten import spk2wrt
trans = spk2wrt()
trans.translate("My life is Triple B . European authorities fined Google a record sixty five thousand dollars on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices . Furthermore , My T - Shirt size is double X in 2019 and it costs six dollars . My weight is fifty kilograms .")
```


