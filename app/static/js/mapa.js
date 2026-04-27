async function carregarPontos() {
    const resposta = await fetch("/api/pontos");
    const pontos = await resposta.json();

    const container = document.getElementById("map");
    container.innerHTML = "";

    if (pontos.length === 0) {
        container.innerHTML = "Nenhum ponto encontrado.";
        return;
    }

    pontos.forEach(p => {
        const div = document.createElement("div");

        div.innerHTML = `
            <strong>${p.nome}</strong><br>
            Tipo: ${p.tipo}<br>
            Latitude: ${p.lat}<br>
            Longitude: ${p.lng}
            <hr>
        `;

        container.appendChild(div);
    });
}

carregarPontos();