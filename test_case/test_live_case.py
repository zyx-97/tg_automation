import pytest
import allure
import os, sys
import json
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), '/base'))
from base.apirequest import baseRequest
from base.get_excle_data import data1, tg_root
from datetime import datetime

@allure.feature('测试请求')
class Testmain():
    # data1 = [tuple(hand_excl.row_datas(j)) for j in range(1, (hand_excl.get_nrow()))]  #迭代器，循环取出excle中的数据

    @allure.story("登录用例")
    @allure.title('{title}')
    # @allure.testcase('投顾接口')
    @pytest.mark.parametrize('methods,urls,datas,headers, title', data1)
    def test_mian(self, methods, urls, datas, headers, title):
        if not headers:
            header = ''
        else:
            header = json.loads(headers)  #判断header是不是为空，不为空需要解析为json格式
        main_respone = baseRequest.send_request(methods, urls, datas, header)
        res = main_respone.status_code
        assert res == 200


if __name__ == '__main__':
    day = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_data = os.path.join(tg_root, f'test_report/test_report{day}/result')
    report_path = os.path.join(tg_root, f'test_report/test_report{day}/report')
    pytest.main(['--alluredir', f'{report_data}', os.path.abspath(__file__)])
    # pytest.main(['-s', os.path.abspath(__file__)])
    os.system(f'allure generate {report_data} -o {report_path}')
    os.system(f'allure open {report_path}')