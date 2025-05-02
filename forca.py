palavra = "uva"
letracerta = [""]*len(palavra)
tentativa = 6
tentativacerta=0
letraerro = 0
errototal=0

forca = [

    """
     _______
    |/      |
    |       
    |       
    |       
    |      
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |       
    |       
    |      
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |      
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|
    |       |
    |      
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / 
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
    |___
    """
]
print("="*46)
print("  JOGO DA FORCA, VOCÊ SÓ PODE ERRAR 6 VEZES  ")
print("="*46)
print(f"           A PALAVRA TEM {len(palavra)} LETRAS     ")
print("="*46)

while errototal < 6 :
    letra = input("Digite uma letra: ")
    for i in range(len(palavra)):
        if letra == palavra[i]:
           letracerta[i] = palavra[i]
           tentativacerta+=1
        else:
            letraerro+=1

    if len(palavra) == letraerro:
        errototal+=1
        tentativa-=1
    letraerro = 0

    if errototal < 6:
        print(forca[errototal])
        print(f"Você ainda tem {tentativa} tentativas")
    else:
        print("Tentativas Esgotadas!!")

    print(letracerta)
    print()

    if tentativacerta == len(letracerta):
        print("Parabêns Você Acertou a Palavra!!!")
        break