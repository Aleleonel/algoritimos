convidados = []
convite = ""
while convite != "ok":
    convite = (input("Digite o nome do convidado: "))
    if convite != "ok":
        convidados.append(convite)
        

print(sorted(convidados))