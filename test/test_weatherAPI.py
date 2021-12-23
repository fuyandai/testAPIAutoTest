import requests
import pytest
import json
import base64

# class Test_mark():
# pytest -v -m positive

# Test target API info: URL
URL = 'http://apis.juhe.cn/simpleWeather/query' # API URL
# key = '3caebaf468ae28396d385c3575bf35d4' # The API credential key that need to register in the website

# 加密Key之后，只留加密字段，要用的时候解密一下
# enckey = base64.b64encode('3caebaf468ae28396d385c3575bf35d4'.encode())
enckey = 'M2NhZWJhZjQ2OGFlMjgzOTZkMzg1YzM1NzViZjM1ZDQ='
deckey = str(base64.b64decode(enckey))[2:-1]
key = deckey

head = '' # API head
body = {
    "city": "上海",
    # "cityname": "上海",
    "key": key,
    "dtype": "json",
    "format": 1
}

@pytest.mark.smoke
@pytest.mark.positive
def test_weather_positive_happypath():
    res = getAPI(URL, body)
    result1 = res.json()
    print(json.dumps(result1, indent=4,ensure_ascii=False))
    assert result1['error_code'] == 0

@pytest.mark.negative
def test_weather_negative_wrongcity():
    body1 = {
        "key": key,
        "city": "abc"
    }
    res = getAPI(URL, body1)
    result1 = res.json()
    print(json.dumps(result1, indent=4, ensure_ascii=False))
    assert result1['error_code'] == 207301
    assert result1['reason'] == "暂不支持该城市"

@pytest.mark.negative
def test_weather_negative_wrongkey():
    body1 = {
        "key": key+'123',
        "city": "abc"
    }
    res = getAPI(URL, body1)
    result1 = res.json()
    print(json.dumps(result1, indent=4, ensure_ascii=False))
    assert result1['error_code'] == 10001
    assert result1['reason'] == "错误的请求KEY"

def getAPI(URL, body):
    print('API requests get begin:')
    response = requests.get(URL, body)
    result = response.json()
    result = json.dumps(result, indent=4,ensure_ascii=False)
    # print(f'API response: {result}')
    return response

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def setup():
    print("函数级别的前置")


def teardown():
    print("函数级别的后置")
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     # print(enckey)
#     # print(deckey)
#     # getAPI()
#     test_weather_negative_wrongcity()
#     test_weather_positive_happypath()

@pytest.mark.smoke
class TestAdd:

    def test_add_03(self):
        b = 1 + 2
        assert 3 == b

    def test_add_04(self):
        b = 1 + 1
        assert 2 == b