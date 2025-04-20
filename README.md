# Categorizador de Despesas

Uma ferramenta simples para categorizar despesas de extratos de cartão de crédito.

## Descrição

Este programa permite categorizar despesas a partir de um arquivo JSON contendo transações. Ele apresenta cada despesa e permite atribuir uma categoria predefinida através de atalhos de teclado.

## Requisitos

- Python 3.6+
- Biblioteca `readchar`

## Instalação

1. Clone este repositório:
```
git clone https://github.com/seu-usuario/expenses-categorizer.git
cd expenses-categorizer
```

2. Instale as dependências:
```
pip install readchar
```

## Uso

Execute o programa passando o caminho para o arquivo JSON de despesas:

```
python main.py caminho/para/despesas.json
```

### Categorias Disponíveis

- `1` - SUPERMERCADO
- `2` - ALIMENTAÇÃO
- `3` - SAÚDE
- `4` - ARTHUR
- `q` - ASSINATURAS
- `w` - HOBBY
- `e` - CACHORROS
- `r` - PRESENTES
- `a` - DESCONHECIDO
- `s` - TRANSPORTE
- `d` - CASA
- `f` - VIAGEM
- `z` - TAXAS
- `x` - OUTROS
- `/` - Sair

### Navegação

- Seta para cima: Voltar para a despesa anterior
- Seta para baixo: Avançar para a próxima despesa

## Formato do Arquivo JSON

O arquivo JSON deve conter uma lista de despesas, onde cada despesa é um objeto com os seguintes campos:

```json
{
  "date": "DD/MM",
  "description": "Descrição da despesa",
  "price": "Valor da despesa"
}
```

Após categorizar uma despesa, o campo `manual_category` será adicionado ao objeto.

## Integração com Parser de Fatura

Este programa pode ser usado em conjunto com o [Parser de Fatura Itaú](https://github.com/seu-usuario/fatura-itau-parser) para extrair e categorizar despesas de faturas de cartão de crédito.