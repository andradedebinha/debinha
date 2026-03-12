faturamento = 15000
custos = 5000
perc_imposto = 0.15

imposto = (faturamento * perc_imposto)
lucro = faturamento - custos + imposto
margem = (lucro / faturamento)

print("Faturamento ",f"{faturamento:,.2f}")
print("Lucro.....: ",f"{lucro:,.2f}")
print("Margem....: ",f"{margem:.2%}")

meta_atingida = (margem > 0.3)
print("Meta Atingida" ,meta_atingida)