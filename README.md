
# 🧩 Desafio prático — Particionador de IDs por Shard (A/B)

## Contexto
Você trabalha em um e-commerce que, para **escalar o banco de dados**, distribui pedidos entre **dois shards**:
- **Shard A** recebe IDs **pares**
- **Shard B** recebe IDs **ímpares**

Seu time quer uma **ferramenta de linha de comando** simples para simular essa distribuição com base em um lote de **20 IDs de pedido**.

---

## Tarefa
Crie um programa que:
1. Leia **20 números inteiros** (IDs de pedido) e armazene numa **lista** principal.
2. Separe os IDs **pares** em uma **lista PAR (Shard A)** e os **ímpares** em uma **lista ÍMPAR (Shard B)**.
3. **Imprima as três listas** (entrada, PAR, ÍMPAR) **mantendo a ordem de entrada**, e mostre o **total** em cada shard.

> 💡 Dica de domínio: esse tipo de lógica é a base de **particionamento** (sharding) e **balanceamento de carga** por chave — comuns em sistemas reais.

---

## Requisitos (aceite)
- Ler **exatamente 20** números inteiros do usuário.
- Considerar **0** como **par**.
- **Manter a ordem** dos itens em cada lista.
- Exibir:
  - Lista original
  - Lista PAR (Shard A) + contagem
  - Lista ÍMPAR (Shard B) + contagem
- Implementar uma **função pura** `separar_pares_impares(lista)` para facilitar testes.

---

## 🔎 Exemplo de execução
```
=== Particionador de IDs por Shard (A/B) ===

Digite o 1º ID: 1024
Digite o 2º ID: 77
...
Digite o 20º ID: 0

Lista (entrada): [1024, 77, ..., 0]
Shard A (PAR): [1024, ..., 0]  | total: 10
Shard B (ÍMPAR): [77, ...]     | total: 10
```

---

## 💻 Como executar

**Pré‑requisito:** Python **3.8+**

1) Clone este repositório ou baixe os arquivos.
```bash
git clone https://github.com/seu-usuario/projeto-fabrica-7.git
cd projeto-fabrica-7
```

2) No terminal, rode:
```bash
python projeto-fabrica-7.py
```
> **Windows:** se `python` não funcionar, tente `py projeto-fabrica-7.py`.

---

## 🧠 Conceitos trabalhados
- Leitura com `input()` e conversão para `int`
- **Listas** e preservação de **ordem de entrada**
- Operador de resto (`%`) para particionar por **par/ímpar**
- Função pura para facilitar **testes e reuso**

---

## 🚀 Extensões sugeridas
- **N sob demanda**: permitir que o usuário informe a quantidade de IDs.
- **Validação**: impedir duplicados ou avisar sobre negativos (se for política da empresa).
- **Métricas**: exibir **percentual** distribuído em cada shard.
- **Persistência**: salvar as três listas em um `.txt` ou `.csv`.
- **Testes**: expandir `tests/test_particionador.py` com mais cenários.

---

## 📂 Estrutura
```
projeto-fabrica-7/
├─ particionador_shards.py
├─ README.md
├─ tests/
│  └─ test_particionador.py
└─ LICENSE
```

---

## 📝 Licença
Este projeto está sob licença **MIT** — use, adapte e compartilhe. ✨
