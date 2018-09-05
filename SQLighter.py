# -*- coding: utf-8 -*-
import sqlite3

class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database,check_same_thread=False)
        self.cursor = self.connection.cursor()

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM books').fetchall()

    def select_single(self, id):
        """ Получаем одну строку с номером name """
        with self.connection:
            try:
                return self.cursor.execute('SELECT * FROM Users WHERE name = ?', (id,)).fetchall()[0]
            except LookupError:
                lm=''
                return(lm) 
    def insert_string(self,botid,name):
        al = [botid,name]
        with self.connection:
            return self.cursor.execute("INSERT INTO Users VALUES (?,?)",al)
    def search(self, dbid):
        with self.connection:
            return self.cursor.execute('SELECT * FROM books WHERE id = ?', (dbid,)).fetchall()[0]

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM Users').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()

    def check_username(self,uname):
#        idsum = self.count_rows()
#        i=1
         gg=False
         try:
             ll = self.cursor.execute('SELECT * FROM Users WHERE name = ?', (uname,)).fetchall()[0]
             if ll[1] != '':
                 gg=True
                 return(gg)
         except LookupError:
             gg=False
             return(gg)
#        while i<=idsum:
#            i=i+1            
#            if  hg == name:
#                gg=True
#                break
    def get_balance(self,uname):
        ll = self.cursor.execute('SELECT * FROM Users WHERE name = ?', (uname,)).fetchall()[0]
        return(ll[2])
    def get_quest(self):
        ll = self.cursor.execute('SELECT * FROM Tasks')
    def add_user_inf(self,name):
        if self.check_username(name)==False:
            idsum = self.count_rows()
            iddb = idsum +1
            st = self.insert_string(iddb,name)


            


