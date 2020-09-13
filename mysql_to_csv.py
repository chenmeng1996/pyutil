import pymysql
import csv
import os
"""
mysql导出csv
"""


def read_from_mysql():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        db='django_learn',
        password='3401231996',
        charset='utf8mb4'
    )
    cursor = conn.cursor()
    sql = 'select * from polls_choice'
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return data


def write_csv():
    data = read_from_mysql()
    filename = 'data/mysql.csv'
    # 获取文件夹路径，不存在则创建文件夹
    path = filename[0:filename.rfind('/')]
    if not os.path.exists(path):
        os.makedirs(path)
    # 写入csv文件，不存在则创建
    with open(filename, mode='w', encoding='utf-8') as f:
        write = csv.writer(f, dialect='excel')
        for item in data:
            write.writerow(item)

if __name__ == '__main__':
    write_csv()