print('{:=^40}'.format (' lOJAS PINHO '))
preco = float(input('preço das compras: R$ '))
print(''' Formas de pagamento
[1] à vista dinheiro / cheque
[2] à vista cartão
[3] 2x no cartão 
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco *5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em, 2x de R${}'.format(parcela))
elif opcao == 4 :
    total = preco + (preco * 20 /100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(' Sua compra será parcelada e, {}x de R$ com Juros'. format(totparc, parcela))
else:
    total = 0
    print('Opção invalida de pagamento. NÃO PODE SER EFETUADA tente novamente')
print('Sua compra de R${:.2f} vai custar  R${:.2f} no final'.format(preco, total))
