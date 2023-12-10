
from safdocs import Despachos, Sqlite
from models import Models

sql = Sqlite()
despachos = Despachos(
    path_folder = 'templates/templates-financeiro', 
    path_converter = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
)

modelo = Models('regularizacao')
print(modelo.get_models())
modelo.set_values([sql.timestamp(), '20', '1654/2023', 'Execução', 'Regularização', '1564/2023', 'São Luís, 25 de dezembro', 'Jersiton Matos'])
print(modelo)

# despachos.create(filename = 'example', table_name = 'regularizacao', data = modelo())
