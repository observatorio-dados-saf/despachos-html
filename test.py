
from safdocs import Documentos, Sqlite
from models import Modelos

sql = Sqlite()
docs = Documentos(
    path_folder = 'templates/templates-financeiro', 
    path_converter = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
)

modelo = Modelos('regularizacao')
print(modelo.get_models())
modelo.set_values([sql.timestamp(), '20', '1654/2023', 'Execução', 'Regularização', '1564/2023', 'São Luís, 25 de dezembro', 'Jersiton Matos'])
print(modelo)

docs.create(filename = 'example', table_name = 'regularizacao', data = modelo())
