from csr import csrFunc
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from translate import translate
from threading import Thread
from time import sleep

TEXT_FILE = 'text.txt'
TARGET_FILE = 'text_translated.txt'

lang = 'Kor'

def getTextTranslated(text_list):
    text_translated_list = []
    for text in text_list:
        text_translated_list.append(translate(text))
    return text_translated_list


def write(filename, content_list):
    with open(filename, 'w') as f:
        for content in content_list:
            f.write(content + '\n')


def getfile(): #파일 여는 함수
    global  file
    file = askopenfilename(filetypes=[("All Files", "*.*")])
    if file is not None:
        lbl2.config(text=file)


def changeSoundToText():
    lbl7.config(text='진행상태 : 음성을 텍스트로 변환 중입니다.')
    print("음성을 텍스트로 변환 중입니다.")
    print(file)
    stt = csrFunc('or41v7xmp7', 'ze8JKUSNnFleu3zmzdemIbLcKXvxlrCeNwDCBxUx', file)
    lab4.config(text=stt)
    lbl7.config(text='진행상태 : 음성 변환 완료.')
    print(stt)
    text_list = []
    text_list.append(stt)
    lbl7.config(text='진행상태 : 텍스트를 영어로 변환중입니다..')
    text_translated_list = getTextTranslated(text_list)
    lab6.config(text=text_translated_list)
    lbl7.config(text='진행상태 : 변환 완료.')
    print(text_translated_list)


if __name__ == '__main__':

    """2. GUI 창"""
    root = Tk()

    lbl = Label(root, text = "선택한 파일 경로")
    lbl.config(font=('바탕체', 20,'bold'))
    lbl.grid(row=0)

    lbl2 = Label(root, text='파일을 선택 해주세요.',justify= CENTER)
    lbl2.config(font=('바탕체',15))
    lbl2.configure(foreground = 'red')
    lbl2.grid(row=1)

    button1 = Button(root,text='파일열기',command=getfile)
    button1.grid(row=2)

    lbl7 = Label(root, text="진행상태 : 대기중",font=('바탕체',15,'bold'))
    lbl7.grid(row=3)





    button2 = Button(root, text='변환 하기', command=changeSoundToText)
    button2.grid(row=6)

    lab3 = Label(root, text= '음성을 텍스트로 변환한 결과',font=('바탕체',20),justify= CENTER)
    lab3.grid(row=7)

    lab4 = Label(root, text=' ', font=('바탕체', 15,'bold'), justify=CENTER,foreground='red')
    lab4.grid(row=8)

    lab5 = Label(root, text='텍스트를 번역한 결과', font=('바탕체', 20), anchor=CENTER,justify=CENTER)
    lab5.grid(row=9)

    lab6 = Label(root, text=' ', font=('바탕체', 15,'bold'), justify=CENTER, foreground='red')
    lab6.grid(row=10)

    root.mainloop()