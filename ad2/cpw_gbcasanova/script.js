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

// CPF
function calculaDV(num) {
    var resto = 0, soma = 0;
    for (i = 2; i < 11; i++) {
        soma = soma + ((num % 10) * i);
        num = parseInt(num / 10);
    }
    resto = (soma % 11);
    return (resto > 1) ? (11 - resto) : 0;
}

function validarCPF() {
    var cpfInput = document.getElementById("cpf").value;

    if (isNaN(cpfInput)) {
        alert("O CPF deve ter apenas números");
        return;
    }

    if (cpfInput.length !== 11) {
        alert("O CPF deve ter 11 dígitos!");
        return;
    }

    var identCPF = parseInt(cpfInput.substring(0, 9));
    
    var dvDigitado = parseInt(cpfInput.substring(9, 11));

    var primeiro_digito = calculaDV(identCPF);
    var segundo_digito = calculaDV(identCPF * 10 + primeiro_digito);
    
    var dvCalculado = (primeiro_digito * 10) + segundo_digito;

    if (dvDigitado !== dvCalculado) {
        alert("Dígitos verificadores incorretos!");
        return;
    }
}

// Adicionar produto
const precosProdutos = {
    "pedigree": 100.00,
    "purina": 130.00,
    "granplus": 130.00,
    "jambo": 25.00
};

function adicionarProduto() {
    var combo = document.getElementById("produtos");
    var lista = document.getElementById("listaCompras");
    var campoValor = document.getElementById("valor");

    if (combo.value === "") {
        alert("Nnehum produto selecionado!");
        return;
    }

    var nomeProduto = combo.options[combo.selectedIndex].text;
    var valorProduto = precosProdutos[combo.value];

    if (lista.value !== "") {
        lista.value += "\n" + nomeProduto;
    } else {
        lista.value = nomeProduto;
    }

    var valorAtual = parseFloat(campoValor.value);
    var novoValorTotal = valorAtual + valorProduto;
    campoValor.value = novoValorTotal.toFixed(2); 
    
    combo.selectedIndex = 0;
}