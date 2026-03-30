import random
from math import gcd

# ============================================================
# IMPLEMENTAÇÃO EDUCACIONAL DO RSA
# Sem uso de bibliotecas de criptografia prontas
# ============================================================


def egcd(a, b):
    """
    Algoritmo de Euclides Estendido.
    Retorna (g, x, y) tal que:
        a*x + b*y = g = mdc(a, b)
    """
    if b == 0:
        return a, 1, 0

    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def mod_inverse(e, phi):
    """
    Calcula o inverso modular de e mod phi:
        d ≡ e^(-1) (mod phi)
    usando Euclides Estendido.
    """
    g, x, _ = egcd(e, phi)
    if g != 1:
        raise ValueError("e e phi(n) não são coprimos; inverso modular não existe.")
    return x % phi


def is_probable_prime(n, k=10):
    """
    Teste probabilístico de primalidade de Miller-Rabin.
    k = número de rodadas de teste.
    Quanto maior k, maior a confiança.
    """
    if n < 2:
        return False

    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        probably_composite = True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                probably_composite = False
                break

        if probably_composite:
            return False

    return True


def generate_prime(bits):
    """
    Gera um número primo provável com o número de bits especificado.
    """
    if bits < 8:
        raise ValueError("Use pelo menos 8 bits para gerar primos.")

    while True:
        candidate = random.getrandbits(bits)
        candidate |= (1 << (bits - 1))
        candidate |= 1

        if is_probable_prime(candidate):
            return candidate


def generate_keys(bits=512):
    """
    Gera um par de chaves RSA.

    bits: tamanho aproximado de cada primo p e q.
    O módulo n terá aproximadamente 2*bits.

    Retorna:
        public_key  = (e, n)
        private_key = (d, n)
        detalhes    = (p, q, phi)
    """
    print(f"[+] Gerando primo p com {bits} bits...")
    p = generate_prime(bits)

    print(f"[+] Gerando primo q com {bits} bits...")
    q = generate_prime(bits)
    while q == p:
        q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537

    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key, (p, q, phi)


def text_to_blocks(text, n):
    """
    Converte o texto em bytes UTF-8 e depois em blocos inteiros menores que n.
    """
    data = text.encode("utf-8")

    block_size = 1
    while (1 << (8 * block_size)) < n:
        block_size += 1
    block_size -= 1

    if block_size < 1:
        raise ValueError("n é pequeno demais para suportar qualquer bloco de dados.")

    blocks = []
    for i in range(0, len(data), block_size):
        chunk = data[i:i + block_size]
        block_int = int.from_bytes(chunk, byteorder="big")
        blocks.append(block_int)

    return blocks, block_size, len(data)


def blocks_to_text(blocks, block_size, original_length):
    """
    Reconstrói o texto a partir dos blocos inteiros.
    """
    recovered = bytearray()

    for block in blocks:
        chunk = block.to_bytes(block_size, byteorder="big")
        recovered.extend(chunk)

    recovered = recovered[:original_length]
    return recovered.decode("utf-8")


def encrypt_message(message, public_key):
    """
    Cifra uma string usando a chave pública.
    Retorna:
        encrypted_blocks, block_size, original_length
    """
    e, n = public_key

    blocks, block_size, original_length = text_to_blocks(message, n)
    encrypted_blocks = [pow(block, e, n) for block in blocks]

    return encrypted_blocks, block_size, original_length


def decrypt_message(encrypted_blocks, private_key, block_size, original_length):
    """
    Decifra os blocos usando a chave privada e reconstrói a mensagem.
    """
    d, n = private_key

    decrypted_blocks = [pow(block, d, n) for block in encrypted_blocks]
    return blocks_to_text(decrypted_blocks, block_size, original_length)


def print_key_info(public_key, private_key, details):
    e, n = public_key
    d, _ = private_key
    p, q, phi = details

    print("\n================= CHAVES GERADAS =================")
    print(f"p   = {p}")
    print(f"q   = {q}")
    print(f"n   = p * q = {n}")
    print(f"phi = (p-1)*(q-1) = {phi}")
    print(f"e   = {e}")
    print(f"d   = {d}")
    print("==================================================\n")


def main():
    print("============================================")
    print("   SISTEMA RSA - CIFRAGEM ASSIMÉTRICA")
    print("============================================")

    while True:
        print("\n1 - Gerar chaves RSA")
        print("2 - Cifrar mensagem")
        print("3 - Decifrar mensagem")
        print("4 - Demonstração automática")
        print("0 - Sair")

        option = input("\nEscolha uma opção: ").strip()

        if option == "1":
            bits = int(input("Informe o tamanho em bits de cada primo (ex: 256, 512): "))
            public_key, private_key, details = generate_keys(bits)
            print_key_info(public_key, private_key, details)

        elif option == "2":
            print("\n[!] Para cifrar, gere as chaves antes.")
            bits = int(input("Informe o tamanho em bits de cada primo (ex: 256, 512): "))
            public_key, private_key, details = generate_keys(bits)

            message = input("Digite a mensagem para cifrar: ")
            encrypted_blocks, block_size, original_length = encrypt_message(message, public_key)

            print("\n--- RESULTADO DA CIFRAGEM ---")
            print("Chave pública (e, n):")
            print(public_key)
            print("\nBlocos cifrados:")
            print(encrypted_blocks)
            print(f"\nTamanho do bloco: {block_size} bytes")
            print(f"Tamanho original da mensagem: {original_length} bytes")

        elif option == "3":
            print("\n[!] Esta opção fará uma demonstração completa.")
            bits = int(input("Informe o tamanho em bits de cada primo (ex: 256, 512): "))
            public_key, private_key, details = generate_keys(bits)

            message = input("Digite a mensagem para cifrar e depois decifrar: ")
            encrypted_blocks, block_size, original_length = encrypt_message(message, public_key)
            decrypted_message = decrypt_message(
                encrypted_blocks,
                private_key,
                block_size,
                original_length
            )

            print_key_info(public_key, private_key, details)

            print("--- MENSAGEM ORIGINAL ---")
            print(message)

            print("\n--- MENSAGEM CIFRADA (blocos inteiros) ---")
            print(encrypted_blocks)

            print("\n--- MENSAGEM DECIFRADA ---")
            print(decrypted_message)

            if decrypted_message == message:
                print("\n[SUCESSO] A mensagem original foi recuperada corretamente.")
            else:
                print("\n[ERRO] A mensagem recuperada é diferente da original.")

        elif option == "4":
            bits = 256
            message = "RSA implementado manualmente com sucesso!"

            print(f"\n[DEMO] Gerando chaves com {bits} bits por primo...")
            public_key, private_key, details = generate_keys(bits)

            print_key_info(public_key, private_key, details)

            print("--- MENSAGEM ORIGINAL ---")
            print(message)

            encrypted_blocks, block_size, original_length = encrypt_message(message, public_key)

            print("\n--- MENSAGEM CIFRADA ---")
            print(encrypted_blocks)

            decrypted_message = decrypt_message(
                encrypted_blocks,
                private_key,
                block_size,
                original_length
            )

            print("\n--- MENSAGEM DECIFRADA ---")
            print(decrypted_message)

            if decrypted_message == message:
                print("\n[SUCESSO] Demonstração concluída com êxito.")
            else:
                print("\n[ERRO] Falha na demonstração.")

        elif option == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
