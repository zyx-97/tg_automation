import requests


class Baserequest:
    def send_request(self,method, url, data=None, header=None):
        """
        发送请求
        :param method:请求方法(get/post)
        :param url:请求地址
        :param data:其他参数
        :param header:请求头
        """
        if method == 'post':
            respone = requests.request(method=f'{method}', url=url, json=data, headers=header)
        else:
            respone = requests.request(method=f'{method}', url=url, params=data, headers=header)

        return respone

baseRequest = Baserequest()
