import requests

HOST = "117.78.2.89"
PORT = 80  # 默认的是 9200

INDEX = 'yndoa'  # 索引库名


# 创建索引
def create_index(index_name='yndoa'):
    global INDEX
    INDEX = index_name
    url = f'http://{HOST}:{PORT}/{index_name}'
    json = {
        "settings": {
            "number_of_shards": 5,  # 主分片数量（默认一个索引被分配5个主分片）
            "number_of_replicas": 1  # 复制分片的数量（每个主分片都有一个复制分片）
        }
    }

    # 调用增加索引的接口
    resp = requests.put(url, json=json)
    print(resp.json())


# 删除索引
def remove_index(index_name=None):
    url = f'http://{HOST}:{PORT}/{index_name if index_name else INDEX}'
    resp = requests.delete(url)
    ret = resp.json()
    print(ret)


# 增加文档
def add_doc(doc: dict, doc_type: str):
    # dict 对象中不存在id的key时会抛出异常吗？ 会
    doc_id = doc.pop("id") if "id" in doc.keys() else None

    url = f'http://{HOST}:{PORT}/{INDEX}/{doc_type}' \
          + ("/" + str(doc_id) if doc_id else '')

    resp = requests.post(url, json=doc)
    ret = resp.json()
    if ret.get('result') == 'created':
        return True

    print(ret)
    return False


# 删除文档
def remove_doc(doc_type, doc_id):
    url = f'http://{HOST}:{PORT}/{INDEX}/{doc_type}/{doc_id}'
    resp = requests.delete(url)
    ret = resp.json()
    if ret.get('result') == 'deleted':
        print("删除成功")
        return True

    print("删除失败")
    return False


def search(keyword):
    url = f'http://{HOST}:{PORT}/_search?q={keyword}'
    resp = requests.get(url)
    ret = resp.json()
    hits = ret.get('hits').get('hits')
    if hits:
        datas = []
        for source in hits:
            source_ = source.get('_source')
            source_['id'] = source.get('_id')

            datas.append(source_)

        return datas  # 返回搜索后的数据


# 用于测试：
if __name__ == '__main__':
    doc = {
        'id': 1,
        'name': 'disen',
        'sex': '男',
        'age': 20
    }
    create_index()
    add_doc(doc, 'person')
    remove_doc('person', '1')
    remove_index()
    print(search("张"))
    create_index('abc3')
    add_doc({'id':1, 'title':'Python'}, 'course')
    add_doc({'id':2, 'title':'Python 3.6'},'course')
    add_doc({'id':3, 'title':'H5'},'course')
    print(search('Python'))
    remove_index('abc3')
