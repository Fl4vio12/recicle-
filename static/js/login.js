function entrar() {

    var email = document.getElementById("email").value.trim();
    var senha = document.getElementById("senha").value.trim();

    if (email == "" || senha == "") {
        alert("Preencha email e senha");
        return;
    }

    document.getElementById("formLogin").submit();

}