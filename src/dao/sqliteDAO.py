import sqlite3
import src.utils.queryBuilder as qb
from os.path import exists
import src.utils.logUtil as log
class SqliteDAO():
    def __init__(self, db_dir) -> None:
        self.db_dir = db_dir
        self.cursor = None

    def _connect(self):
        if exists(self.db_dir):
            try:
                self.cursor = sqlite3.connect(self.db_dir).cursor()
                print("Conexão realizada com sucesso!")
            except Exception as e:
                raise Exception("Erro ao conectar em banco de dados: " + e.args)
        else:
            raise Exception("O diretório informado para o banco de dados não existe!")
    
    def close(self):
        if self.cursor:
            self.cursor.close()

    def executeQuery (self, query : str, args : dict , qtdRows : int) -> None:
        try:
            self._connect()
            for i in range(0, qtdRows):
                for key in args.keys():
                    args[key] = str(int(args[key]) + i) 

                sql = qb.buildQuery(query, args)
                self.cursor.executescript(sql)
                
                log.printProgress(qtdRows, i)
        except sqlite3.Error as error:
            print("Erro ao executar a query: " + str(error.args))
        except Exception as cvtError:
            print("Erro ao atualizar a query: " + str(cvtError.args))