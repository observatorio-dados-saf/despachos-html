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
    'area_tabela': despachos.convert_excel(filename = 'data/Teste Sistema.xlsx'),
    'area_img': despachos.upload_img(filename = 'data/hcm.jpg', h = 200),
    'data_despacho': 'São Luís, 25 de dezembro de 2023',
    'nome_colaborador': 'Jersiton Tiago Pereira Matos'
}

despachos.create(filename = 'example', table_name = 'blank', data = info_blank)
