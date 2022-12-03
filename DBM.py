import pymysql as p


def getConnection():
    return p.connect(host='localhost', user='root', password='', database='blogger')


def addUser(t):
    db = getConnection()
    sql = 'insert into user values(%s,%s,%s,%s)'
    cr = db.cursor()
    cr.execute(sql, t)
    db.commit()
    db.close()


def addAuthor(t):
    db = getConnection()
    sql = 'insert into author values(%s,%s,%s,%s)'
    cr = db.cursor()
    cr.execute(sql, t)
    db.commit()
    db.close()





def checklgauthor(t):
    db = getConnection()
    sql = 'select email,password from author where email=%s'
    cr = db.cursor()
    cr.execute(sql, t[0])
    data = cr.fetchall()
    db.commit()
    db.close()
    return data


def checklguser(t):
    db = getConnection()
    sql = 'select email,password from user where email=%s'
    cr = db.cursor()
    cr.execute(sql, t[0])
    data = cr.fetchall()
    db.commit()
    db.close()
    return data


def addPost(t):
    db = getConnection()
    sql = 'insert into authorpost values(%s,%s,%s)'
    cr = db.cursor()
    cr.execute(sql, t)
    db.commit()
    db.close()


def selectAllpost():
    db = getConnection()
    sql = 'select * from authorpost'
    cr = db.cursor()
    cr.execute(sql)
    elist = cr.fetchall()
    db.commit()
    db.close()
    return elist


def deletePost(username):
    db = getConnection()
    sql = 'delete from authorpost where username=%s'
    cr = db.cursor()
    cr.execute(sql, username)
    db.commit()
    db.close()

def selectuserById(username):
    db = getConnection()
    sql = 'select * from authorpost where username=%s'
    cr = db.cursor()
    cr.execute(sql, username)
    elist = cr.fetchall()
    db.commit()
    db.close()
    return elist[0]


def updatePost(t):
    db = getConnection()
    sql = 'update authorpost set username=%s,blogtitle=%s,post=%s where username=%s'
    cr = db.cursor()
    cr.execute(sql, t)
    db.commit()
    db.close()

def selectpost():
    db = getConnection()
    sql = "select * from authorpost where username=%s"
    cr = db.cursor()
    user=("username",)
    cr.execute(sql,user)
    elist = cr.fetchall()
    db.commit()
    db.close()
    return elist

  
