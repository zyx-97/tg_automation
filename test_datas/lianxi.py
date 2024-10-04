import yaml

# 准备数据
data = {
    'name': '张三',
    'age': 30,
    'is_student': False,
    'hobbies': ['reading', 'traveling']
}

# 写入数据到YAML文件
with open('excle_config.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file, allow_unicode=True)

print("数据已成功写入")