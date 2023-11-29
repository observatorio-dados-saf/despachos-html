import webbrowser
import re

class Despachos():

    def __init__(self, folder: str) -> None:
        self.PATH_TEMPLATE = folder

    def create(self, type_: str, repl: dict) -> None:
        
        base_html = open(f'''{self.PATH_TEMPLATE}/{type_}.html''', 'r', encoding='utf-8').read()
        
        for k, v in repl.items():
            base_html = re.sub(k, str(v), base_html)
        
        with open('index.html', 'w', encoding = 'utf-8') as file:
            file.write(base_html)
            file.close()
        
        webbrowser.open('index.html', 0)

if __name__ == '__main__':

    despachos = Despachos(folder = 'templates')

    replaces = {
        'var_num_page': 14,
        'num_proc': '18497/2023', 
        'dest': 'FUNDO ESTADUAL DE SAÚDE', 
        'theme': 'INDICAÇÃO DE CONTA', 
        'num_desp': '1850/2023', 
        'num_fonte': '1.6.00.301000', 
        'num_ag': '3846-6',
        'num_db': '8455-7', 
        'text_rec': 'Manutenção (Custeio) - Atenção à Saúde da População para Procedimentos no MAC', 
        'num_port': 'PORTARIA GM/MS Nº 25, DE 20 DE JANEIRO DE 2023', 
        'text_port': 'Divulga os montantes anuais alocados aos Estados, Distrito Federal e Municípios, destinados ao cofinanciamento das ações e serviços públicos de saúde no grupo de atenção de média e alta complexidade ambulatorial e hospitalar (Teto MAC).', 
        'colab': 'Jersiton Tiago Pereira Matos'
    }

    despachos.create(type_ = 'ind_conta', repl = replaces)
