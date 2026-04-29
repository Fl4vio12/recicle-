class Ponto:

    lista = [

        {
            "nome":"Ponto Centro",
            "tipo":"plastico",
            "lat":-5.09,
            "lng":-42.80
        },

        {
            "nome":"Ponto Sul",
            "tipo":"papel",
            "lat":-5.08,
            "lng":-42.79
        },

        {
            "nome":"Ponto Norte",
            "tipo":"vidro",
            "lat":-5.10,
            "lng":-42.82
        }

    ]


    @classmethod
    def listar(cls):
        return cls.lista


    @classmethod
    def filtro(cls, tipo):

        nova = []

        for item in cls.lista:

            if item["tipo"] == tipo:
                nova.append(item)

        return nova