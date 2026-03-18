print('--- Relatorio Estatísticos de Negócio ---')

print(f'A média de vendas é \
      $ {media_valor_vendas:,.2f}')
print(f'A mediana (valor central) das vendas é \
      $ {q2:,.2f}')
print(f'O Delta (Diferença Financeira) entre \
      elas é: $ {delta_media_mediana:,.2f}')

print('\n--- Analise Comportamental ---\n')
print(f'Distância Relativa entre elas: \
      {distancia_percentual:.2f}')


if abs(distancia_percentual) < 0.10:
      print(f'INFERÊNCIA: Baixa Dispersão. \
            A média é confiável para representar a coluna.')

elif abs(distancia_percentual) < 0.25:
      print(f'INFERÊNCIA: Dispersão Moderada. \
            Fique atento aos extremos, média começa a mentir.')
      
else:
      print(f'INFERÊNCIA: Alta Dispersão. \
            A média NÃO é confiável, foque na mediana.')

print(f'Grau de Assimetria (Skewness): \
      {assimetria:.4f}')

if assimetria > 0.5:
    print(f'INFERÊNCIA (Assimetria Positiva): \
            Nossas vendas tem uma cauda longa para a direita.\
            Os grandes clientes são minoria, todavia eles \
            faturam valores expressivos \
            puxando a venda média para cima')
elif assimetria < -0.5:
    print(f'INFERÊNCIA (Assimetria Negativa): \
            Nossa vendas tem uma cauda longa para a esquerda.\
            O valor médio está sendo puxado para baixo por um \
            grande volume de vendas baratas, \
            talvez pela liquidação')
else:
    print(f'INFERÊNCIA (Simétrica): Distribuição Equilibrada.\
          Média e mediana estão bem próximas.')
