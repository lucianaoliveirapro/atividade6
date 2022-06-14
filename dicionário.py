itensQuantidade=int(input("Digite a quantidade de itens diferentes: "))
itens=[]
i=0
while i<itensQuantidade:
    nomeItem=input("Nome do produto{}: ".format(i+1))
    quantosdesse=float(input("Quantidade desse produto: "))
    valorunitario=float(input("Valor unitário desse produto: "))
    item={
        "nomeItem":nomeItem,
        "quantosdesse":quantosdesse,
        "valorunitario":valorunitario
        }
    itens.append(item)
    i+=1
total=0
print("===========================")
print("Recibo")
print("Quantidade | Nome | Valor")
para item em itens:
    print("{} | {} | R${}".format(item["quantosDesse"],item["nomeItem"],item["valorUnitario"]))
    total+=item["valorUnitario"] * item["quantosDesse"]
print("Total: R$"+str(total))
print("======================")
