function cadastrar() {

    var nome = document.getElementById("nome").value.trim();
    var email = document.getElementById("email").value.trim();
    var senha = document.getElementById("senha").value.trim();

    if (nome == "" || email == "" || senha == "") {
        alert("Preencha todos os campos");
        return;
    }

    document.getElementById("formCad").submit();

}