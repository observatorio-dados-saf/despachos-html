
import streamlit as st
from safdocs import Despachos, Sqlite
from models import Models

sql = Sqlite()
despachos = Despachos(
    path_folder = 'templates/templates-financeiro', 
    path_converter = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
)

col1, col2 = st.columns(2)

with col1:

    lista_modelos = st.selectbox('Modelos', ['blank', 'regularizacao'])

    modelo = Models(lista_modelos)

    n_cols, names_cols = modelo.get_models()

    for i in names_cols:

        if i == 'timestamp':

            modelo.set_value('timestamp', st.text_input('timestamp', value = sql.timestamp()))

        elif 'tabela' in i:

            excel = st.file_uploader('area_tabela', 'xlsx')

            if excel is not None:

                modelo.set_value(
                    'area_tabela', 
                    despachos.convert_excel(
                        
                    )
                )

        # elif 'img' in i:
# 
        #     up_img = st.file_uploader('area_img', ['jpg', 'png'])
# 
        #     if up_img is not None:
# 
        #         modelo.set_value(
        #             'area_img', 
        #             despachos.upload_img(
        #                 up_img, h = 200
        #             )
        #         )
# 
        else:

            modelo.set_value(i, st.text_input(i))

with col2:

    st.json(modelo())

    file = st.text_input('Nome do Arquivo')

    criar = st.button('Gerar Documento')

    if criar:

        despachos.create(
            filename = file, table_name = lista_modelos, data = modelo()
        )

        st.success('Arquivo gerado com sucesso!')
