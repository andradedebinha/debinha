qtd_caixas = 1250
capacidade_caminhao = 12

caminhoes_completos = (qtd_caixas // capacidade_caminhao)
print("Caminhao Completos: ",caminhoes_completos)

caixas_restantes = (qtd_caixas % caminhoes_completos)
print("Caixas Restantes: ",caixas_restantes)