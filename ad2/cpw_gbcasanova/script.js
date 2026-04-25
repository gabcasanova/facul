// Janela
function abrirJanela(idDoModal) {
    document.getElementById(idDoModal).style.display = 'block';
}

function fecharJanela(idDoModal) {
    document.getElementById(idDoModal).style.display = 'none';
}

// Descrição dos Produtos
const bancoProdutos = {
    "pedigree": {
        titulo: "Pedigree",
        imagem: "img/RaçãoPedigree90.jpg",
        sabor: "Sabor Carne",
        peso: "10kg",
        preco: "R$100,00"
    },
    "aipo": {
        titulo: "Purina Aipo",
        imagem: "img/RaçãoAipo90.jpg",
        sabor: "Sabor Carne e Frango",
        peso: "10kg",
        preco: "R$130,00"
    },
    "gran": {
        titulo: "GranPlus Choice",
        imagem: "img/RaçãoGranPlus90.jpg",
        sabor: "Sabor Carne e Frango",
        peso: "10kg",
        preco: "R$130,00"
    },
    "osso": {
        titulo: "JAMBO PET",
        imagem: "img/BrinquedoJambo90.jpg",
        sabor: "Osso Silicone",
        peso: "",
        preco: "R$25,00"
    },
};

function mudarDescricao(nomeDoProduto) {
    const info = bancoProdutos[nomeDoProduto];

    if (info) {
        document.getElementById("descTitulo").innerText = info.titulo;
        document.getElementById("descImagem").src = info.imagem;
        document.getElementById("descSabor").innerText = info.sabor;
        document.getElementById("descPeso").innerText = info.peso;
        
        document.getElementById("valorPreco").innerText = info.preco;
    }
}



