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
    print(f"## | {"nome":<15} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<15} | {lead["email"]}")


def search_leads():
    print("buscando")
    query = input("Buscar por: ").strip().lower()
    search_results = control.read_leads_search(query)
    print(f"## | {"nome":<15} | E-mail")
    for i, lead in search_results:
        print(f"{i:02d} | {lead["name"]:<15} | {lead["email"]}")


def export_leads():
    print("lead exportado")
    path_csv = control.export_csv()
    if path_csv is None:
        print("Nao foi possivel exportar para csv")
    else:
        print(f"Exportado para {path_csv}")


def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar Lead")
        print("[2] Listar Leads")
        print("[3] Buscar (nome/email)")
        print("[4] Exportar para CSV")
        print("[0] Sair do programa")
        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Saindo...")
            break
        else:
            print("opção invalida")


if __name__ == "__main__":
    main()
