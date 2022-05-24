
from csr import csrFunc
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename



"""2. GUI 창"""
root = Tk()
root.geometry('200x100')

"""3. 파일 열기"""
file = askopenfilename(filetypes=[("All Files", "*.*")])
if file is not None:
    print(file)

    file2 = file




stt = csrFunc('or41v7xmp7', 'Y985MO35NtwqPcPbDCw7fBnZUdBmSmeXH3nOzLBk', file2)

"""5. 작성한 텍스트를 파일로 저장"""
f = open('C:\\UnityProject\\STTWithPy\\' + '결과1' + ".txt", 'w') # 원하는 폴더 경로를 설정해야 함
print(stt)
f.write(stt)
f.close()