from wordchain import *
import changable

class GeneralizedKor(WordRule):
    def __init__(self, minlen, maxlen, headindex, tailindex, changable = True):
        self.minlen = minlen
        self.maxlen = maxlen
        self.headindex = headindex
        self.tailindex = tailindex
        self.ischangable = changable
        super().__init__()

    def get_data(self):
        with open("data/elrule.txt", 'r') as f:
            word_list = [word.strip('\n').strip('\ufeff').strip(' ') for word in f.readlines() if self.minlen <= len(word.strip('\n').strip('\ufeff').strip(' ')) <= self.maxlen]
        return word_list
    
    def head(self, word):
        return word[self.headindex]

    def tail(self, word):
        return word[self.tailindex]
    
    def changable(self, index):
        if not self.ischangable:
            return (index,)
        return changable.changable(index)
    


class Kor(WordRule):

    def get_data(self):
        with open("data/elrule.txt", 'r') as f:
            word_list = [word.strip('\n').strip('\ufeff').strip(' ') for word in f.readlines()]
        return word_list
    
    def head(self, word):
        return word[0]

    def tail(self, word):
        return word[-1]
    
    def changable(self, index):
        return changable.changable(index)


class KorEnd2(WordRule):

    def get_data(self):
        with open("data/elrule.txt", 'r') as f:
            word_list = [word.strip('\n').strip('\ufeff') for word in f.readlines() if len(word.strip('\n').strip('\ufeff')) > 2]
        return word_list
    
    def head(self, word):
        return word[:2]

    def tail(self, word):
        return word[-2:]
    
    def changable(self, index):
        return (index,)

class KorEnd3(WordRule):
    def get_data(self):
        with open("data/elrule.txt", 'r') as f:
            word_list = [word.strip('\n').strip('\ufeff') for word in f.readlines() if len(word.strip('\n').strip('\ufeff')) > 3]
        return word_list
    
    def head(self, word):
        return word[:3]

    def tail(self, word):
        return word[-3:]
    
    def changable(self, index):
        return (index,)

class KorEnd4(WordRule):
    def get_data(self):
        with open("data/elrule.txt", 'r') as f:
            word_list = [word.strip('\n').strip('\ufeff') for word in f.readlines() if len(word.strip('\n').strip('\ufeff')) > 4]
        return word_list
    
    def head(self, word):
        return word[:4]

    def tail(self, word):
        return word[-4:]
    
    def changable(self, index):
        return (index,)

