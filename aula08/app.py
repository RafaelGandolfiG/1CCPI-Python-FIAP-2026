from model import model_lead
import control
import pandas as pd


def add_lead():
    name = input("nome: ")
    email = input("e-mail: ")
    status = input("etapa no funil de vendas: ")
    print("lead adicionado")
    print(model_lead(name, email, status))
    control.create_lead(model_lead(name, email, status))


def list_leads():
    leads = control.read_leads()
    # df=pd.read_json(control.DB_PATH)
    #   print(df)


def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar Lead")
        print("[2] Listar Leads")
        print("[0] Sair do programa")
        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Saindo...")
            break
        else:
            print("opção invalida")


if __name__ == "__main__":
    main()
