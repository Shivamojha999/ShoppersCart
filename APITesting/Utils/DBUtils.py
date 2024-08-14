import pymysql
from pymysql.cursors import DictCursor
from APITesting.Utils.RequestInterface import Request

class DBUtils(Request):

    '''
    created By: Shivam Ojha
    since: 11 August 2024
    desc: This method is used to create Db Connection
    param: user,password,port,host
    return: connection
    '''
    def createDbConnection(self):
        connection = pymysql.connect(user=self.dbParameters['user'],password=self.dbParameters['password'],
                                     port=int(self.dbParameters['port']),host=self.dbParameters['host'],database=self.dbParameters['dataBase'])
        return connection

    '''
    created By: Shivam Ojha
    since: 11 August 2024
    desc: This method is used to execute Select Sql Query
    param: sqlQuery
    return: list Of dict
    '''
    def executeSelectSqlQuery(self,sqlQuery):
        connection = self.createDbConnection()
        try:
            dbCursor = connection.cursor(pymysql.cursors.DictCursor)
            dbCursor.execute(sqlQuery)
            dbResponse = dbCursor.fetchall()
            dbCursor.close()
        except Exception as e:
            raise Exception(f"Failed running {sqlQuery}, Error: {str(e)}")
        finally:
            connection.close()
        return dbResponse

    '''
    created By: Shivam Ojha
    since: 14 August 2024
    desc: This method is used to execute Non Select Sql Query
    param: sqlQuery
    return: int
    '''
    def executeNonSelectSqlQuery(self, sqlQuery):
        connection = self.createDbConnection()
        try:
            dbCursor = connection.cursor()
            dbCursor.execute(sqlQuery)
            connection.commit()
            rowsAffected = dbCursor.rowcount
            dbCursor.close()
        except Exception as e:
            connection.rollback()
            raise Exception(f"Failed running {sqlQuery}, Error: {str(e)}")
        finally:
            connection.close()
        return rowsAffected
