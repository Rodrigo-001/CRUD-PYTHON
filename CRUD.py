# AULA 16/10 - Conexão com o banco de dados Oracle e CRUD

# importar oracledb
import oracledb


def getConnection():
    '''
    Desc: Conecta ao banco de dados Oracle
    Return: conn (objeto de conexão)
    '''
    try:
        conn = oracledb.connect(user="xxxxxxx", password="xxxxxx", host="oracle.fiap.com.br", port=1521, service_name="ORCL")
    except Exception as e:
        print(f'Erro ao obter conexão: {e}')        
    return conn

def createTable():
    '''
    Desc: Cria a tabela CEO_DETAILS
    Return: None
    '''
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql_create = """
        CREATE TABLE CEO_DETAILS(
            FIRST_NAME VARCHAR2(50),
            LAST_NAME VARCHAR2(50),
            COMPANY VARCHAR2(50),
            AGE NUMBER
        )
        """
        cursor.execute(sql_create)
        print('Tabela criada!')
    except Exception as e:
        print(f'Erro ao criar tabela: {e}')

def select():
    '''
    Desc: Executa um select na tabela CEO_DETAILS
    Return: None
    '''
    # tratamento de exceção
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql_select = 'SELECT * FROM CEO_DETAILS'
        cursor.execute(sql_select)
        # percorrer as linhas da tabela
        i = 1  
        for result in cursor: 
            print(f'\nlinha {i}: {result}')
            i += 1
    except Exception as e:
        print(f'Erro ao executar select: {e}')

def insert():
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql_insert = "INSERT INTO CEO_DETAILS VALUES ('Jeff', 'Bezos', 'Amazon', 56)"
        cursor.execute(sql_insert)
        conn.commit()
        print('\nDados inseridos com sucesso!\n')
    except Exception as e:
        print(f'Erro ao executar insert: {e}')
    
def update():
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql_update = "UPDATE CEO_DETAILS SET AGE = 77 WHERE FIRST_NAME = 'Jeff'"  
        cursor.execute(sql_update)
        conn.commit()
        print('\nDados atualizados com sucesso!\n')
    except Exception as e:
        print(f'Erro ao executar update: {e}')

def delete():
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql_delete = "DELETE FROM CEO_DETAILS WHERE FIRST_NAME = 'Jeff'"
        cursor.execute(sql_delete)
        conn.commit()
        print('\nDados deletados com sucesso!\n')
    except Exception as e:
        print(f'Erro ao executar delete: {e}')
    

def closeConnection(conn):
    '''
    Desc: Fecha a conexão com o banco de dados
    Return: None
    '''
    try:
        conn.close()
        print('\nConexão fechada com sucesso!')
    except Exception as e:
        print(f'Erro ao fechar conexão: {e}')

#Principal
conn = getConnection()

# print('\nINSERINDO DADOS NA TABELA:')
# insert()

# print('\nATUALIZANDO DADOS DA TABELA:')
# update()

print('\nDELETANDO DADOS DA TABELA:')
delete()

print('CONSULTANDO DADOS DA TABELA:')
select()
closeConnection(conn)