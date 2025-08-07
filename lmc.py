def obter_numero(prompt, permitir_vazio=False):
    """Função para obter um número do usuário, tratando o formato brasileiro."""
    while True:
        try:
            texto = input(prompt)
            if permitir_vazio and not texto:
                return None
            numero = float(texto.replace('.', '').replace(',', '.'))
            return numero
        except (ValueError, TypeError):
            print("Erro: Por favor, insira um número válido (ex: 1500,50). Tente novamente.")

def obter_percentual(prompt):
    """Função para obter uma porcentagem com até 2 casas decimais."""
    while True:
        try:
            texto = input(prompt)
            if '%' in texto:
                texto = texto.replace('%', '')
            
            numero = float(texto.replace(',', '.'))
            # Converte para decimal, ex: 90.16 -> 0.9016
            return numero / 100.0
        except (ValueError, TypeError):
            print("Erro: Por favor, insira um percentual válido (ex: 89,66). Tente novamente.")


def formatar_reais(valor):
    """Formata um número como moeda brasileira (R$)."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_percentual(valor):
    """Formata um número como porcentagem."""
    return f"{valor:.2%}"

def main():
    """Função principal do programa."""
    print("--- Calculadora com Ajuste Fino para Porcentagens de 2 Casas Decimais ---")
    
    teto_maximo_geral = obter_numero("\nDigite o TETO MÁXIMO (valor final total): ")
    if teto_maximo_geral is None: return

    print("\nInsira os Valores Originais. Deixe em branco para finalizar.")
    valores_originais = []
    contador = 1
    while True:
        valor = obter_numero(f"Valor Original #{contador}: ", permitir_vazio=True)
        if valor is None: break
        valores_originais.append(valor)
        contador += 1

    if len(valores_originais) < 2:
        print("É preciso ter ao menos 2 valores para fazer o ajuste.")
        return

    # --- Início do Processo Interativo ---
    resultados = []
    soma_parcial_final = 0
    
    print("\n--- Defina as porcentagens para os primeiros itens ---")
    # Loop para N-1 itens (todos exceto o último)
    for i in range(len(valores_originais) - 1):
        vo = valores_originais[i]
        print(f"\nItem #{i+1} (Valor Original: {formatar_reais(vo)})")
        percentual = obter_percentual("Digite a % Aplicada (ex: 89,66): ")
        
        valor_final_item = round(vo * percentual, 2)
        soma_parcial_final += valor_final_item
        
        resultados.append({
            'vo': vo,
            'pa': percentual,
            'vf': valor_final_item
        })

    # --- Cálculo Automático para o Último Item ---
    print("\n--- Ajustando o último item para bater o TETO MÁXIMO ---")
    
    ultimo_item_vo = valores_originais[-1]
    ultimo_item_vf = teto_maximo_geral - soma_parcial_final
    ultimo_item_pa = ultimo_item_vf / ultimo_item_vo if ultimo_item_vo != 0 else 0
    
    resultados.append({
        'vo': ultimo_item_vo,
        'pa': ultimo_item_pa,
        'vf': ultimo_item_vf
    })
    
    # --- Impressão dos Resultados ---
    print("\n" + "=" * 80)
    print("--- Resultado Final com Ajuste ---")
    print(f"{'Valor Original':<25} {'% Aplicada':<20} {'Valor Final':<20}")
    print("-" * 80)
    
    soma_total_verificacao = 0
    for res in resultados:
        soma_total_verificacao += res['vf']
        percentual_display = f"{res['pa']:.2%}" 
        print(f"{formatar_reais(res['vo']):<25} {percentual_display:<20} {formatar_reais(res['vf']):<20}")

    # Calcula a soma total dos valores originais para exibição
    soma_total_original = sum(valores_originais)

    print("=" * 80)
    # --- BLOCO DE TOTAIS (com a nova linha) ---
    print(f"{'SOMA VALORES ORIGINAIS:':>47} {formatar_reais(soma_total_original):>20}")
    print(f"{'SOMA FINAL CALCULADA:':>47} {formatar_reais(soma_total_verificacao):>20}")
    print(f"{'TETO MÁXIMO DEFINIDO:':>47} {formatar_reais(teto_maximo_geral):>20}")


if __name__ == "__main__":
    main()