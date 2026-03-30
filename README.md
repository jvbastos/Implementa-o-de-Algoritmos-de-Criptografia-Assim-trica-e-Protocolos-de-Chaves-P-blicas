# 🔐 Implementação do Algoritmo RSA em Python

## 📌 Autor
João Vítor Resende Bastos  
Curso: Análise e Desenvolvimento de Sistemas – IFTM  

---

## 📖 Introdução

Este projeto tem como objetivo implementar o algoritmo de criptografia assimétrica RSA (Rivest-Shamir-Adleman) de forma manual, sem o uso de bibliotecas criptográficas prontas.

A proposta consiste em desenvolver todo o ciclo de funcionamento do RSA, incluindo a geração de chaves, cifragem e decifragem de mensagens, demonstrando na prática o conceito de confidencialidade na segurança da informação.

---

## 🎯 Objetivo

- Implementar o algoritmo RSA do zero;
- Gerar chaves públicas e privadas;
- Cifrar mensagens utilizando a chave pública;
- Decifrar mensagens utilizando a chave privada;
- Demonstrar o funcionamento da criptografia assimétrica.

---

## ⚙️ Funcionamento do RSA

### 1. Geração das chaves

1. Escolhem-se dois números primos grandes:
   - p e q

2. Calcula-se:
   - n = p × q
   - φ(n) = (p - 1)(q - 1)

3. Escolhe-se um número e tal que:
   - 1 < e < φ(n)
   - MDC(e, φ(n)) = 1

4. Calcula-se d:
   - d ≡ e⁻¹ mod φ(n)

---

### 2. Chaves geradas

- Chave pública: (e, n)
- Chave privada: (d, n)

---

### 3. Cifragem

A mensagem é convertida em números e cifrada:

c = m^e mod n

---

### 4. Decifragem

A mensagem original é recuperada:

m = c^d mod n

---

## 🔢 Conceitos Matemáticos

### Números Primos
São números divisíveis apenas por 1 e por eles mesmos.

### Aritmética Modular
Trabalha com restos de divisão.

Exemplo:
17 mod 5 = 2

### Totiente de Euler
Representa a quantidade de números coprimos com n.

φ(n) = (p-1)(q-1)

### Algoritmo de Euclides Estendido
Utilizado para calcular o inverso modular (valor de d).

---

## 🖥️ Implementação

O sistema foi desenvolvido em Python e inclui:

- Geração de primos (Miller-Rabin)
- Cálculo do inverso modular
- Conversão de texto para blocos numéricos
- Cifragem e decifragem com exponenciação modular

---

## ▶️ Como Executar

```bash
python rsa.py
