from safdocs import Despachos, Sqlite

sql = Sqlite()
despachos = Despachos(path_folder = 'templates/templates-financeiro')

despachos.html_to_pdf(
    html_name = 'piso_enfermagem_conta_1701740936.html',
    pdf_name = 'teste_despacho.pdf'
)
