resp1 = input("O programa funciona?\n")
if resp1 == "SIM":
    resp2 = input("Você entende o que fez?\n")
    if resp2 =="SIM":
        print("Ótimo. Então não mexe!\n")
    else:# resp2 != SIM
        resp6 = input("Já foi na tutoria?\n")
        if resp6 == "SIM":
            print("Choremos!\n")
        else: #resp 6 != "SIM"
            print("Temos um time a disposição!\n")

else:#resp1 != SIM
    resp3 = input("Você sabe onde está o erro?\n")
    if resp3 == "SIM":
        resp4 = input("Acha que pode solucionar sozinho?\n")
        if resp4 == "SIM":
            print("Então mão na massa!\n")
        else:#resp4 != "SIM"
            resp5 = input("Já pesquisou no Google?\n")
            if resp5 == "SIM":
                resp6 = input("Já foi na tutoria?\n")
                if resp6 == "SIM":
                    print("Choremos!\n")
                else: #resp 6 != "SIM"
                    print("Temos um time a disposição!\n")
            else: #resp5 != "SIM"
                print("Corre lá então!\n")
    else: #resp3 == "SIM"
        resp6 = input("Já foi na tutoria?\n")
        if resp6 == "SIM":
            print("Choremos!\n")
        else: #resp 6 != "SIM"
            print("Temos um time a disposição!\n")
        
            
