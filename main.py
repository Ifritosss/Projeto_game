print ("+--------------------------------------------------------------+")
print ("|######################## SHOW DO TRILHÃO #######################|")
print ("+--------------------------------------------------------------+")

Reais = 0
cont = 1
print ("ESCOLHA OS SEGUINTES TESMAS: \n 1 Saude \n 2 Educação")

Resposta = int(input(" Digite sua escolha: "))

if Resposta == 1:
    
    print ("PERGUNTA NUMERO 1")
    print ("Quantos ovos são necessarios para se fazer um bolo? \n Alternativa 1: 3 Ovos \n Alternativa 2: 5 Ovos \n Alternativa 3: 10 Ovos")
    questao1 = int(input("Digite sua resposta: "))
    if questao1 != 2:
          break
    print (" Resposta errada ")
    print (" Para fazer um bolo são necessarios 5 Ovos para que ele possa ficar consistente")
         
    else:
        print (" Certa resposta ")
        print ("Para fazer um bolo são necessarios 5 Ovos para que ele possa ficar consistente")
        Reais += 1
        
    print ("PERGUNTA NUMERO 2")
    print ("Quantas xicaras de cha de arroz são necessarias para se fazer um bolo? \n Alternativa 1: 3 Xicaras \n Alternativa 2: 5 Xicaras \n Alternativa 3: 10 Xicaras")
    questao2 = int(input("Digite sua resposta: "))
    if questao2 != 1:
        print (" Resposta errada")
        print ("Para fazer um bolo são necessarios  3 Xicaras para que ele possa ficar consistente")
        Reais +=  1
    else:
        print (" Certa resposta")
        print ("Para fazer um bolo são necessarios 3 Xicaras para que ele possa ficar consistente")
        
    print ("Voce possui até o momento R$ %2.8f" % (Reais))
    
