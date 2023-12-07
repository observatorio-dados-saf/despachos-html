
import re
import os
import sqlite3
import pdfkit

from datetime import datetime
from time import sleep

class Sqlite():

    def __init__(self) -> None:
        self.CON = sqlite3.connect('database.db')
        self.CURSOR = self.CON.cursor()

    def timestamp(self) -> str:
        return str(int(datetime.now().timestamp()))

    def show_tables(self) -> None:
        return [i[1] for i in self.CURSOR.execute(f'''SELECT * FROM sqlite_master''').fetchall()]

    def create_table(self, table_name: str, keys_: list) -> None:
        try:
            self.CURSOR.execute(f'''CREATE TABLE {table_name}({', '.join(keys_)})''')
        except:
            pass

    def columns(self, table_name: str) -> list:
        return [i[1] for i in self.CURSOR.execute(f'''PRAGMA table_info({table_name})''').fetchall()]

    def insert(self, table_name: str, values_: list) -> None:
        self.CURSOR.execute(f'''INSERT INTO {table_name} VALUES ({','.join(list('?' * len(values_)))})''', values_)

    def create_insert(self, table_name: str, data: dict) -> None:
        self.create_table(table_name, list(data.keys()))
        self.insert(table_name, list(data.values()))
        self.CON.commit()

    def read(self, table_name: str) -> list:
        return self.CURSOR.execute(f'''SELECT * FROM {table_name}''').fetchall()
    
    def delete(self, table_name: str, key_: str, value_: str, all_: bool = False) -> None:
        if all_:
            self.CURSOR.execute(f'''DELETE FROM {table_name}''')
        else:
            self.CURSOR.execute(f'''DELETE FROM {table_name} WHERE {key_} = "{value_}"''')
        self.CON.commit()
    
    def update(self, table_name: str, key_: str, value_: str, target_: str, target_value: str) -> None:
        self.CURSOR.execute(f'''UPDATE {table_name} SET {target_} = "{target_value}" WHERE {key_} = "{value_}"''')
        self.CON.commit()

class Despachos():

    def __init__(self, path_folder: str, path_converter: str) -> None:
        self.PATH_TEMPLATE = path_folder
        self.CSS = 'styles.css'
        self.PATH_WKHTP = path_converter

    def html_to_pdf(self, html_name: str, pdf_name: str) -> None:
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

    def create(self, filename, table_name: str, data: dict) -> None:
        path = f'''{self.PATH_TEMPLATE}/{table_name}.html'''
        base_html = open(path, 'r', encoding='utf-8').read()
        
        for k, v in data.items():
            base_html = re.sub(k, str(v), base_html)
        
        filepath = f'''{filename}_{table_name}_{str(int(datetime.now().timestamp()))}'''
        with open(f'''{filepath}.html''', 'w', encoding = 'utf-8') as file:
            file.write(base_html)
            file.close()
        
        self.html_to_pdf(
            html_name = f'''{filepath}.html''', pdf_name = f'''{filepath}.pdf'''
        )

        os.remove(f'''{filepath}.html''')

