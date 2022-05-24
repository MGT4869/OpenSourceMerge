import os

from translate import translate

TEXT_FILE = 'text.txt'
TARGET_FILE = 'text_translated.txt'


def getText(file):
    text_list = []
    with open(file, 'r') as f:
        while True:
            text = f.readline()
            if not text: break
            text_list.append(text)
    return text_list


def getTextTranslated(text_list):
    text_translated_list = []
    for text in text_list:
        text_translated_list.append(translate(text))
    return text_translated_list


def write(filename, content_list):
    with open(filename, 'w') as f:
        for content in content_list:
            f.write(content + '\n')


if __name__ == '__main__':
    print('번역 수행중...')
    text_list = []
    text_list.append("실험")
    text_list.append('입니다')
    #text_list = getText(TEXT_FILE)
    text_translated_list = getTextTranslated(text_list)
    write(TARGET_FILE, text_translated_list)
    print('번역 완료')
