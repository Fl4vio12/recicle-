class Ranking:

    lista = [

        {"nome":"Flavio", "pontos":150},
        {"nome":"Ana", "pontos":120},
        {"nome":"Carlos", "pontos":90},
        {"nome":"Marcos", "pontos":70},
        {"nome":"Luan", "pontos":50}

    ]


    @classmethod
    def listar(cls):
        return cls.lista