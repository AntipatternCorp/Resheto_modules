import sqlite3

PATH_DEFAULLT = 'C:\Materials_temp\PyProj\Resheto_modules'

def connector(sql, path = PATH_DEFAULLT):
    with sqlite3.connect(path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        row = cursor.fetchone()
    return row

def set_field(table_name, field, key_field, key,path = PATH_DEFAULLT):
    sql = 'select '+str(field) +' from '+ str(table_name)+ ' where '+ str(key_field) + ' = ' + str(key)
    row = connector(sql, path)
    return row

def insert_data (table_name, data, path = PATH_DEFAULLT):
    sql = 'insert into ' + str(table_name) + ' values ( ' + str(data) + ' )'
    connector(sql,path)
    return True

def set_all (table_name, path = PATH_DEFAULLT):# список всех
    with sqlite3.connect(path) as conn:
        cursor = conn.cursor()
        cursor.execute('select * from '+str(table_name))
        rows = cursor.fetchall()
    return rows

def count (table_name, path = PATH_DEFAULLT):
    with sqlite3.connect(path) as conn:
        cursor = conn.cursor()
        cursor.execute('select count(*) from '+str(table_name))
        count_l = cursor.fetchall()
        count_l = count_l[0][0]
    return count_l

def drop_data (table_name, key_field, key,path = PATH_DEFAULLT):
    sql = 'delete from ' + str(table_name) +' where '+str(key_field) +' = ' + str(key)
    connector(sql,path)
    return True

def upd_field(table_name, field, value, key_field, key, path = PATH_DEFAULLT):
    sql = ''' UPDATE ?
              SET ? = ? 
              WHERE ? = ?'''
    args = (str(table_name), str(field), str(value), str(key_field), str(key))
    with sqlite3.connect(path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    return True
