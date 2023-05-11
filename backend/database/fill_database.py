import psycopg2
import pandas as pd

from database import engine



# Charger le fichier CSV dans un DataFrame Pandas
df = pd.read_csv("database/car_pred.csv")

# Insérer les données dans les tables correspondantes

df = df.rename(columns={"Manufacturer": "name"})
df['name'].drop_duplicates().to_sql('manufacturers', con=engine, if_exists='append', index=False)

df = df.rename(columns={"Airbags": "airbags"})
df['airbags'].drop_duplicates().to_sql('airbags', con=engine, if_exists='append', index=False)

df = df.rename(columns={"Drive wheels": "drivewheel"})
df['drivewheel'].drop_duplicates().to_sql('drive_wheel', con=engine, if_exists='append', index=False)

df = df.rename(columns={"Gear box type" : "gearbox"})
df['gearbox'].drop_duplicates().to_sql('gear_box_type', con=engine, if_exists='append', index=False)

df = df.rename(columns={"Fuel type": "fuel"})
df['fuel'].drop_duplicates().to_sql('fuel_type', con=engine, if_exists='replace', index=False)

df = df.rename(columns={"Doors": "doors"})
df['doors'].drop_duplicates().to_sql('doors', con=engine, if_exists='append', index=False)

df = df.rename(columns={"Cylinders": "cylinders"})
df['cylinders'].drop_duplicates().to_sql('cylinders', con=engine, if_exists='append', index=False)

df = df.rename(columns={"Color": "color"})
df['color'].drop_duplicates().to_sql('colors', con=engine, if_exists='append', index=False)

df = df.rename(columns={"Model": "model"})
df['model'].drop_duplicates().to_sql('models', con=engine, if_exists='append', index=False)

df = df.rename(columns={"Category": "categorie"})
df['categorie'].drop_duplicates().to_sql('categories', con=engine, if_exists='append', index=False)

df = df.rename(columns={"Wheel": "wheel_pos"})
df['wheel_pos'].drop_duplicates().to_sql('wheel', con=engine, if_exists='append', index=False)




df = df.rename(columns={"Engine volume":"volume", "Turbo":"turbo"})
# Grouper les données par volume
grouped = df.groupby('volume')

# Créer une nouvelle DataFrame pour stocker les données finales
data = pd.DataFrame()

# Parcourir chaque groupe et ajouter les combinaisons avec le booléen à la DataFrame finale
for name, group in grouped:
    bool_combinations = pd.DataFrame({'volume': [name]*2, 'turbo': [True, False]})
    data = data.append(bool_combinations, ignore_index=True)

# Supprimer les doublons et insérer les données dans la table
data.drop_duplicates().to_sql('engine_volume', con=engine, if_exists='append', index=False)



# Fermer la connexion
engine.dispose()


