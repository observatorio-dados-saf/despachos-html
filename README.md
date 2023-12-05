# Despachos Automatizados com HTML, CSS e Python

## 1. _How to Use_

```python
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

> Obs: _cabeçalhos e rodapés: False, elementos gráficos: True_

## 2. To-do List

### Features

- Prioridades:
    - [ ] Upload de planilhas para elaborar despachos (complexa);
    - [ ] Upload de Imagem;
    - [ ] Despachos em lote (moderada);

- Outros:
    - [ ] Cálculos automáticos (fácil);
    - [ ] Carga de novos modelos (complexa);

### Infraestrutura

- [ ] Gerenciamento de binaries;
- [x] Múltiplos browsers;
- [x] Banco de Dados (SQLite + Excel);
- [ ] Gerencimanento de Histórico e Logs (Opcional)

## 3. CRUD Sqlite

_Gerenciamento de tabelas com sqlite3._

```python
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

## 4. Tabela de FontSizing

| Points  | Pixels  |   Ems    |    %    |
|:--------:|:--------:|:---------:|:--------:|
| 6pt     | 8px     | 0.5em    | 50%     |
| 7pt     | 9px     | 0.55em   | 55%     |
| 7.5pt   | 10px    | 0.625em  | 62.5%   |
| 8pt     | 11px    | 0.7em    | 70%     |
| 9pt     | 12px    | 0.75em   | 75%     |
| 10pt    | 13px    | 0.8em    | 80%     |
| 10.5pt  | 14px    | 0.875em  | 87.5%   |
| 11pt    | 15px    | 0.95em   | 95%     |
| 12pt    | 16px    | 1em      | 100%    |
| 13pt    | 17px    | 1.05em   | 105%    |
| 13.5pt  | 18px    | 1.125em  | 112.5%  |
| 14pt    | 19px    | 1.2em    | 120%    |
| 14.5pt  | 20px    | 1.25em   | 125%    |
| 15pt    | 21px    | 1.3em    | 130%    |
| 16pt    | 22px    | 1.4em    | 140%    |
| 17pt    | 23px    | 1.45em   | 145%    |
| 18pt    | 24px    | 1.5em    | 150%    |
| 20pt    | 26px    | 1.6em    | 160%    |
| 22pt    | 29px    | 1.8em    | 180%    |
| 24pt    | 32px    | 2em      | 200%    |
| 26pt    | 35px    | 2.2em    | 220%    |
| 27pt    | 36px    | 2.25em   | 225%    |
| 28pt    | 37px    | 2.3em    | 230%    |
| 29pt    | 38px    | 2.35em   | 235%    |
| 30pt    | 40px    | 2.45em   | 245%    |
| 32pt    | 42px    | 2.55em   | 255%    |
| 34pt    | 45px    | 2.75em   | 275%    |
| 36pt    | 48px    | 3em      | 300%    |
