def obter_numero(prompt):
    """Função para obter um número do usuário, tratando o formato brasileiro."""
    while True:
        try:
            texto = input(prompt)
            if not texto:
                return None
            numero = float(texto.replace('.', '').replace(',', '.'))
            return numero
        except ValueError:
            print("Erro: Por favor, insira um número válido (ex: 1500,50). Tente novamente.")

def formatar_reais(valor):
    """Formata um número como moeda brasileira (R$)."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_percentual(valor):
    """Formata um número como porcentagem."""
    return f"{valor:.2%}"

def executar_um_calculo():
    """Esta função contém toda a lógica para um único cálculo de rateio."""
    print("\n" + "*"*65)
    print("Iniciando novo cálculo...")
    # 1. Obter o TETO MÁXIMO geral
    teto_maximo_geral = obter_numero("\nPrimeiro, digite o TETO MÁXIMO (valor final total): ")
    if teto_maximo_geral is None:
        print("TETO MÁXIMO é obrigatório. Programa encerrado.")
        return
        
    print("\nAgora, insira todos os Valores Originais. Deixe em branco para finalizar.")
    print("-" * 40)

    # 2. Obter a lista de Valores Originais
    valores_originais = []
    contador = 1
    while True:
        valor = obter_numero(f"Valor Original #{contador}: ")
        if valor is None:
            break
        valores_originais.append(valor)
        contador += 1

    if not valores_originais:
        print("Nenhum valor inserido. Finalizando este cálculo.")
        return

    # --- Início dos Cálculos ---

    # 3. Somar os valores originais
    soma_dos_originais = sum(valores_originais)

    # 4. Calcular o percentual de rateio único
    percentual_rateio = teto_maximo_geral / soma_dos_originais if soma_dos_originais != 0 else 0
    
    # --- Impressão dos Resultados ---
    print("\n" + "=" * 65)
    print("--- Resultado do Rateio ---")
    print(f"Soma dos Valores Originais (Base de Cálculo): {formatar_reais(soma_dos_originais)}")
    print(f"TETO MÁXIMO definido (Alvo): {formatar_reais(teto_maximo_geral)}")
    print(f"Percentual de Rateio Único Calculado: {formatar_percentual(percentual_rateio)}")
    print("-" * 65)
    
    # Cabeçalho da tabela
    print(f"{'Valor Original':<25} {'% Aplicada':<20} {'Valor Final':<20}")
    print("-" * 65)

    soma_final_verificacao = 0
    # Calcula e imprime cada linha
    for valor in valores_originais:
        valor_final_item = valor * percentual_rateio
        soma_final_verificacao += valor_final_item
        print(f"{formatar_reais(valor):<25} {formatar_percentual(percentual_rateio):<20} {formatar_reais(valor_final_item):<20}")

    print("=" * 65)
    # Imprime a linha de totais para verificação
    print(f"{formatar_reais(soma_dos_originais):<25} {'':<20} {formatar_reais(soma_final_verificacao):<20}")


def main():
    """Função principal que controla o loop do programa."""
    print("--- Calculadora de Rateio Proporcional com Teto ---")
    
    while True:
        executar_um_calculo()
        
        proximo = input("\nDeseja realizar um novo cálculo? (s/n): ").lower()
        if proximo != 's':
            break
            
    print("\nObrigado por usar a calculadora. Até mais!")


if __name__ == "__main__":
    main()