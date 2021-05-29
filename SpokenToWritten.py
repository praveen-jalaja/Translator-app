import spacy
import en_core_web_sm
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy
from word2number import w2n


class spk2wrt:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.tuples_nums = {"single": 1,
                            "double": 2,
                            "triple": 3,
                            "quadruple": 4,
                            "quintuple": 5,
                            "sextuple": 6,
                            "septuple": 7,
                            "octuple": 8,
                            "nonuple": 9,
                            "decuple": 10
                            }

    def Multiplier(self, text):
        text_splits = text.split()
        doc = self.nlp(text.lower())
        matcher = Matcher(self.nlp.vocab)
        pattern = [
            {'LOWER': {
                "REGEX": "(?:single|double|triple|quadruple|quintuple|sextuple|septuple|octuple|nonuple|decuple)"},
             'POS': 'ADJ'},
            {'POS': {'NOT_IN': ['VERB', 'AUX', 'ADJ', 'PRON', 'ADV']}}]
        matcher.add("Matching", [pattern])
        matches = matcher(doc)
        doc_2 = self.nlp(text)
        indicies = []
        multiplier_words = [(str(doc_2[start:end].text), start, end) for id, start, end in matches]
        i = 0
        for words, start, end in multiplier_words:
            indicies.append(start - i)
            words_split = words.split()
            if words_split[0].lower() in self.tuples_nums.keys():
                text_splits[end - 1] = self.tuples_nums[words_split[0].lower()] * words_split[1]
            else:
                text_splits = text_splits

            i += 1

        for z in indicies:
            del text_splits[z]

        return ' '.join(text_splits)

    def MoneyConvertor(self, money_ls):
        currency = ["dollars", "dollar", "euro", "euros", "yens", "yen", "rupee", "rupees", "pound", "pounds"]
        money = []
        for a in money_ls:
            a = a.lower()
            a = a.split()
            b = [word for word in a if word in set(currency)]
            b = ' '.join(b)
            if b == "dollars" or b == "dollar":
                symbol = "$"
            elif b == "euros" or b == "euro":
                symbol = "€"
            elif b == "yens" or b == "yen":
                symbol = "¥"
            elif b == "pound" or b == "pounds":
                symbol = "£"
            else:
                symbol = ""
            a = [word for word in a if word not in set(currency)]
            a = ' '.join(a)
            p = symbol + str(w2n.word_to_num(a))
            money.append(p)
        return money

    def QunatityConvetor(self, quan_ls):
        quantity = ["pounds", "kilograms", "grams"]
        quan = []
        for a in quan_ls:
            a = a.lower()
            a = a.split()
            b = [word for word in a if word in set(quantity)]
            b = ' '.join(b)
            if b == "pounds":
                symbol = " lbs"
            elif b == "kilograms":
                symbol = " kg"
            elif b == "grams":
                symbol = " gm"
            else:
                symbol = ""
            a = [word for word in a if word not in set(quantity)]
            a = ' '.join(a)
            quan.append(str(str(w2n.word_to_num(a)) + symbol))

        return quan

    def QuantityMoneyTranslate(self, text):
        doc = self.nlp(text)

        money_ls = []
        quan_ls = []
        for x in doc.ents:
            if x.label_ == 'MONEY':
                money_ls.append(str(x))
            if x.label_ == 'QUANTITY':
                quan_ls.append(str(x))
        money = self.MoneyConvertor(money_ls)
        quan = self.QunatityConvetor(quan_ls)

        j = 0
        k = 0
        final_str = []
        for Y in doc:
            if Y.ent_iob_ == 'B' and Y.ent_type_ == 'QUANTITY':
                final_str.append(str(quan[j]))
                j = j + 1
            elif Y.ent_iob_ == 'I' and Y.ent_type_ == 'QUANTITY':
                final_str = final_str
            else:
                final_str.append(str(Y))

        final_text = ' '.join(final_str)

        doc = final_text
        doc = self.nlp(final_text)

        k = 0
        final_str_1 = []
        for Y in doc:
            if Y.ent_iob_ == 'B' and Y.ent_type_ == 'MONEY':
                final_str_1.append(str(money[k]))
                k = k + 1
            elif Y.ent_iob_ == 'I' and Y.ent_type_ == 'MONEY':
                final_str_1 = final_str_1
            else:
                final_str_1.append(str(Y))

        final_text_1 = ' '.join(final_str_1)
        return final_text_1

    def translate(self, text):
        return self.QuantityMoneyTranslate(self.Multiplier(text))
