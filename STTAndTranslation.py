from csr import csrFunc
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
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

    """2. GUI 창"""
    root = Tk()
    root.geometry('200x100')

    """3. 파일 열기"""
    file = askopenfilename(filetypes=[("All Files", "*.*")])
    if file is not None:
        print(file)

        file2 = file

    print("음성을 텍스트로 변환 중입니다.")
    stt = csrFunc('or41v7xmp7', 'ze8JKUSNnFleu3zmzdemIbLcKXvxlrCeNwDCBxUx', file2)

    """5. 작성한 텍스트를 파일로 저장"""
    f = open('C:\\UnityProject\\STTWithPy\\' + TEXT_FILE, 'w')  # 원하는 폴더 경로를 설정해야 함
    f.write(stt)
    text_list = []
    text_list.append(stt)
    f.close()
    print('변환이 완료되었습니다.')

    print('번역 수행중...')
    text_translated_list = getTextTranslated(text_list)
    write(TARGET_FILE, text_translated_list)
    print('번역 완료\n')

    print('입력된 음성은 아래와 같습니다.')
    print(stt+'\n')

    print('번역된 테스트는 아래와 같습니다')
    print(text_translated_list)