# Despachos Automatizados com HTML, CSS e Python

## 1. Requirements

Requer a instalação do software [wkhtmltox](https://wkhtmltopdf.org/) - cópia [aqui](utils/).

```
pip install pdfkit pandas openpyxl
```

## 2. Implantações e To-do List

#### Implantações

- [Deuses dos Executáveis](https://github.com/orgs/pyinstaller/discussions/7100)
- [Build Pack Heroku](https://elements.heroku.com/buildpacks/rohandebroy/heroku-buildpack-wkhtmltopdf)
- [NiceGui WebApp](https://github.com/zauberzeug/nicegui)

#### Features Prioridade (50%)

- [x] Upload de planilhas para elaborar despachos;
- [x] Upload de Imagem;
- [x] Múltiplos browsers;
- [x] Banco de Dados - Aplicação Local - Logs (SQLite + Excel);
- [x] Conversão HTML para PDF (WKHTMLTOX);
- [x] Carga de novos modelos - módulo [Models](models.py);
- [ ] Download de Bytes;
- [ ] Despachos em lote;
- [ ] Protótipo da Versão Web

## 3. _How to Use_

```python
from safdocs import Documentos, Sqlite
from models import Modelos

sql = Sqlite()
docs = Documentos(
    path_folder = 'templates/templates-financeiro', 
    path_converter = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
)

modelo = Modelos('regularizacao')
print(modelo.get_models())
modelo.set_values([sql.timestamp(), '20', '1654/2023', 'Execução', 'Regularização', '1564/2023', 'São Luís, 25 de dezembro', 'Jersiton Matos'])
print(modelo)

docs.create(filename = 'example', table_name = 'regularizacao', data = modelo())
```

> Obs: _cabeçalhos e rodapés: False, elementos gráficos: True_

## 4. CRUD Sqlite

_Gerenciamento de tabelas com sqlite3._

```python
from safdocs import Sqlite

sql = SqlController()

notificacao = {
    ...
}

sql.create('notificacao', notificacao) # gravando dados

print(sql.show_tables()) # tabelas 

print(sql.read(table_name = 'conta')) # dados List[Tuple]

sql.delete('conta', 'timestamp', '1701317738') # DELETE

sql.update('conta', 'timestamp', '1701317981', 'data_despacho', 'São Luís (MA), 25 de dezembro de 2023') # UPDATE

```