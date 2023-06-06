#!/usr/bin/env python
# coding: utf-8

from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import GridSearchCV
import category_encoders as ce
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from sqlalchemy import create_engine
import psycopg2
import pandas as pd


def prediction_with_csv():
    df = pd.read_csv('./backend/database/car_pred.csv', sep=',')
    df["Levy"] = df["Levy"].str.replace("-", "0")
    df['Levy'] = df['Levy'].astype(int)
    df["Mileage"] = df["Mileage"].str.replace(" km", "")
    df['Mileage'] = df['Mileage'].astype(int)
    df = df.loc[(df['Price'] > 1000) & (df['Price'] < 1000000)]
    df['Prod. year'] = pd.to_datetime(df['Prod. year'], format='%Y')
    df['Prod. year'] = df['Prod. year'].dt.year
    df["Doors"] = df["Doors"].str.replace(
        "-May", "").str.replace("-Mar", "").str.replace(">", "")
    df['Doors'] = df['Doors'].astype(int)
    df['Turbo'] = df['Engine volume'].apply(lambda x: 'Turbo' in x)
    df["Engine volume"] = df["Engine volume"].str.replace(" Turbo", "")
    df['Engine volume'] = df["Engine volume"].astype(float)
    df['Leather interior'] = df['Leather interior'].map(
        {'Yes': True, 'No': False})
    df['Wheel'] = df['Wheel'].map(
        {'Left wheel': True, 'Right-hand drive': False})
    df = df.drop_duplicates()

    pd.set_option('display.max_rows', None)

    df["Levy"] = df["Levy"].str.replace("-", "0")
    df['Levy'] = df['Levy'].astype(int)
    # df

    print(df['Fuel type'].value_counts())

    # Calculer le nombre de valeurs uniques pour chaque valeur de la colonne
    value_counts = df['Manufacturer'].value_counts()

    # Filtrer le résultat pour garder seulement les valeurs avec un nombre de valeurs uniques inférieur à 100
    selected_values = value_counts[value_counts < 100]

    # Afficher les valeurs sélectionnées
    print(selected_values.index.tolist())

    df.dtypes

    df["Mileage"] = df["Mileage"].str.replace(" km", "")
    df['Mileage'] = df['Mileage'].astype(int)

    df = df.loc[(df['Price'] > 1000) & (df['Price'] < 1000000)]

    df['Prod. year'] = pd.to_datetime(df['Prod. year'], format='%Y')
    df['Prod. year'] = df['Prod. year'].dt.year

    df["Doors"] = df["Doors"].str.replace(
        "-May", "").str.replace("-Mar", "").str.replace(">", "")
    df['Doors'] = df['Doors'].astype(int)

    df['Turbo'] = df['Engine volume'].apply(lambda x: 'Turbo' in x)

    df["Engine volume"] = df["Engine volume"].str.replace(" Turbo", "")
    df['Engine volume'] = df["Engine volume"].astype(float)

    df['Leather interior'] = df['Leather interior'].map(
        {'Yes': True, 'No': False})

    df['Wheel'] = df['Wheel'].map(
        {'Left wheel': True, 'Right-hand drive': False})

    df = df.drop_duplicates()

    print(df['Manufacturer'].unique())
    print(df['Model'].unique())
    print(df['Category'].unique())
    print(df['Fuel type'].unique())
    print(df['Gear box type'].unique())
    print(df['Drive wheels'].unique())
    print(df['Color'].unique())

    print(df.Manufacturer.nunique())
    print(df.Model.nunique())
    print(df.Category.nunique())
    print(df['Fuel type'].nunique())
    print(df['Gear box type'].nunique())
    print(df['Drive wheels'].nunique())
    print(df['Color'].nunique())

    # Enregistrement Dataset
    df.to_csv('car_pred.csv', index=False)

    # OBSERVATION :
    #
    # Remplacement des tirets "-" de la colonne "Levy" par la médiane (Ugo)
    # Kilometrage "Mileage" entre 0 & 1 000 000 (Quentin)
    # Retirer type de fuel electric (juste une seule valeur)
    # Potentiellment retirer les encoding de l'alphabet géorgien
    # Manufacturer, valeurs faible (1 seul véhicule TESLA)
    #

    ("columns={'Manufacturer':'name'}")

    # Connexion à la base de données
    engine = create_engine('postgresql://postgres:0000@localhost:5432/carpred')

    # Charger le fichier CSV dans un DataFrame Pandas
    df = pd.read_csv("./backend/database/car_pred.csv")

    # Insérer les données dans les tables correspondantes

    df = df.rename(columns={"Manufacturer": "name"})
    df['name'].drop_duplicates().to_sql('manufacturers', con=engine,
                                        if_exists='append', index=False)

    df = df.rename(columns={"Airbags": "nb_airbag"})
    df['nb_airbag'].drop_duplicates().to_sql(
        'airbags', con=engine, if_exists='append', index=False)

    df = df.rename(columns={"Drive wheels": "dw_type"})
    df['dw_type'].drop_duplicates().to_sql('drive_wheel', con=engine,
                                           if_exists='append', index=False)

    df = df.rename(columns={"Gear box type": "gb_type"})
    df['gb_type'].drop_duplicates().to_sql('gear_box_type', con=engine,
                                           if_exists='append', index=False)

    df = df.rename(columns={"Fuel type": "f_type"})
    df['f_type'].drop_duplicates().to_sql('fuel_type', con=engine,
                                          if_exists='replace', index=False)

    df = df.rename(columns={"Doors": "nb_door"})
    df['nb_door'].drop_duplicates().to_sql(
        'doors', con=engine, if_exists='append', index=False)

    df = df.rename(columns={"Cylinders": "nb_cylinder"})
    df['nb_cylinder'].drop_duplicates().to_sql(
        'cylinders', con=engine, if_exists='append', index=False)

    df = df.rename(columns={"Color": "color"})
    df['color'].drop_duplicates().to_sql(
        'colors', con=engine, if_exists='append', index=False)

    df = df.rename(columns={"Model": "model_name"})
    df['model_name'].drop_duplicates().to_sql(
        'models', con=engine, if_exists='append', index=False)

    df = df.rename(columns={"Category": "category_name"})
    df['category_name'].drop_duplicates().to_sql(
        'categories', con=engine, if_exists='append', index=False)

    df = df.rename(columns={"Wheel": "wheel_pos"})
    df['wheel_pos'].drop_duplicates().to_sql(
        'wheel', con=engine, if_exists='append', index=False)

    df = df.rename(columns={"Engine volume": "volume", "Turbo": "turbo"})
    # Grouper les données par volume
    grouped = df.groupby('volume')

    # Créer une nouvelle DataFrame pour stocker les données finales
    data = pd.DataFrame()

    # Parcourir chaque groupe et ajouter les combinaisons avec le booléen à la DataFrame finale
    for name, group in grouped:
        bool_combinations = pd.DataFrame(
            {'volume': [name]*2, 'turbo': [True, False]})
        data = data.append(bool_combinations, ignore_index=True)

    # Supprimer les doublons et insérer les données dans la table
    data.drop_duplicates().to_sql('engine_volume', con=engine,
                                  if_exists='append', index=False)

    # Fermer la connexion
    engine.dispose()

    pd.__version__

    ("columns={'Manufacturer':'name'}")

    # Appliquer l'encodage one-hot à la colonne "cat_col"
    df['Num_Category'] = df['Category'].astype('category').cat.codes

    # grouper les données par nom de catégorie
    grouped = df.groupby('Category')

    # parcourir chaque groupe et vérifier si chaque groupe a une seule valeur pour la colonne 'Num_Category'
    for name, group in grouped:
        num_categories = group['Num_Category'].unique()
        if len(num_categories) > 1:
            print(
                f"La catégorie '{name}' a plusieurs valeurs pour la colonne 'Num_Category': {num_categories}")
        else:
            print(
                f"La catégorie '{name}' a la valeur unique {num_categories[0]} pour la colonne 'Num_Category'")

    encoder = OrdinalEncoder()

    df[['Marque', 'Modèle', 'Num_Category']] = encoder.fit_transform(
        df[['Manufacturer', 'Model', 'Category']])

    # grouper les données par nom de catégorie
    grouped = df.groupby('Category')

    # parcourir chaque groupe et vérifier si chaque groupe a une seule valeur pour la colonne 'Num_Category'
    for name, group in grouped:
        num_categories = group['Num_Category'].unique()
        if len(num_categories) > 1:
            print(
                f"La catégorie '{name}' a plusieurs valeurs pour la colonne 'Num_Category': {num_categories}")
        else:
            print(
                f"La catégorie '{name}' a la valeur unique {num_categories[0]} pour la colonne 'Num_Category'")
    df.corr()

    # # Diviser les données en variables de caractéristiques et de cible
    # X = df[['Prod. year','Engine volume','Mileage','Cylinders','Doors','Airbags','Turbo','Manufacturer','Category']]  # toutes les colonnes sauf "price"
    # y = df['Price']  # la colonne "price" est notre cible

    X = df.drop(['ID', 'Price', 'Levy'], axis=1)
    y = df['Price']

    # Encoder les variables catégorielles
    label_encoder = LabelEncoder()
    X['Manufacturer'] = label_encoder.fit_transform(X['Manufacturer'])

    onehot_encoder = ce.OneHotEncoder(cols=['Category'])
    X = onehot_encoder.fit_transform(X)

    # Charger les données et les diviser en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Sélectionner les features et la variable cible
    X = df.drop(['ID', 'Price'], axis=1)
    y = df['Price']

    # Encoder les variables catégorielles
    onehot_encoder = ce.OneHotEncoder(
        cols=['Manufacturer', 'Category', 'Model'])
    ordinal_encoder = ce.OrdinalEncoder(
        cols=['Fuel type', 'Gear box type', 'Drive wheels', 'Color'])

    X = onehot_encoder.fit_transform(X)
    X = ordinal_encoder.fit_transform(X)

    # Charger les données et les diviser en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    ("'Levy',", "'Model'")

    lr = LinearRegression()
    lr.fit(X_train, y_train)

    dt = DecisionTreeRegressor(random_state=0)
    dt.fit(X_train, y_train)

    rf = RandomForestRegressor(n_estimators=100, random_state=0)
    rf.fit(X_train, y_train)

    # RESULTS 2 ENCODES ONE-HOT ORDINAL SANS LEVY SANS MODEL
    y_pred_lr = lr.predict(X_test)
    mse_lr = mean_squared_error(y_test, y_pred_lr)
    r2_lr = r2_score(y_test, y_pred_lr)
    print('Linear regression :')
    print('R²:', r2_lr)
    print('MSE:', mse_lr)

    y_pred_dt = dt.predict(X_test)
    mse_dt = mean_squared_error(y_test, y_pred_dt)
    r2_dt = r2_score(y_test, y_pred_dt)
    print('Decision Tree :')
    print('R²:', r2_dt)
    print('MSE:', mse_dt)

    y_pred_rf = rf.predict(X_test)
    mse_rf = mean_squared_error(y_test, y_pred_rf)
    r2_rf = r2_score(y_test, y_pred_rf)
    print('Random Forest :')
    print('R²:', r2_rf)
    print('MSE:', mse_rf)

    # RESULTS 2 ENCODES ONE-HOT ORDINAL AVEC LEVY SANS MODEL
    y_pred_lr = lr.predict(X_test)
    mse_lr = mean_squared_error(y_test, y_pred_lr)
    r2_lr = r2_score(y_test, y_pred_lr)
    print('Linear regression :')
    print('R²:', r2_lr)
    print('MSE:', mse_lr)

    y_pred_dt = dt.predict(X_test)
    mse_dt = mean_squared_error(y_test, y_pred_dt)
    r2_dt = r2_score(y_test, y_pred_dt)
    print('Decision Tree :')
    print('R²:', r2_dt)
    print('MSE:', mse_dt)

    y_pred_rf = rf.predict(X_test)
    mse_rf = mean_squared_error(y_test, y_pred_rf)
    r2_rf = r2_score(y_test, y_pred_rf)
    print('Random Forest :')
    print('R²:', r2_rf)
    print('MSE:', mse_rf)

    # RESULTS 2 ENCODES ONE-HOT ORDINAL AVEC LEVY AVEC MODEL
    y_pred_lr = lr.predict(X_test)
    mse_lr = mean_squared_error(y_test, y_pred_lr)
    r2_lr = r2_score(y_test, y_pred_lr)
    print('Linear regression :')
    print('R²:', r2_lr)
    print('MSE:', mse_lr)

    y_pred_dt = dt.predict(X_test)
    mse_dt = mean_squared_error(y_test, y_pred_dt)
    r2_dt = r2_score(y_test, y_pred_dt)
    print('Decision Tree :')
    print('R²:', r2_dt)
    print('MSE:', mse_dt)

    y_pred_rf = rf.predict(X_test)
    mse_rf = mean_squared_error(y_test, y_pred_rf)
    r2_rf = r2_score(y_test, y_pred_rf)
    print('Random Forest :')
    print('R²:', r2_rf)
    print('MSE:', mse_rf)

    # Définir les modèles à entraîner et les paramètres à tester
    models = [
        {
            'name': 'Random Forest',
            'estimator': RandomForestRegressor(),
            'hyperparameters': {
                'n_estimators': [10, 50, 100],
                'max_depth': [1, 2, 3, 4, 5, 10],
                'min_samples_split': [2, 3, 4]
            },
        },
    ]

    # Entraîner les modèles et sélectionner le meilleur modèle
    for model in models:
        print(f'Training {model["name"]}...')
        grid = GridSearchCV(model['estimator'], model['hyperparameters'], cv=5)
        grid.fit(X_train, y_train)
        model['best_params'] = grid.best_params_
        model['best_score'] = grid.best_score_
        model['best_estimator'] = grid.best_estimator_

    # Sélectionner le modèle avec le meilleur score
    best_model = max(models, key=lambda x: x['best_score'])
    print(f'Best model: {best_model["name"]}')
    print(f'Best score: {best_model["best_score"]:.2f}')
    print(f'Best parameters: {best_model["best_params"]}')

    print('R²:', r2_score(y_test, y_pred))
    print('MSE:', mean_squared_error(y_test, y_pred))

    # Résultat de base SANS MARQUE & LEVY
    print("Linear Regression:")
    print("MSE: ", mse_lr)
    print("R2 score: ", r2_lr)

    print("Decision Tree:")
    print("MSE: ", mse_dt)
    print("R2 score: ", r2_dt)

    print("Random Forest:")
    print("MSE: ", mse_rf)
    print("R2 score: ", r2_rf)

    #     {
    #         'name': 'Linear Regression',
    #         'estimator': LinearRegression(),
    #         'hyperparameters': {},
    #     },
    #     {
    #         'name': 'Decision Tree',
    #         'estimator': DecisionTreeRegressor(),
    #         'hyperparameters': {
    #             'max_depth': [1, 2, 3, 4, 5],
    #             'min_samples_split': [2, 3, 4]
    #         },
    #     },

    # BEST SCORE & RESULTS

    # Charger les données et les diviser en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Définir les modèles à entraîner et les paramètres à tester
    models = [
        {
            'name': 'Linear Regression',
            'estimator': LinearRegression(),
            'hyperparameters': {},
        },
        {
            'name': 'Decision Tree',
            'estimator': DecisionTreeRegressor(),
            'hyperparameters': {
                'max_depth': [1, 2, 3, 4, 5],
                'min_samples_split': [2, 3, 4]
            },
        },
        {
            'name': 'Random Forest',
            'estimator': RandomForestRegressor(),
            'hyperparameters': {
                'n_estimators': [10, 50, 100],
                'max_depth': [1, 2, 3, 4, 5],
                'min_samples_split': [2, 3, 4]
            },
        },
    ]

    # Entraîner les modèles et sélectionner le meilleur modèle
    for model in models:
        print(f'Training {model["name"]}...')
        grid = GridSearchCV(model['estimator'], model['hyperparameters'], cv=5)
        grid.fit(X_train, y_train)
        model['best_params'] = grid.best_params_
        model['best_score'] = grid.best_score_
        model['best_estimator'] = grid.best_estimator_

    # Sélectionner le modèle avec le meilleur score
    best_model = max(models, key=lambda x: x['best_score'])
    print(f'Best model: {best_model["name"]}')
    print(f'Best score: {best_model["best_score"]:.2f}')
    print(f'Best parameters: {best_model["best_params"]}')

    # BEST SCORE MODELE 2 ENCODING SANS LEVY AVEC MODEL : 0.31
    # BEST SCORE MODELE 2 ENCODING AVEC LEVY SANS MODEL : 0.39
    # BEST SCORE MODELE 2 ENCODING SANS LEVY SANS MODEL : 0.40
    # BEST SCORE MODELE 2 ENCODING AVEC LEVY AVEC MODEL : 0.36
    return predictions.tolist()
