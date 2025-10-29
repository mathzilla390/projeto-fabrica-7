def separar_pares_impares(lista_original):
    lista_pares = [] 
    lista_impares = [] 
    
    for id_pedido in lista_original:
        if id_pedido % 2 == 0:
            lista_pares.append(id_pedido)
        else:
            lista_impares.append(id_pedido)
            
    return lista_pares, lista_impares

def coletar_ids(num_ids=20):
    ids_entrada = []
    print(f"\n--- Coletando {num_ids} IDs de Pedido ---\n")
    
    for i in range(1, num_ids + 1):
        while True:
            try:
                id_str = input(f"Digite o {i}º ID: ")
                id_int = int(id_str)
                
                if isinstance(id_int, int):
                    ids_entrada.append(id_int)
                    break
            except ValueError:
                print("ERRO: Por favor, digite um número inteiro válido para o ID.")
    return ids_entrada
def main():
    NUM_ITENS = 20
    print("=== Particionador de IDs por Shard (A/B) ===")
    lista_original = coletar_ids(NUM_ITENS)
    lista_pares, lista_impares = separar_pares_impares(lista_original)
    print("\n" + "="*40)
    print("RESUMO DA DISTRIBUIÇÃO:")
    print("="*40)
    print(f"Lista (entrada): {lista_original}")
    total_par = len(lista_pares)
    print(f"Shard A (PAR): {lista_pares}  | total: {total_par}")
    total_impar = len(lista_impares)
    print(f"Shard B (ÍMPAR): {lista_impares}     | total: {total_impar}")
    if total_par + total_impar != NUM_ITENS:
        print("\nAVISO: A soma dos totais não é igual ao número de itens lidos. Verifique a lógica.")
if __name__ == "__main__":
    main()