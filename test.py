from safdocs import Despachos, Sqlite

sql = Sqlite()
despachos = Despachos(path_folder = 'templates/templates-financeiro')

indicacao_conta = {
    'timestamp': sql.timestamp(),
    'num_pagina': '',
    'num_proc': '56489/2023', 
    'destinatario': 'FUNDO ESTADUAL DE SAÚDE', 
    'assunto_despacho': 'INDICAÇÃO DE CONTA', 
    'num_desp': '1906/2023', 
    'num_fonte': '1.6.05.405000', 
    'num_agencia': '3846-6',
    'num_conta': '9497-8',
    'info_recurso': 'Manutenção (Custeio) - Gestão do SUS - Assistência Financeira Complementar para Pagamento do Piso da Enfermagem', 
    'num_port': 'PORTARIA GM/MS Nº 2.031, DE 28 DE NOVEMBRO DE 2023', 
    'obj_port': 'Dispõe sobre os valores referentes à nona parcela do exercício de 2023, de que trata o Título IX-A da Portaria de Consolidação GM/MS nº 6, de 28 de setembro de 2017, relativos ao repasse da assistência financeira complementar.', 
    'data_despacho': 'São Luís, 25 de dezembro de 2023',
    'nome_colaborador': 'Jersiton Tiago Pereira Matos'
}

despachos.create(filename = 'piso_enfermagem', table_name = 'conta', data = indicacao_conta)
