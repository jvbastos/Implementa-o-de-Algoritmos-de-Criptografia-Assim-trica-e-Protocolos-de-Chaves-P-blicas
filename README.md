# Implementação do Algoritmo RSA em Python

## Descrição

Este projeto apresenta uma implementação completa do algoritmo de criptografia assimétrica RSA (Rivest-Shamir-Adleman), desenvolvida manualmente em Python, sem o uso de bibliotecas de criptografia prontas.

O sistema realiza todo o ciclo de vida do RSA:

- geração de números primos grandes;
- cálculo do módulo `n = p * q`;
- cálculo do totiente de Euler `φ(n) = (p - 1)(q - 1)`;
- escolha do expoente público `e`;
- cálculo do expoente privado `d` por meio do algoritmo de Euclides estendido;
- cifragem da mensagem com a chave pública;
- decifragem da mensagem com a chave privada.

Além disso, o programa converte automaticamente textos para blocos numéricos compatíveis com a aritmética modular exigida pelo algoritmo.

---

## Fundamentação Teórica

### 1. Criptografia Assimétrica

A criptografia assimétrica utiliza duas chaves diferentes:

- **Chave pública**: usada para cifrar a mensagem;
- **Chave privada**: usada para decifrar a mensagem.

No RSA, a segurança está baseada na dificuldade computacional de fatorar números inteiros muito grandes, especialmente o produto de dois números primos grandes.

---

### 2. Números Primos

Um número primo é um número natural maior que 1 que possui exatamente dois divisores positivos: 1 e ele mesmo.

Exemplos:
- 2, 3, 5, 7, 11, 13...

No RSA, escolhem-se dois primos grandes `p` e `q`. Esses valores são mantidos em segredo.

---

### 3. Módulo e Aritmética Modular

A aritmética modular trabalha com restos de divisão.

Exemplo:
`17 mod 5 = 2`

Isso significa que, ao dividir 17 por 5, o resto é 2.

No RSA, as operações principais são feitas com exponenciação modular:

`c = m^e mod n`

onde:
- `m` é a mensagem em forma numérica;
- `e` é o expoente público;
- `n` é o módulo.

Na decifragem:

`m = c^d mod n`

onde:
- `d` é o expoente privado.

---

### 4. Totiente de Euler

Após escolher os primos `p` e `q`, calcula-se:

`n = p * q`

e

`φ(n) = (p - 1)(q - 1)`

O valor `φ(n)` é fundamental para determinar a relação entre a chave pública e a chave privada.

---

### 5. Escolha de `e`

O valor `e` deve satisfazer:

- `1 < e < φ(n)`
- `mdc(e, φ(n)) = 1`

Ou seja, `e` deve ser coprimo de `φ(n)`.

Na prática, costuma-se usar `e = 65537`, pois é eficiente e seguro para implementações convencionais.

---

### 6. Cálculo de `d`

O valor `d` é o inverso modular de `e` em relação a `φ(n)`:

`d * e ≡ 1 (mod φ(n))`

Esse valor é calculado usando o **algoritmo de Euclides estendido**.

---

### 7. Funcionamento do RSA

#### Geração das chaves
1. Escolher dois primos grandes `p` e `q`;
2. Calcular `n = p * q`;
3. Calcular `φ(n) = (p - 1)(q - 1)`;
4. Escolher `e` tal que `mdc(e, φ(n)) = 1`;
5. Calcular `d`, o inverso modular de `e mod φ(n)`.

#### Chaves formadas
- **Chave pública**: `(e, n)`
- **Chave privada**: `(d, n)`

#### Cifragem
A mensagem numérica `m` é cifrada por:

`c = m^e mod n`

#### Decifragem
O texto cifrado `c` é recuperado por:

`m = c^d mod n`

---

## Observação importante

Esta implementação possui finalidade **acadêmica e didática**.

Embora represente corretamente a lógica matemática do RSA, ela **não é adequada para uso em produção real**, pois implementações seguras exigem mecanismos adicionais, como:

- padding seguro (ex.: OAEP);
- geradores criptograficamente seguros;
- proteção contra ataques práticos.

---

## Tecnologias utilizadas

- Python 3
- Bibliotecas padrão:
  - `random`
  - `math`

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/rsa-assimetrico.git
cd rsa-assimetrico
```

### 2. Execute o programa

```bash
python rsa.py
```

---

## Funcionalidades disponíveis no menu

- Gerar chaves RSA;
- Cifrar uma mensagem;
- Decifrar uma mensagem;
- Executar uma demonstração automática.

---

## Exemplo de uso

### Mensagem original
```text
RSA implementado manualmente com sucesso!
```

### Saída esperada
- geração de `p` e `q`;
- cálculo de `n`, `φ(n)`, `e`, `d`;
- mensagem cifrada em blocos numéricos;
- recuperação correta da mensagem original com a chave privada.

---

## Estrutura do projeto

```text
rsa-assimetrico/
├── rsa.py
└── README.md
```

---

## Autor

Projeto desenvolvido para fins acadêmicos, com foco na compreensão da criptografia assimétrica RSA e sua fundamentação matemática.
