from safdocs import Despachos, Sqlite

sql = Sqlite()
despachos = Despachos(
    path_folder = 'templates/templates-financeiro', 
    path_converter = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
)

indicacao = {
    'timestamp': sql.timestamp(),
    'num_pagina': '20',
    'num_proc': '56489/2023', 
    'destinatario': 'FUNDO ESTADUAL DE SAÚDE', 
    'assunto_despacho': 'INDICAÇÃO DE CONTA', 
    'num_desp': '1877/2023', 
    'num_fonte': '1.6.05.405000', 
    'num_agencia': '3846-6',
    'num_conta': '9497-8', 
    'info_recurso': 'Manutenção (Custeio) - Gestão do SUS - Assistência Financeira Complementar para Pagamento do Piso da Enfermagem', 
    'num_port': 'PORTARIA GM/MS Nº 2.031, DE 28 DE NOVEMBRO DE 2023', 
    'obj_port': 'Dispõe sobre os valores referentes à nona parcela do exercício io de 2023, de que trata o Tıt́ulo IX-A da Portaria de Consolidação GM/MS nº 6, de 28 de setembro de 2017, relativos ao repasse da assistência financeira complementar.',
    'data_despacho': 'São Luís, 25 de dezembro de 2023',
    'nome_colaborador': 'Jersiton Tiago Pereira Matos'
}

despachos.create(filename = 'Indicação Teste Piso', table_name = 'conta', data = indicacao)
