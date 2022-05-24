"""200803_main.py"""
"""네이버 클라우드 API에서 제공하는 CSR 모듈을 활용한 음성을 텍스트로 변환하는 프로그램"""

"""녹음한 음성을 글자로 변경하는 모듈"""

"""
네이버 클라우드 API중 CSR API를 활용함
"""

"""1. 필요한 모듈"""
# 음성을 글로
import requests

"""2. 음성 파일을 글자로 변경"""

def csrFunc(cloudApi_clientId, cloudApi_clientSecret, wantToText):
    """음성을 글자로"""
    """2-1. 어떤 언어의 음성 파일을 변경할 것인지 입력 - 현재 가능한 것은 Eng와 Kor"""
    # inputLang = input('언어를 입력하세요: ')  # lang = "Eng" # 언어 코드 ( Kor, Jpn, Eng, Chn )

    """2-2. 네이버 CSR API를 활용하기 위해서 필요한 정보"""
    url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=Kor" # + inputLang
    data = open(wantToText, 'rb')
    headers = {
        "X-NCP-APIGW-API-KEY-ID": cloudApi_clientId,
        "X-NCP-APIGW-API-KEY": cloudApi_clientSecret,
        "Content-Type": "application/octet-stream"
    }
    response = requests.post(url, data=data, headers=headers)
    rescode = response.status_code
    if (rescode == 200):  # 응답이 성공했으면
        response_data = response.json()
        sttResult = response_data['text']
        return sttResult # 글자로 나온 결과와 설정해준 언어를 반환
    else:  # 200(성공)으로 떨어지지 않으면 이유를 출력. 음성 파일에 말이 없어도 에러가 떨어짐
        print("Error : " + response.text)
