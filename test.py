from safdocs import Despachos, Sqlite

sql = Sqlite()
despachos = Despachos(path_folder = 'templates/templates-financeiro')

infos_ind = {
    'timestamp': sql.timestamp(),
    'num_pagina': '20',
    'num_proc': '56489/2023', 
    'destinatario': 'FUNDO ESTADUAL DE SAÚDE', 
    'assunto_despacho': 'INDICAÇÃO DE CONTA', 
    'num_desp': '1877/2023', 
    'num_fonte': '1.6.00.301000', 
    'num_agencia': '3846-6',
    'num_conta': '8455-7', 
    'info_recurso': 'Manutenção (Custeio) - Atenção à População para Procedimentos no MAC', 
    'num_port': 'PORTARIA GM/MS Nº 25, DE 20 DE JANEIRO DE 2023', 
    'obj_port': 'Divulga os montantes anuais alocados aos Estados, Distrito Federal e Municípios, destinados ao cofinanciamento das ações e serviços públicos de saúde no grupo de atençãode média e alta complexidade ambulatorial e hospitalar (Teto MAC).', 
    'data_despacho': 'São Luís, 25 de dezembro de 2023',
    'nome_colaborador': 'Jersiton Tiago Pereira Matos'
}

infos_not = {
    'timestamp': sql.timestamp(),
    'num_pagina': '23',
    'num_proc': '45684/2023', 
    'destinatario': 'DEPARTAMENTO DE CONTRATOS E CONVÊNIOS', 
    'assunto_despacho': 'CIÊNCIA DE PAGAMENTO', 
    'num_desp': '1878/2023', 
    'fl_dci': '12',
    'data_despacho': 'São Luís, 25 de dezembro de 2023',
    'nome_colaborador': 'Jersiton Tiago Pereira Matos'
}

tables = {
    1: 'conta', 2: 'notificacao'
}

despachos.create(table_name = tables.get(1), data = infos_ind)
