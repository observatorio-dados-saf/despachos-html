
import json

class Models():
    '''
    classe que gerencia os campos de cada documento .html
    Parâmetros:
        - name_model: nome do arquivo .html
    '''
    def __init__(self, name_model: str) -> None:
        self.name_model = name_model
        self.models = {
            'blank': [
                'timestamp', 'num_pagina', 'num_proc', 'destinatario', 'assunto_despacho',
                'num_desp', 'area_texto', 'area_tabela', 'area_img', 'data_despacho',
                'nome_colaborador'
            ],
            'regularizacao': [
                'timestamp', 'num_pagina', 'num_proc', 'destinatario', 
                'assunto_despacho', 'num_desp', 'data_despacho', 'nome_colaborador'
            ]
        }
        self.dictionary = {k: '' for k in self.models.get(self.name_model)}

    def __str__(self) -> str:
        '''exibe o estado atual do dicionário'''
        return json.dumps(self.dictionary, indent = 2)
    
    def __call__(self) -> dict:
        '''retorna o dicionário como uma chamada de função'''
        return self.dictionary
    
    def get_models(self) -> list:
        '''retorna os campos a partir do valor de name_model e o seu tamanho'''
        columns = self.models.get(self.name_model)
        return len(columns), columns
    
    def set_value(self, key_: str, value_: str) -> None:
        '''
        seta valores no dicionário desde que existam no modelo
        Parâmetros:
            - key_: chave a ser editada
            - value_: novo valor
        '''
        if key_ in self.models.get(self.name_model):
            self.dictionary.update({key_: value_})

    def set_values(self, values_: list) -> None:
        '''
        seta todos os valores do dicionário
        Parâmetros:
            - values_: uma lista de valores
        '''
        n_col, names_ = self.get_models()
        for i in range(n_col):
            try:
                self.dictionary.update({names_[i]: values_[i]})
            except:
                pass