"""200803_main.py"""
"""네이버 클라우드 API에서 제공하는 CSR 모듈을 활용한 음성을 텍스트로 변환하는 프로그램"""

"""GUI로 파일을 불러옴"""

"""1. 필요한 모듈"""
#파일을 GUI를 활용하여 열기
from tkinter import *
from tkinter.ttk import *
#파일 여는 기능
from tkinter.filedialog import askopenfilename

"""2. GUI 창"""
root = Tk()
root.geometry('200x100')

"""3. 파일 열기"""
def open_file():
    file = askopenfilename(filetypes=[("All Files", "*.*")])

    if file is not None:
        print(file)

        return file
