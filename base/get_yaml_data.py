import yaml

class HandleYaml:
    # 读取yaml文件
    def load_yaml(self, file_name):
        if file_name == None:
            file_path = ""
        else:
            file_path = file_name
        try:
            with open(file_path, encoding='UTF-8') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)   #5.1及以上版本的写法
            return data
        except Exception:
            print("未找到yaml文件")
            return {}