window.onload = function () {

    var mapa = L.map("mapa").setView([-5.09, -42.80], 13);

    L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
    ).addTo(mapa);


    /* pontos */

    var p1 = L.marker([-5.09, -42.80])
        .addTo(mapa)
        .bindPopup("Ponto Centro - plastico");

    p1.tipo = "plastico";


    var p2 = L.marker([-5.08, -42.79])
        .addTo(mapa)
        .bindPopup("Ponto Sul - papel");

    p2.tipo = "papel";


    var p3 = L.marker([-5.10, -42.82])
        .addTo(mapa)
        .bindPopup("Ponto Norte - vidro");

    p3.tipo = "vidro";


    var lista = [p1, p2, p3];


    /* filtro */

    window.irFiltro = function (tipo) {

        for (var i = 0; i < lista.length; i++) {

            mapa.removeLayer(lista[i]);

            if (tipo == "todos" || lista[i].tipo == tipo) {
                lista[i].addTo(mapa);
            }

        }

    }


    /* localização */

    if (navigator.geolocation) {

        navigator.geolocation.getCurrentPosition(function (pos) {

            var lat = pos.coords.latitude;
            var lng = pos.coords.longitude;

            mapa.setView([lat, lng], 14);

            L.marker([lat, lng])
                .addTo(mapa)
                .bindPopup("Você está aqui")
                .openPopup();

        });

    }

}