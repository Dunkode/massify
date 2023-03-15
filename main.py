from src.dao.sqliteDAO import SqliteDAO
import src.utils.queryBuilder as qb
from tkinter import filedialog

if __name__ == "__main__":
    
    print("Selecione o diretório em que se encontra o Banco")
    directory = filedialog.askopenfilename()
    
    con = SqliteDAO(directory)

    print("Selecione arquivo em que se encontra a Query")
    query = filedialog.askopenfile().read()
    queryArgs = qb.requestQueryArgs()

    try:
        qtd = int(input("Digite a quantidade de linhas que devem ser criadas:\n"))
    except ValueError:
        print("Digite um valor válido!")
        quit()

    con.executeQuery(query, queryArgs, qtd)
    con.close()