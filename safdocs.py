
import re
import os
import sqlite3
import pdfkit
import locale
import time
import pandas
from datetime import datetime

class Sqlite():
    '''Controlador SQLITE'''
    def __init__(self) -> None:
        self.CON = sqlite3.connect('database.db')
        self.CURSOR = self.CON.cursor()

    def timestamp(self) -> str:
        '''retorna total de segundos desde 1970-01-01'''
        return str(int(datetime.now().timestamp()))

    def show_tables(self) -> None:
        '''retorna o nome das tabelas do banco'''
        return [
            i[1] for i in self.CURSOR.execute(
                f'''SELECT * FROM sqlite_master'''
            ).fetchall()
        ]

    def create_table(self, table_name: str, keys_: list) -> None:
        '''
        cria uma tabela vazia no banco
        Parâmetros:
            - table_name: nome da tabela a ser criada (faz referência ao nome do arquivo .html)
            - keys_: uma lista contendo o nome das colunas da tabela
        '''
        
        try:
            self.CURSOR.execute(
                f'''CREATE TABLE {table_name}({', '.join(keys_)})'''
            )
        except:
            pass

    def columns(self, table_name: str) -> list:
        '''
        retorna o nome das colunas de uma tabela
        Parâmetros:
            - table_name: nome de uma tabela existente no banco
        '''
        
        return [
            i[1] for i in self.CURSOR.execute(
                f'''PRAGMA table_info({table_name})'''
            ).fetchall()
        ]

    def insert(self, table_name: str, values_: list) -> None:
        '''
        insere valores em uma tabela do banco
        Parâmetros:
            - table_name: nome de uma tabela existente no banco
            - values_: lista contendo os valores a serem lançados no banco
            (deve ser compatível com o número de colunas)
        '''
        
        query = f'''
        INSERT INTO {table_name} VALUES ({','.join(list('?' * len(values_)))})
        '''
        self.CURSOR.execute(query, values_)

    def create(self, table_name: str, data: dict) -> None:
        '''
        executa create_table e insert em seguida a partir dos mesmos parâmetros
        Parâmetros:
            - table_name: nome de uma tabela existente ou não, no banco
            - values_: lista contendo os valores a serem lançados no banco
            (deve ser compatível com o número de colunas)
        '''
        
        self.create_table(table_name, list(data.keys()))
        self.insert(table_name, list(data.values()))
        self.CON.commit()

    def read(self, table_name: str) -> list:
        '''lê uma tabela do banco'''
        return self.CURSOR.execute(f'''SELECT * FROM {table_name}''').fetchall()
    
    def delete(self, 
               table_name: str, key_: str, 
               value_: str, all_: bool = False) -> None:
        '''
        exclui um valor específico de uma tabela a partir de uma chave e valor
        Parâmetros:
            - table_name: nome da tabela a ser editada
            - key_: coluna que será usada como chave
            - value_: valor procurado
            - all_: se True, deleta todos os valores da tabela
        '''
        
        if all_:
            self.CURSOR.execute(f'''DELETE FROM {table_name}''')
        else:
            self.CURSOR.execute(
                f'''DELETE FROM {table_name} WHERE {key_} = "{value_}"'''
            )
        self.CON.commit()
    
    def update(self, 
               table_name: 
               str, key_: str, value_: str, 
               target_: str, target_value: str) -> None:
        
        '''
        edita um valor específico de uma tabela a partir de uma chave e valor
        Parâmetros:
            - table_name: nome da tabela a ser editada
            - key_: coluna que será usada como chave
            - value_: valor procurado
            - target_: coluna com o valor a ser editado
            - target_value: novo valor
        '''
        
        query = f'''
        UPDATE {table_name} SET {target_} = "{target_value}" 
        WHERE {key_} = "{value_}"
        '''
        self.CURSOR.execute(query)
        self.CON.commit()

class Documentos():
    '''
    Gerador e Controlador de Despachos
    Parâmetros:
        - path_folder: caminho dos templates do setor
        - path_converter: caminho para o executável wkhtmltox
    '''

    def __init__(self, path_folder: str, path_converter: str) -> None:
        self.PATH_TEMPLATE = path_folder
        self.CSS = 'styles.css'
        self.PATH_WKHTP = path_converter
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

    def html_to_pdf(self, html_name: str, pdf_name: str) -> None:
        '''
        converte um arquivo .html para .pdf usando o software wkhtmltox
        Parâmetros:
            - html_name: nome ou caminho do arquivo que será convertido
            - pdf_name: nome do novo arquivo .pdf
        '''

        pdfkit.from_file(
            html_name, 
            pdf_name, 
            options = {
                'page-size': 'A4', 
                '--enable-local-file-access': True, 
                '--user-style-sheet': self.CSS
            }, 
            configuration = pdfkit.configuration(
                wkhtmltopdf = self.PATH_WKHTP
            )
        )

    def money(self, value: float) -> str:
        '''converte um valor (float) para Real Brasileiro'''

        if re.match(r'\d', str(value)):
            return locale.currency(value, grouping = True)
        return value
        
    def convert_excel(self, filename: str) -> str:
        '''
        converte um arquivo .xlsx em uma string com tag table
        Parâmetros:
            - filename: nome ou caminho do arquivo
        '''

        df = pandas.read_excel(
            filename
        )

        columns = list(df.columns)
        columns = f'''\t<tr id="header-table">\n{''.join([f'''\t\t\t<th>{i}</th>\n''' for i in columns])}\t\t</tr>'''
        
        values_by_lines = [list(i) for i in df.values]
        values = []
        for line in values_by_lines:
            values.append(f'''\t<tr>\n{''.join([f'''\t\t\t<td align="center">{self.money(i)}</td>\n''' for i in line])}\t\t</tr>''')
        values = '\n'.join(values)

        table_structure = f'''
        <table align="center">
        {columns}
        {values}
        </table>
        '''

        return table_structure
    
    def upload_img(self, filename: str, h: int) -> str:
        '''
        escreve a tag img para um arquivo específico
        Parâmetros:
            - filename: nome ou caminho do arquivo
            - h: altura desejada para a imagem (a largura será o dobro da altura).
        '''

        return f'''
        <img id="img_upload" src="{filename}" width="{2*h}" height="{h}">
        '''

    def create(self, filename, table_name: str, data: dict) -> None:
        '''
        cria um arquivo pdf a partir das informações inseridas
        Parâmetros:
            - filename: identificador do arquivo (str)
            - table_name: nome do arquivo html usado como base (str)
            - data: informações que estaram no documento (dict)
        '''
        
        path = f'''{self.PATH_TEMPLATE}/{table_name}.html'''
        base_html = open(path, 'r', encoding='utf-8').read()
        
        for k, v in data.items():
            base_html = re.sub(k, str(v), base_html)
        
        filepath = f'''{filename}_{table_name}_{str(int(datetime.now().timestamp()))}'''
        with open(f'''{filepath}.html''', 'w', encoding = 'utf-8') as file:
            file.write(base_html)
            file.close()
        
        time.sleep(1)

        self.html_to_pdf(
            html_name = f'''{filepath}.html''', pdf_name = f'''{filepath}.pdf'''
        )

        os.remove(f'''{filepath}.html''')

