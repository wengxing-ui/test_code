import yaml
def getParams(fileName):
    dataList = []
    try:
        with open(fileName, "r", encoding="UTF-8") as f:
            conText = yaml.load_all(f, Loader=yaml.FullLoader)
            for i in conText:
                dataList.append(i)
    except Exception as e:
        print('获取{}数据失败!'.format(fileName))
        raise e
    else:
        return dataList
