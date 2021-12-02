import pytest
import allure
import os
import json
from apirequest import baseRequest
from get_excle_data import hand_excl, tg_root

@allure.feature('测试请求')
class Testmain():
    data1 = [tuple(hand_excl.row_datas(j)) for j in range(1, (hand_excl.get_nrow()))]  #迭代器，循环取出excle中的数据

    @allure.story("登录用例")
    @allure.title('{title}')
    # @allure.testcase('投顾接口')
    @pytest.mark.parametrize('methods,urls,datas,headers, title', data1)
    def test_mian(self, methods, urls, datas, headers, title):
        if headers == '':
            header = ''
        else:
            header = json.loads(headers)  #判断header是不是为空，不为空需要解析为json格式
        main_respone = baseRequest.send_request(methods, urls, datas, header)
        res = main_respone.status_code
        assert res == 200


if __name__ == '__main__':
    report_data = os.path.join(tg_root, 'test_report/result')
    report_path = os.path.join(tg_root, 'test_report/report')
    pytest.main(['--alluredir', f'{report_data}', 'test_live_case.py'])
    # pytest.main(['-s', 'test_live_case.py'])
    os.system(f'allure generate {report_data} --clean -o {report_path} ')