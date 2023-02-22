import os
import pandas as pd

# Carrega o DataFrame com os nomes dos pokémons e seus números da Pokédex
pokedex_df = pd.read_csv('pokemon.csv')

# Define o diretório onde estão os arquivos a serem renomeados
dir_path = './images/'

# Percorre os arquivos no diretório
for filename in os.listdir(dir_path):
    if filename.endswith('.png'):
        try:
            # Obtém o número da Pokédex a partir do nome do arquivo
            pokedex_num = int(filename.split('.')[0])

            # Obtém o nome do pokémon correspondente ao número da Pokédex
            pokemon_name = pokedex_df.loc[pokedex_df['pokedex_number'] == pokedex_num, 'name'].iloc[0]

            # Define o novo nome do arquivo
            new_filename = f'{pokemon_name}.png'

            # Renomeia o arquivo
            os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))
        except:
            pass