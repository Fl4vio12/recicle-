async function login() {
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;

    const resposta = await fetch("/api/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, senha })
    });

    const dados = await resposta.json();

    if (dados.status === "ok") {
        window.location.href = "/mapa";
    } else {
        document.getElementById("erro").innerText = dados.mensagem;
    }
}