'''Importar bibliotecas
    'csv' para leer archivos csv
    'matplotlib.pyplot' para generar gráficos'''
import csv
import matplotlib.pyplot as plt

'''Creamos una función que toma como argumentos la ruta del archivo CSV y los nombres de las columnas X y Y'''

def plot_bar_chart_from_csv(csv_path, x_column, y_column):

  '''Se crean listas vacías para almacenar los datos de las columnas X y Y'''  
  x_values = []
  y_values = []

  '''Se abre el archivo CSV y se lee el contenido'''
  with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
    
        '''Se itera sobre cada fila del archivo CSV'''
        for row in reader:
            x_values.append(row[x_column])
            y_values.append(float(row[y_column])) 

  plt.bar(x_values, y_values, color='blue')

  plt.xlabel(x_column)
  plt.ylabel(y_column)
  plt.title('Gráfico de Barras desde CSV')

  plt.show()

if __name__ == '__main__':
    csv_path = 'App/data.csv'
    x_column = 'Year'
    y_column = 'CO2_emission'

    plot_bar_chart_from_csv(csv_path, x_column, y_column)