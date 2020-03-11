# coding:utf-8
import pandas
from pyetl import Etl
from sqlalchemy.dialects.oracle import cx_oracle

storage_type_mapping= {
    "0":"文件系统",
    "1":"数据库类型"
}
db_driver_mapping = {
    "mysql": "pymysql",
    "oracle": "cx_oracle",
    "postgresql": "psycopg2",
    "mssql": "pyodbc",
    "sqlite": "",
}

class BaseConfig(object):
    def __init__(self, src_uri=None, dst_uri=None, src_placeholder="?", table_task='py_script_task', query_size=2000000,
                 insert_size=200000, new_table_field_default_size=200, debug=False):
        self.DEBUG = debug
        self.SRC_URI = src_uri
        # self.SRC_URI = "mysql+pymysql://root:root@localhost:3306/test"
        self.DST_URI = dst_uri
        # self.DST_URI = "mysql+pymysql://root:root@localhost:3306/test_dev"
        self.SRC_PLACEHOLDER = src_placeholder
        self.TASK_TABLE = table_task
        self.QUERY_SIZE = query_size
        self.INSERT_SIZE = insert_size
        self.NEW_TABLE_FIELD_DEFAULT_SIZE = new_table_field_default_size


class EtlConfig(BaseConfig):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PrivateEtl(Etl):
    def __init__(self, src_tab, dst_tab):
        super().__init__(src_tab, dst_tab)


    def get_src_tab_create_info(self):
        sql, _ = self._gen_sql(None, None)
        iter_df = pandas.read_sql(
            sql, self.src_obj.connect,
            chunksize=self._query_count)
        sql = "show create table %s"%self.src_tab
        create_sql = self.src_obj.read(sql)
        return create_sql[0][1] if create_sql else None


    def create_dst_tab(self, create_sql):
        try:
            if self.dst_obj.exist_table(self.src_tab):
                return True
            if create_sql:
                self.dst_obj.insert(create_sql)
            else:
                return False
        except Exception:
            return False
        return True


def task(*args, **kwargs):

    # src_tab = "menu"
    # src_update = "SRC_UPDATE_FIELD"
    # dst_tab = "menu"
    # dst_unique = "DST_UNIQUE"
    # mapping = {
    #     "ID": "CODE"
    # }
    def get_db_tables(db_name):
        sql = ""

    def get_uri(**kwargs):
        db_type = kwargs.get('db_type', None)
        driver = db_driver_mapping.get(db_type)
        username = kwargs.get('username', None)
        password = kwargs.get('password', None)
        host = kwargs.get('host', None)
        port = kwargs.get('port', None)
        db_name = kwargs.get('db_name', None)

        storage_type = kwargs.get('storage_type')

        if storage_type == '0':
            uri_str = src_dict.get('path')
        else:
            if db_type == 'sqlite':
                uri_str = "%s%s://" % (db_type, driver)
            else:
                uri_str = '%s+%s://%s:%s@%s:%s/%s' % (db_type, driver, username, password, host, port, db_name)

        return uri_str

    src_dict = args[0]
    dst_dict = args[1]
    src_uri = get_uri(**src_dict)
    dst_uri = get_uri(**dst_dict)
    src_tab = kwargs.get('src_tab', None)
    dst_tab = kwargs.get('dst_tab', None)

    app = PrivateEtl(src_tab, dst_tab,
                     #   mapping=mapping,
                     #   updte=src_update,
                     #   unique=dst_unique
                     )
    # src_uri = "mysql+pymysql://root:root@localhost:3306/test"
    # dst_uri = "mysql+pymysql://root:root@localhost:3306/test"
    app.config(EtlConfig(debug=True, src_uri=src_uri, dst_uri=dst_uri))
    is_created = app.create_dst_tab(app.get_src_tab_create_info())
    if is_created:
        app.dst_tab=app.src_tab

    conditions = "pid=0"
    app.run(where=conditions, groupby=None, days=None)


def test_db_sql():
    a = Etl(None, None)
    b = a._connect("oracle+cx_oracle://sys:x09W4eof71@localhost:1521/orcl?mode=SYSDBA")
    b.read("select * from user_tables")
    print(b)

if __name__ == '__main__':
    # args = ({"db_type":'mysql', "storage_type":1, "username":'root',"password":'root',"host":'localhost',"port":'3306', "db_name":'test'},
    #         {"db_type":'mysql', "storage_type":1, "username":'root',"password":'root',"host":'localhost',"port":'3306', "db_name":'test_dev'})
    # task(*args, src_tab="menu")
    import cx_Oracle
    # # "load/123456@localhost/ora11g"
    # conn = cx_Oracle.connect("sys/x09W4eof71@localhost/orcl",mode=cx_Oracle.SYSDBA)
    # c = conn.cursor()
    # x = c.execute('select * from user_tables')

    from sqlalchemy import Column, String, Integer, DateTime, create_engine
    test_db_sql()
