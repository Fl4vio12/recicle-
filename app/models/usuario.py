from app.models.db import conectar


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


    def salvar(self):

        conn = conectar()

        conn.execute(
            "INSERT INTO usuarios(nome,email,senha) VALUES(?,?,?)",
            (self.nome, self.email, self.senha)
        )

        conn.commit()
        conn.close()


    def entrar(self):

        conn = conectar()

        usuario = conn.execute(
            "SELECT * FROM usuarios WHERE email=? AND senha=?",
            (self.email, self.senha)
        ).fetchone()

        conn.close()

        return usuario