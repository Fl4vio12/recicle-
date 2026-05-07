class Material:
    lista = [

        {
            "nome":"Papel",
            "icone":"📄",
            "dica":"Mantenha seco antes de reciclar."
        },

        {
            "nome":"Plástico",
            "icone":"🧴",
            "dica":"Lave as embalagens antes do descarte."
        },

        {
            "nome":"Vidro",
            "icone":"🍾",
            "dica":"Cuidado com vidro quebrado."
        },

        {
            "nome":"Metal",
            "icone":"🥫",
            "dica":"Latas podem ser recicladas."
        },

        {
            "nome":"Eletrônicos",
            "icone":"💻",
            "dica":"Leve para pontos especiais."
        }

    ]

    @classmethod
    def listar(cls):

        return cls.lista