import  requests
from untils. log_trace import  *

#发送get请求
def get_request(url,data=None,headers=None):
    res = requests.get(url=url,data=data,headers=headers)
    return res

#发送post请求
def post_request(url,data,headers=None):
    res = requests.post(url=url,data=data,headers=headers)
    return res

#发送delete请求
def del_request(url,data=None,headers=None):
    res = requests.delete(url,data=data)
    return res

#发送put请求
def put_request(url,data,headers=None):
    pass

def send_request(method,url,data=None,headers=None):
    try:
        logging.info(headers)
        if headers:
            if method == "GET":
                return get_request(url,data,headers=headers)
            if method == "POST":
                return post_request(url,data=data,headers=headers)
            if method == "DELETE":
                return  del_request(url,data=data,headers=headers)
            #put使用频率低，暂时不写
            if method == "PUT":
                return  put_request(url,data=data,headers=headers)
        else:
            logging.info("Header is null")
    except Exception as e:
        logging.info("send request fail:%s"%e)