import mysql.connector
from database import Database
from usuario import Usuario

class UsuarioDAO:
    def inserir(self, usuario: Usuario):
        conn = Database.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (nome, email, senha, tipo, telefone, cidade, estado) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (usuario.nome, usuario.email, usuario.senha, usuario.tipo, usuario.telefone, usuario.cidade, usuario.estado)
        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()