class KorMid(WordRule):

    def get_data(self):
        with open("data/elrule.txt", 'r') as f:
            word_list = [word.strip('\n').strip('\ufeff') for word in f.readlines() if len(word.strip('\n').strip('\ufeff')) %2 == 1 and len(word.strip('\n').strip('\ufeff'))] 
        return word_list
    
    def head(self, word):
        return word[0]

    def tail(self, word):
        return word[len(word) // 2]
    
    def changable(self, index):
        return changable.changable(index)

class Eng1(WordRule):

    def get_data(self):
        with open("data/words_alpha.txt", 'r') as f:
            word_list = [word.strip('\n').strip('\ufeff') for word in f.readlines() if len(word.strip('\n').strip('\ufeff')) > 2]
        return word_list
    
    def head(self, word):
        return word[0]

    def tail(self, word):
        return word[-1]
    
    def changable(self, index):
        return (index,)

class Eng(WordRule):

    def get_data(self):
        with open("data/kkutueng.txt", 'r') as f:
            word_list = [word.strip('\n').strip('\ufeff') for word in f.readlines() if len(word.strip('\n').strip('\ufeff')) > 2]
        return word_list
    
    def head(self, word):
        return word[:2]

    def tail(self, word):
        return word[-2:]
    
    def changable(self, index):
        return (index,)

class EngRev(WordRule):

    def get_data(self):
        with open("data/kkutueng.txt", 'r') as f:
            word_list = [word.strip('\n').strip('\ufeff') for word in f.readlines() if len(word.strip('\n').strip('\ufeff')) > 2]
        return word_list
    
    def head(self, word):
        return word[-2:]

    def tail(self, word):
        return word[:2]
    
    def changable(self, index):
        return (index,)

class Test1(WordRule):
    
    def get_data(self):
        word_list = ['갖갖','갖은돼지시변','갖춘탈바꿈','겁축','겁죽','겁맹','겁결','겁욕','견취견','견묘','견직','견방직','견혼식','견이불식','견습','견융','견득','견삭','견척','견권','견락시권','견효','견식','견벽','견축','견결','견고해변','견죽', '결결','결핍','결획','결정축','결정권','결재권','결의권','결어중첩','결삭','결관삭','결벽','결맹','결척','결식','결관식','결혼식','결혼례식','결혼기념식','결핵균','결좌','결가부좌','결택','결자웅','결권','결궤','결득','결견','겸지우겸','겸칭','겸섭','겸업','겸득','겸괘','겸직','곬섶','곶사비낭','곶닢','곽재겸','곽희','곽학송','괘견','괘변','괘직','괘사직','괘상현','괘하현','괘효','굉굉','굉업','굉규','굉변','굉확','굉재탁식','굳기름','굵은밸','굵은밸균','굽벽','굽뒤축','굽은균','굽이흐름','궁궁','궁핍','궁궐','궁현','궁척','궁권','궁결','궁합지괘','궁첩','궁수좌','궁서설묘','궁사멱득','궁장식','궁팔십','궁심멱득','궁묘','궁둔','궁멱','궁듕','궁을','궁인직','궁사무척','궁준','궁축','궁춘','궁낭','궁깃','궁륭','궁벽', '권덕규','권굉','권칭','권익륭','권벽','권첩','권축','권뢰','권고사직','권유식','권변','권삭','권삼득','권섭','권전법륜','권좌','권현','권중현','권폄','권혁','권흉','권균','권설직','권업','권식','권척','권결','권준', '궐획','궐희','궐직','궐식', '규규','규곽','규견','규괘','규식지희','규법의식','규식','규소기름','규칙별구름','규벽','규결','규칙물결','규획','규춘','규준', '균핵균','균축','균륜','균습','균현','균질권','균권','균실번식','귤잎','귤홍','궤맹','궤변','궤촉','궤직','궤좌','궤도업','궤멸','궤핍','궤결','긁어냄','긱겁','깃촉','깃꼴잎','깊은바다물결','깡통계좌','깻잎','꺽죽','꽂임촉','꽝낭','꽤지름','꺾꽂이묘','꺾은지붕','꺾은획','꺾인지붕','꺾임결','꺾임지붕','껭변','껭낭','꽈배기엿','꿈밖','꿈결','꿩의비름','끽겁','낑깡','낭핍','낭유도식','낭자궤','낭지겁','낭축','낭랑묘','낭갈레죽','낭식','낭직','낭비벽','낯가죽','낸드름','냇둑','냄새뇌','넷째','녓곶','높쌘구름','높은이랑식','높은잎','높층구름','높은더미구름','높은층구름','뇌뢰','뇌척수막염균','뇌막염균','뇌굉','뇌변','뇌궁','뇌홍','뇌준','뉫결','늑흔','늑삭','늠준','늠균','늠식','늠축','덮깃','됫박구궁','됫밑','둑신묘','둑지꽝','둔폄','둔벙','둔괘','둠벙','둠붕','듕깃','득첩','득업','득결','득희','득롱망촉','득도식','득송','득효','듬벙','딩기죽','또변','뚬붕','띤죽','뢰준','뢰촉','뢰홍','뢰명산붕','룽징춘','륜첩','륜습','륜좌','륜직','륜척','륭준','륵흔','륵삭','맘결','맑은대쑥','맑은물못','맷돌흐름','맹꽁이맹','맹습','맹연습','맹삭','맹견','맹도견','맹묘','맹벽','맹종죽','맹험','맹홍','맹춘','맹낭','멋낭','멤버십','멱씨름','멱득','멸칭','멸균','못갖춘탈바꿈','묘획','묘삭','묘직','묘윤','묘득','묘유권','묘식','묘축','묘준','묘궁','묘사전궁','묽은음식','뭉게구름','믌결','밑거름','밑굽','밑깃','밖굽','밖벽','밸굽','밸벽','밸호흡','벗어난끝바꿈','벙드레죽','벡보름','벳꽂','벽읍','벽중깃','벽궁','벽견','변지변','변상가변','변읍','변멸','변희','변압기기름','변궁','변화무궁','변상벽','변두리벽','변호권','변축','변형식','변관식','변혁','변칭','변형균','변두죽','변흔','변견','변죽','봇둑','붕획','붕결','붕어마름','붕따우곶','붕괴권','붕사용융','붕어죽','붕어톱','붕궤','붙박이식','뷔송','뷔퐁','븘곶','빅씨름','빠름','빡죽','뺨가죽','빼빼','빼깃','뾰족지붕','삐삐','삐욱','삭즉삭','삭름','삭벽','삭직','삭탈관직','삭축','삸오뇌','삸밑','샹샹','샹쑥','샹송','섭벽','섭식','섭직','섭험','섭육십','섭죽','섶가랑잎','솟을지붕','송자송','송욱','송병준','송고직','송화다식','송치규','송이구름','송깃','송산현','송기죽','송엽죽','송죽','송피죽','송춘','송습','송척','송괘','송뢰','송축','송별식','쇄식','쇄홍','쇄직','쇳닢','쇳송','습궐','습유보궐','습벽','습업','습직','습득','습윤','습자첩','습곡축','습식','습도식','습입식','식식','식업','식료공업','식산흥업','식료가공업','식료가공공업','식겁','식읍','식멸','식균','식용균','식초산균','식당직','식견','식권','식희','식혜암죽','식민지리윤','식변','식욕','식낭','식송','식궐','십겁','십습','십년일득','십불선업','십장식','십이궁','십자좌','십자못','십자나사못','십주희','싯줴','쌘구름','쌘비구름','썰물흐름','쎅찌야식','쐐기가름','쑥엿','업시름','업축','업무권','엑스축','엿기름','엿궤','엿죽','옆모습','옆벽','옆변','옆잎','옆주름','옛꿈','욕중관수욕','욕식','욧거죽','욱은지붕','웅읍','웅도거읍','웅주거읍','웅묘','웅사굉변','웅변','웅문거벽','웅천거벽','웅준','윤동규','윤흔','윤곽','윤택','윤멸','윤희','윤덕희','윤업','윤현','윤습','윤첩','윤변','윤척','윤삭','윤직','윤희결','윤좌','윤선좌','윤제홍','윤흡','윤곽괘','윤봉춘','윤준','윤식','윤축','융희','융즉','융준','융식','융궁','읍륵','읍권','을묘','을묘왜변','을미개혁','을미사변','을축','을좌','읏듬','잎덧거름','잎자욱','잎밑','잗주름','잘못','잘잘못','잘못보냄','잘텐','잘겁','잴봇','젬벽','젯구름','좁쌀엿','좁쌀죽','좌향좌','좌뇌','좌사윤','좌직','좌사직','좌승직','좌반전직','좌부승직','좌규','좌업','좌변','좌부변','좌권','좌석권','좌척','좌우청촉','좌청우촉','좌식','좌궁깃','좌현','좌보궐','좌우켠','좌험','좌표축','죽죽','죽엽죽','죽력죽','죽척','죽는시늉','죽소춘','죽림칠현','죽궤','죽궁','죽을사변','죽식','죽견','준규','준민고택','준삭','준척','준직','준좌','준맹','준변','준거좌','준견','준축','준호구식','준공식','준준무식','준뢰','준물권','줴피낭','직업','직매상업','직관수업','직교축','직핍','직첩','직맹','직업동맹','직각변','직결','직렬연결','직송','직격뢰','직업의식','직효','직파양식','직접조종방식','직각주사기록방식','직삼궁','직사궁','직척','직궁','직장낭','직권','즉멸','즉견','즉결','즉좌','즉위식','즉효','즐욕','째못','찹쌀엿','찹쌀다식','챙견','챙지름','척택','척촉','척수공권','척결','척삭','척벽','척사희','척석희','척식','척촌지효','척확','척축','척홍','첩첩','첩섭','첩시꽂','첸지꽂','첸양현','촉규','촉륜','촉식','촉직','촛밑','축대칭','축융','축첩','축자식','축하식','축성식','축판식','축보름','축척','축산업','축좌','축견','축삭','축송','축세륜','춘희','춘뢰','춘궁','춘첩','춘삭','춘삼삭','춘경추확','춘대옥촉','춘식','춘축','춘효','춘규','췌괘','췌변','칭굉','칭웅','칭직','칭병사직','칭송','캄캄절벽','캉캉','캉딩','캠축','캠핑','컴맹','켠씨름','콥트직','콴툼','쾌쾌','쾌변','쾌둔','쾌척','쾌괘','퀘벡','택곽','택견','택식','택현','탤컴','탤벗','텃삭','텃세권','텐디꽂','템포슈붕','텡지여름','툼벙','튐성여효','틸트업','팝송','폄칭','폄직','폄척','폄좌','퐁텐','퐁텐블로궁','푿소가죽','핍축','핍궤','핑딩','핑퐁','험득','험윤','험결','험좌','헙낭','헷노름','헷밑','헹겟나잘','헹경낭','혁직','혁업','혁명권','혁명주권','혁괘','혁낭','혁현','현현','현폄','현겁','현대식','현판식','현칭','현척','현궁','현준','현벽','현상벽','현수벽','현업','현출작업','현윤','현상윤','현삭','현촉','현직','현험','현춘','현순백결','현상우변','현하웅변','현하구변','현하지변','현상양좌','현미경좌','현상량좌','현좌','현괘','현묘','현효','현행계획','현택','현혁','혐핍','혐연권','혐흡','홍업','홍척','홍첩','홍혁','홍원식','홍만식','홍범식','홍시죽','홍죽','홍합죽','홍색견','홍견','홍벽','홍수벽','홍예벽','홍계희','홍명희','홍희','홍대촉','홍촉','홍륜','홍색세균','홍규','홍대둑','홍둔','홍예밑','홍이섭','홍월귤','확산권','확삭','확견','확준','확효','확대척','획득','효고현','효근귤','효모균','효죽','효웅','효창묘','효험','효습','효득','흉겸','흉곽','흉괘','흉벽','흉변','흉호흡','흔캄','흔들축','흔굉','흔희','흔척','흘레구름','흡배기변','흡습','흡연권','흡음벽','흡현','희희','희읍','희칭','희첩','희망권','희견궁','희망퇴직','희죽','희준','희소식', '톱날지붕']
        return word_list

    def head(self, word):
        return word[0]

    def tail(self, word):
        return word[-1]
    
    def changable(self, index):
        return changable.changable(index)

class Test2(WordRule):

    def get_data(self):
        word_list = ["ab", "acb", "adb", "ba", "bb","bcb", "abb", "bcbc", "bc", "bna", "da", "ac", "bc", "ba", "bd", "cb", "cd", "da", "dca", "db", "dc", 'asd', 'ae', 'be', 'ce', 'de', 'dde', 'cce', 'ee', 'eae']
        return word_list

    def head(self, word):
        return word[0]

    def tail(self, word):
        return word[-1]
    
    def changable(self, index):
        return (index,)


class Test3(WordRule):

    def get_data(self):
        word_list = ['낙지새우숙회', '늘보주머니쥐', '홍허리대모벌', '먹장님노린재', '티오시안산염', '룡골버들잎벌', '날개무늬잎벌', '깜보라노린재', '능쟁이피부염', '여덟팔자수염', '범나비애기벌', '왕자루맵시벌', '장미등에잎벌', '빠리꼼뮨문학', '잎말이고치벌', '낚시오랑캐꽃', '낮은돋을새김', '용배수양수장', '망가니즈산염', '양식장동물학', '각시실노린재', '렌트겐진단학', '올레일알코올', '학부형위원회', '장백패랭이꽃', '회리전기마당', '엮음자진한잎', '염락관민지학', '십자긴노린재', '엄지머리총각', '또꼬바지장난', '회선고정대여', '떠꺼머리총각', '잔털오랑캐꽃', '연오랑세오녀', '려포성편도염', '꽃잎수다른꽃', '티오아비산염', '쥐꼬리선인장', '난부자든가난', '여름나이어장', '장백오랑캐꽃', '양주좀개수염', '줄무늬애기벌', '왜졸방제비꽃', '홍띠윤구멍벌', '켄타우루스좌', '재판외적제재', '회선임시대여', '밤나무애기벌', '십이월파문학', '벌거숭이박쥐', '참졸방제비꽃', '홀아비바람꽃', '먹테얼게비늘', '숫무우애기벌', '엷은잎제비꽃', '벌림판조임줄', '당중앙위원회', '좌변포도대장', '떠꺼머리처녀', '뽕나무노린재', '참나무노린재', '김일성경기장', '잣나무송곳벌', '각시패랭이꽃', '꽃봉오리흑벌', '깜둥긴노린재']
        return word_list

    def head(self, word):
        return word[0]

    def tail(self, word):
        return word[-1]
    
    def changable(self, index):
        return changable.changable(index)

class Kor23(WordRule):

    def get_data(self):
        with open("data/elrule.txt", 'r') as f:
            word_list = [word.strip('\n').strip('\ufeff').strip(' ') for word in f.readlines() if len(word.strip('\n').strip('\ufeff').strip(' ')) == 2 or len(word.strip('\n').strip('\ufeff').strip(' ')) == 4]
        return word_list
    
    def head(self, word):
        return (word[0], len(word))

    def tail(self, word):
        return (word[-1], 2 if len(word) == 4 else 4)
    
    def changable(self, index):
        changetuple = changable.changable(index[0])
        result = tuple()
        for c in changetuple:
            result += ((c, index[1]),)
        return result

class Kor234(WordRule):

    def get_data(self):
        with open("data/elrule.txt", 'r') as f:
            word_list = [word.strip('\n').strip('\ufeff').strip(' ') for word in f.readlines() if 2 <= len(word.strip('\n').strip('\ufeff').strip(' ')) <= 4]
        return word_list
    
    def head(self, word):
        return (word[0], len(word))

    def tail(self, word):
        if len(word) == 2 : 
            nextlen = 3
        elif len(word) == 3:
            nextlen = 4
        else:
            nextlen = 2
        return (word[-1], nextlen)
    
    def changable(self, index):
        changetuple = changable.changable(index[0])
        result = tuple()
        for c in changetuple:
            result += ((c, index[1]),)
        return result

class nojong(WordRule):

    def get_data(self):
        with open("data/elrule.txt", 'r') as f:
            word_list = [word.strip('\n').strip('\ufeff').strip(' ') for word in f.readlines() if isnojong(word.strip('\n').strip('\ufeff').strip(' '))]
        return word_list
    
    def head(self, word):
        return word[0]

    def tail(self, word):
        return word[-1]
    
    def changable(self, index):
        return (index,)

def isnojong(korean_word):
    r_lst = []
    for w in list(korean_word.strip()):
        ch1 = (ord(w) - ord('가'))//588
            ## 중성은 총 28가지 종류
        ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28
        ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2
        if ch3 != 0:
            return False
    return True