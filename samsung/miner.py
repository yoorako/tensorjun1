from konlpy.tag import Okt
import  re
class Samsung:
    def __int__(self):
        pass

    @staticmethod
    def __init__():
        okt = Okt()
        okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        filename = 'data/kr-Report_2018'
        with open(filename, 'r', encoding='utf-8')as f:
            texts = f.read()
        return texts

    @staticmethod
    def extract_hangeul(texts):
        temp = text.replace('\n', '|') #줄바꿈 제거
        tokenizer = re.compile(r'[^ ㄱ-힣]+') #한글만
        temp = tokenizer.sub('', temp)
        return temp

   @staticmethod
    def change_token(texts):
         tokens = word tokenize()
         print(tokens[:7])

