# database.py - Configuração e conexão com o banco
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'aproximati'  # Nome do seu banco
        self.user = 'root'
        self.password = ''  # Senha padrão do XAMPP ta vazia
        self.connection = None
    
    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Conexão com MySQL estabelecida!")
                return True
        except Error as e:
            print(f"Erro ao conectar com MySQL: {e}")
            return False
    
    def desconectar(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão MySQL encerrada")
    
    def executar_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            return cursor
        except Error as e:
            print(f"Erro ao executar query: {e}")
            return None
    
    def buscar_dados(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return []

# Instância global do banco
db = Database()