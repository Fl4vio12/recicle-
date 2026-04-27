async function cadastrar() {
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;

    const resposta = await fetch("/api/cadastro", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ nome, email, senha })
    });

    const dados = await resposta.json();

    if (dados.status === "ok") {
        window.location.href = "/login";
    } else {
        document.getElementById("erro").innerText = dados.mensagem;
    }
}