print("+-------------------------------------------------------+")
print("|################### SHOW DO TRILHÃO ###################|")
print("+-------------------------------------------------------+")

Reais = 0
count = 1
print("ESCOLHA ENTRE: \n 1 para Começar \n 2 para Sair")

Resposta = int(input("Digite sua escolha: "))

if Resposta == 1:
    print("\nPERGUNTA NUMERO 1")
    print("Para quantos tipos sanguíneos o tipo O+ pode doar? >>>>Responda com o número das alternativas!<<<< \n [Alternativa 1] - 2 tipos \n [Alternativa 2] - 4 tipos \n [Alternativa 3] - Todos os tipos \n [Alternativa 4] - Nenhuma dessas")
    questao1 = int(input("Digite sua resposta: "))
    if questao1 == 2:
        print("Certa Resposta")
        print("O tipo sanguíneo O+ é compatível com todos os positivos, totalizando 4 tipos")
        Reais += 1
    else:
        print("Resposta errada!")
        print("O tipo sanguíneo O+ é compatível com todos os positivos, totalizando 4 tipos, a resposta correta era [Alternativa 2] - 4 tipos")
    print("\nPERGUNTA NUMERO 2")
    print("Qual a proteína responsavel pela coloração do corpo? \n [Alternativa 1] - Melanina \n [Alternetiva 2] - Caseína \n [Alternativa 3] - Actina \n [Alternativa 4] - Miosina")
    questao2 = int(input("Digite sua resposta: "))
    if questao2 == 1:
        print("Certa resposta")
        print("A proteína responsável pela coloração do corpo é nomeada de Melanina produzida pela Tirosina")
        Reais += 1
    else:
        print("Resposta errada!")
        print("A proteína responsável pela coloração do corpo é nomeada de Melanina, que é produzida pela Tirosina, a resposta correta era [Alternativa 1] - Melanina")
    print("\nPERGUNTA NUMERO 3")
    print("Qual o fator que o corpo de um diabético não reproduz? \n [Alternativa 1] - Sacarose \n [Alternativa 2] - Maltose \n [Alternativa 3] - Celulose \n [Alternativa 4] - Insulina")
    questao3 = int(input("Digite sua resposta: "))
    if questao3 == 4:
        print("Certa resposta")
        print("A insulina é um hormônio que o corpo de um diabético não produz o suficiente e por isso a glicose não é metabolizada")
        Reais += 1
    else:
        print("Resposta errada!")
        print("A insulina é um hormônio que o corpo de um diabético não produz o suficiente e por isso a glicose não é metabolizada, resposta correta é [Alternativa 4] - Insulina")

    print("\nPERGUNTA NUMERO 4")
    print("O sexo pode trazer muitos benefícios para a vida do homem e da mulher, quais desses a seguir não é um desses benefícios? \n [Alternativa 1] - Sistema Imunológico \n [Alternativa 2] - Sono \n [Alternativa 3] - Produção de Glicose \n [Alternativa 4] - Produção de Ocitocina")
    questao4 = int(input("Digite sua resposta: "))
    if questao4 == 3:
        print("Certa reposta")
        print("O sexo ajuda muito na vida dos adultos, porém a produção de glicose não é um benefício e por isso, é a única das alternativas que não é um benefício do mesmo")
        Reais += 1
    else:
        print("Resposta errada!")
        print("Dentre todos os benefícios, a produção de glicose não se aplica como um, então a resposta certa sera a [Alternativa 3] - Produção de Clicose")

    print("\nPERGUNTA NUMERO 5")
    print("É recomendado que prática ao levantar da cama? \n [Alternativa 1] - Flexão \n [Alternativa 2] - Abdominal \n [Alternativa 3] - Banho \n [Alternativa 4] - Alongamento")
    questao5 = int(input("Digite sua resposta: "))
    if questao5 == 4:
        print("Certa resposta")
        print("Ao acordar, é recomendado que façamos um alongamento, para que assim, nossos músculos possam ser preparados para a rotina do dia, por isso, é muito importante esta atividade ao acordar")
        Reais += 1
    else:
        print("Resposta errada!")
        print("Ao acordar, é muito importante alongar seu corpo para preparar os músculos para o estímulo do dia, por isso, a resposta certa seria [Alternativa 4] - Alongamento")
    print("\nPARABÉNS! Você conseguiu um total de R$ %2.8f" % (Reais))
    print("\nObrigado por jogar o nosso jogo! Aperte qualquer tecla para encerrar a janela! <3")
else:
    print("Até logo!")
