import pymysql as sql

def ConnectionPooling():
    db=sql.connect(host='localhost',port=3306,user='root',passwd='123',db='medassist_ecom',cursorclass=sql.cursors.DictCursor)
    # db is an Object Which Hold the Database Engine Address
    cmd=db.cursor()
    return db,cmd




