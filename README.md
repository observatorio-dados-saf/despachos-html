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

#### Features Prioridade

- [x] Upload de planilhas para elaborar despachos;
- [x] Upload de Imagem;
- [ ] Despachos em lote;
- [ ] Carga de novos modelos;
- [x] Conversão HTML para PDF (WKHTMLTOX);
- [ ] Download de Bytes;
- [x] Múltiplos browsers;
- [x] Banco de Dados (SQLite + Excel);
- [ ] Gerencimanento de Histórico e Logs (opcional)
- [ ] Protótipo da Versão Web e da Versão Local

## 3. _How to Use_

```python
from safdocs import Despachos, Sqlite

sql = Sqlite()
despachos = Despachos(
    path_folder = 'templates/templates-financeiro', 
    path_converter = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
)

info_blank = {
    'timestamp': sql.timestamp(),
    'num_pagina': '1',
    'num_proc': '1122334/2023', 
    'destinatario': 'ÁREA TESTE', 
    'assunto_despacho': 'TESTE DE FUNCIONALIDADES', 
    'num_desp': '1/2023', 
    'area_texto': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing.',
    'area_tabela': despachos.convert_excel(filename = 'Teste Sistema.xlsx'),
    'area_img': despachos.upload_img(filename = 'hcm.jpg', h = 200),
    'data_despacho': 'São Luís, 25 de dezembro de 2023',
    'nome_colaborador': 'Jersiton Tiago Pereira Matos'
}

despachos.create(filename = 'example', table_name = 'blank', data = info_blank)
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