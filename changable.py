import collections

def changable(char):

    o = ord(char)


    if ord('랴') <= o <= ord('럏') or\
        ord('려') <= o <= ord('렿') or\
        ord('료') <= o <= ord('룧') or\
        ord('류') <= o <= ord('륳') or\
        ord('리') <= o <= ord('맇') or\
        ord('례') <= o <= ord('롛'):
        return [char, chr(o + ord('아') - ord('라'))]
    if ord('라') <= o <= ord('랗') or\
        ord('래') <= o <= ord('랳') or\
        ord('로') <= o <= ord('롷') or\
        ord('루') <= o <= ord('뤃') or\
        ord('르') <= o <= ord('릏') or\
        ord('뢰') <= o <= ord('룋'):
        return [char, chr(o + ord('나') - ord('라'))]
    if ord('녀') <= o <= ord('녛') or\
        ord('뇨') <= o <= ord('눃') or\
        ord('뉴') <= o <= ord('늏') or\
        ord('니') <= o <= ord('닣'):
        return [char, chr(o + ord('아') - ord('나'))]
    return [char]


CHO = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 
    'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]
JUNG = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 
    'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
]

JONG = [
    '', 'ㄱ','ㄲ','ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 
    'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 
    'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]


def break_korean(string):
    break_words = []
    for k in string:
        if ord("가") <= ord(k) <= ord("힣"):
            index = ord(k) - ord("가")
            c_cho = int((index / 28) / 21)
            c_jung = int((index / 28) % 21)
            c_jong = int(index % 28)

            break_words.append(CHO[c_cho])
            break_words.append(JUNG[c_jung])
            if c_jong > 0:
                break_words.append(JONG[c_jong])
        else:
            break_words.append(k)
    return break_words

