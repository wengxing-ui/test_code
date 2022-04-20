import pymysql
class ConDB:
    cur, con = None,None
    @classmethod
    def con_db(cls,host='localhost', user='root', passwd='', port=3306, db='', charset='utf8'):
        """连接数据库，返回游标和数据库连接对象"""
        try:
            cls.con = pymysql.connect(host=host, user=user, passwd=passwd,
                                      port=port, db=db, charset=charset)
            cls.cur = cls.con.cursor()  # 创建游标对象
        except Exception as e:
            print(e)
    @classmethod
    def close(cls):
        """关闭数据库连接"""
        cls.cur.close()
        cls.con.close()

    @classmethod
    def select_one(cls,sql):
        """获取select语句查询结果的一个值"""
        cls.cur.execute(sql)
        return cls.cur.fetchone()

    @classmethod
    def select_all(cls,sql):
        """获取select语句查询结果的所有值"""
        cls.cur.execute(sql)
        return cls.cur.fetchall()

    @classmethod
    def dml(cls,sql):
        """执行dml操作，提交事务"""
        cls.cur.execute(sql)
    @classmethod
    def commit(cls):
        """提交事务"""
        cls.con.commit()


