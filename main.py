"""200803_main.py"""
"""네이버 클라우드 API에서 제공하는 CSR 모듈을 활용한 음성을 텍스트로 변환하는 프로그램"""

"""음성에서 텍스트로 변환하는 기능을 호출하는 메인 모듈"""

"""1. 필요한 모듈"""
#파일 열기
from SoundToText.file import *
#파일 이름 - 경로를 제외한 순수 파일 이름
import re
# 어떤 언어로 녹음을 했는지 지정하고 해당 파일을 찾아서 글자로 변경
from SoundToText.csr import *
# 클라우드 api 및 파일 저장 경로가 저장된 개인정보
from SoundToText.privateInfo import *

"""2. API를 활용할 때 필요한 정보"""
# 네이버 클라우드 API(돈 드는 ID 및 Secret)_CSR, CPV, CSS API
cloudApi_clientId = clientID
cloudApi_clientSecret = clientPW

"""3. 파일 선택"""
file = open_file()

regexRuleDir = re.compile(".+/")
regexRuleType = re.compile("\.(.*?)$")

fileDirectory = regexRuleDir.search(file)
fileType = regexRuleType.search(file)

fileDirectory_group = fileDirectory.group()
fileType_group = fileType.group()

fileName = file.replace(fileDirectory_group, "").replace(fileType_group, "")

# print(fileName)

"""4. 저장된 음성 파일과 언어 선택을 하여 글자로 변경"""
stt = csrFunc(cloudApi_clientId, cloudApi_clientSecret, file)

"""5. 작성한 텍스트를 파일로 저장"""
f = open(savePath + fileName + ".txt", 'w') # 원하는 폴더 경로를 설정해야 함
f.write(stt)
f.close()




