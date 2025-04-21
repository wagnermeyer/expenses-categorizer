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

Para filtrar despesas por uma categoria específica:

```
python main.py caminho/para/despesas.json CATEGORIA
```

### Categorias Disponíveis

- `1` - SUPERMERCADO
- `2` - ALIMENTAÇÃO
- `3` - SAÚDE
- `4` - BEBÊ
- `q` - TRANSPORTE
- `w` - LAZER/HOBBY
- `e` - JUROS/MULTAS/TAXAS
- `r` - SAÚDE
- `a` - FILHOS
- `s` - PRESENTES/DOAÇÕES
- `d` - PESSOAIS
- `f` - VIAGENS
- `z` - DESCONHECIDO
- `x` - OUTROS
- `/` - Sair

### Navegação

- Seta para cima: Voltar para a despesa anterior
- Seta para baixo: Avançar para a próxima despesa
- Teclas de categoria: Atribuir a categoria correspondente à despesa atual

### Interface

A interface do programa mostra:
- O número da despesa atual e o total de despesas
- A data da despesa
- A descrição da despesa
- O valor da despesa
- A categoria atual (se já foi atribuída)
- Um menu com todas as categorias disponíveis e seus atalhos de teclado

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

## Salvamento Automático

O programa salva automaticamente as alterações no arquivo JSON original após cada categorização, garantindo que nenhuma informação seja perdida.

## Dicas de Uso

1. **Categorização Rápida**: Use os atalhos de teclado para categorizar despesas rapidamente.
2. **Filtragem**: Use o filtro por categoria para revisar ou corrigir categorizações específicas.