from django.db import connection
from django.http import JsonResponse

# Create your views here.

from django.views import View

from common import es_


# 在数据库初始化时，同步把数据库中表的数据添加到索引中
class ESView(View):

    def async_es(self, *tables, **kwargs):
        print(tables)
        for table_name in tables:
            es_.remove_index('%s_index' % table_name)
            es_.create_index('%s_index' % table_name)
            columns = kwargs[table_name]

            sql1 = 'select count(*) from %s' % table_name
            sql = 'select %s from %s' % (','.join(columns), table_name)
            c = connection.cursor()

            c.execute(sql1)
            print(c.fetchone(), table_name)
            c.execute(sql)
            for row in c.fetchall():
                doc = {name: row[i] for i, name in enumerate(columns)}
                es_.add_doc(doc, table_name)

            c.close()

    def get(self, request):
        # 同步ES(初始化)
        self.async_es('goods', 'news', 'user',
                      goods=['id', 'name', 'address', 'price'],
                      news=['id', 'title', 'author'],
                      user=['id', 'name', 'phone'])

        return JsonResponse({
            'status': 0,
            'msg': '同步ElasticSearch搜索引擎成功'
        })


# 查询ES引擎中的数据：
class ESSearchView(View):
    def get(self, request):
        es_.search()    # 查询索引
        data = request.GET
        print(data)

        return JsonResponse({
            'status': 0,
            'msg': '查询数据成功'
        })


# 上传日志：
class ESLogView(View):
    def post(self, request):
        data = request.POST
        print(data)

        return JsonResponse({
            'status': 0,
            'msg': '上传日志成功'
        })

