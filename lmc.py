import pandas as pd

def obter_numero(prompt):
    """Função para obter um número do usuário, tratando o formato brasileiro."""
    while True:
        try:
            texto = input(prompt)
            if not texto:
                return None  # Retorna None se o usuário não digitar nada
            
            # Limpa e converte o número no formato brasileiro (ex: "1.234,56")
            numero = float(texto.replace('.', '').replace(',', '.'))
            return numero
        except ValueError:
            print("Erro: Por favor, insira um número válido (ex: 1500,50). Tente novamente.")

def main():
    """Função principal do programa."""
    print("--- Calculadora de Porcentagem Aplicada ---")
    print("Preencha os pares de valores. Deixe o 'Valor Original' em branco para finalizar.\n")

    dados = []
    contador = 1

    while True:
        # Pede ao usuário o Valor Original
        valor_original = obter_numero(f"Digite o Valor Original #{contador}: ")
        
        # Se o usuário deixar em branco, o loop termina
        if valor_original is None:
            break
        
        # Pede ao usuário o Valor Final correspondente
        valor_final = obter_numero(f"Digite o Valor Final   #{contador}: ")

        if valor_final is None:
            print("Valor Final não pode ser vazio. Por favor, insira o par novamente.")
            continue

        # Adiciona os valores à nossa lista de dados
        dados.append({
            'Valor Original (R$)': valor_original,
            'Valor Final (R$)': valor_final
        })
        contador += 1
        print("-" * 20)

    # Se nenhum dado foi inserido, encerra o programa
    if not dados:
        print("Nenhum dado inserido. Programa finalizado.")
        return

    # Cria um DataFrame (tabela) com a biblioteca pandas
    df = pd.DataFrame(dados)

    # Calcula a coluna '% Aplicada'
    # Adiciona uma verificação para evitar divisão por zero
    df['% Aplicada'] = df.apply(
        lambda row: row['Valor Final (R$)'] / row['Valor Original (R$)'] if row['Valor Original (R$)'] != 0 else 0,
        axis=1
    )

    # Adiciona a linha de Total
    soma_original = df['Valor Original (R$)'].sum()
    soma_final = df['Valor Final (R$)'].sum()
    percentual_total = soma_final / soma_original if soma_original != 0 else 0
    
    total_row = pd.DataFrame({
        'Valor Original (R$)': [soma_original],
        '% Aplicada': [percentual_total],
        'Valor Final (R$)': [soma_final]
    }, index=['TOTAL'])
    
    # Reorganiza as colunas para corresponder à sua imagem
    df = df[['Valor Original (R$)', '% Aplicada', 'Valor Final (R$)']]

    # Imprime o resultado formatado
    print("\n--- Resultado Final ---")
    
    # Imprime a tabela principal
    print(df.to_string(formatters={
        'Valor Original (R$)': 'R$ {:,.2f}'.format,
        '% Aplicada': '{:,.2%}'.format,
        'Valor Final (R$)': 'R$ {:,.2f}'.format
    }))
    
    print("-" * 65) # Linha separadora
    
    # Imprime a linha de totais
    print(total_row.to_string(formatters={
        'Valor Original (R$)': 'R$ {:,.2f}'.format,
        '% Aplicada': '{:,.2%}'.format,
        'Valor Final (R$)': 'R$ {:,.2f}'.format
    }, header=False)) # 'header=False' para não repetir o cabeçalho


# Executa a função principal quando o script é rodado
if __name__ == "__main__":
    main()