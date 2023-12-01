# Despachos Automatizados com HTML, CSS e Python

## 1. _How to Use_

```
from safdocs import Despachos, Sqlite

sql = Sqlite()
despachos = Despachos(path_folder = 'templates/templates-financeiro')

indicacao = {
    'timestamp': sql.timestamp(),
    'num_pagina': '20',
    'num_proc': '56489/2023', 
    'destinatario': 'FUNDO ESTADUAL DE SAÚDE', 
    'assunto_despacho': 'INDICAÇÃO DE CONTA', 
    'num_desp': '1877/2023', 
    'num_fonte': '1.6.00.301000', 
    'num_agencia': '3846-6',
    'num_conta': '8455-7', 
    'info_recurso': 'Manutenção (Custeio) - Teto MAC', 
    'num_port': 'PORTARIA GM/MS Nº 25, DE 20 DE JANEIRO DE 2023', 
    'obj_port': 'Divulga os montantes anuais alocados aos Estados, Distrito Federal e Municípios, destinados ao cofinanciamento das ações e serviços públicos de saúde no grupo de atençãode média e alta complexidade ambulatorial e hospitalar (Teto MAC).', 
    'data_despacho': '25 de dezembro de 2023',
    'nome_colaborador': 'Jersiton Tiago Pereira Matos'
}

despachos.create(table_name = 'conta', data = indicacao)
```

## 2. To-do List

### Features

- Prioridades:
    - [ ] Upload de planilhas para elaborar despachos (complexa);
    - [ ] Despachos em lote (moderada);

- Outros:
    - [ ] Cálculos automáticos (fácil);
    - [ ] Carga de novos modelos (complexa);

### Infraestrutura

- [ ] Gerenciamento de binaries;
- [ ] Múltiplos browsers;
- [x] Banco de Dados (SQLite + Excel);
- [ ] Gerencimanento de Histórico e Logs

## 3. CRUD Sqlite

_Gerenciamento de tabelas com sqlite3._

```
from safdocs import Sqlite

sql = SqlController()

notificacao = {
    'timestamp': sql.timestamp(),
    'num_pagina': '250',
    'num_proc': '265453/2023', 
    'destinatario': 'DEPARTAMENTO DE CONTRATOS E CONVÊNIOS', 
    'assunto_despacho': 'CIÊNCIA E PROVIDÊNCIAS', 
    'num_desp': '1865/2023', 
    'texto_despacho': 'Encaminhamos os autos para ciência e providências conforme fl. XX.',
    'data_despacho': '25 de dezembro de 2023',
    'nome_colaborador': 'Jersiton Tiago Pereira Matos'
}

sql.create_insert('notificacao', notificacao) # gravando dados

print(sql.show_tables()) # tabelas 

print(sql.read(table_name = 'conta')) # dados List[Tuple]

sql.delete('conta', 'timestamp', '1701317738') # DELETE

sql.update('conta', 'timestamp', '1701317981', 'data_despacho', 'São Luís (MA), 25 de dezembro de 2023') # UPDATE

```
