# #coding:utf-8
# from untils.send_request import send_request
#
# def test_send_request():
#     url="https://twww.bitasset.cc:7001/proxy/user/token"
#     headers = {
#         "cookie":"JSESSIONID=8e5051e0-905e-4193-ad22-2feac7cd696c",
#         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
#     }
#     res = send_request("GET",url,headers=headers)
#     print(res.text)
#
#
#
# if __name__ == "__main__":
#     test_send_request()

from untils.run_main import runner
if __name__ == "__main__":
    #test_send_request()
    runner = runner()
    runner.join_case()
    runner.sum()