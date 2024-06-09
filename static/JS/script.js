function toggleEdit() {
    var displayElement = document.getElementById("display");
    var editElement = document.getElementById("edit");
    if (displayElement.style.display === "none") {
        displayElement.style.display = "block";
        editElement.style.display = "none";
    } else {
        displayElement.style.display = "none";
        editElement.style.display = "block";
    }
}


function rota_deletar() {
    window.location.href = "/perfil/deletar";
}

// Função para obter parâmetros de consulta da URL
function getQueryParams() {
    const params = {};
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    urlParams.forEach((value, key) => {
      params[key] = value;
    });
    return params;
  }

// Preencher o campo 'nome' com o valor do parâmetro de consulta
document.addEventListener("DOMContentLoaded", () => {
    const params = getQueryParams();
    if (params.elemento) {
      document.getElementById('nome').value = params.elemento;
    }
  });