import xlrd
from get_yaml_data import HandleYaml
import os

tg_root = os.path.dirname(os.path.dirname(__file__))  # 获取当前文件所在目录的上级目录
excle_yaml_path = os.path.join(tg_root, r'test_datas\excle_config')
excle_path = os.path.join(tg_root, r'test_datas\test_data1.xlsx')

class Handle_excle:
    def __init__(self):
        global sheet1
        try:
            excl = xlrd.open_workbook(excle_path)  # 打开excle文件
        except Exception:
            print("找不到文件")
        handle = HandleYaml()  # 读取yaml文件中的excl表名
        list_sheet = handle.load_yaml(excle_yaml_path)['sheet_name']
        sheet_name: str = ''.join(list_sheet)  # 转化为字符串
        sheet1 = excl.sheet_by_name(sheet_name)  # 通过sheet名查找

    def get_cell_value(self, xrow, xcol):
        """

        :type xrow: 第几行
        :type xcol: 第几列
        """
        cell_value = sheet1.cell_value(xrow, xcol)  # 取第xx行第xx列
        return cell_value

    def get_nrow(self):
        nrow = sheet1.nrows
        return nrow   #获取表的行数

    def get_ncol(self):
        ncol = sheet1.ncols
        return ncol   #获取表的列数

    def row_datas(self, row):
        # 获取excle中某一行数据
        col_len = hand_excl.get_ncol()
        row_cell = sheet1.row_values(row, 1, col_len)
        return row_cell

hand_excl = Handle_excle()

data1 = [tuple(hand_excl.row_datas(j)) for j in range(1, (hand_excl.get_nrow()))]

