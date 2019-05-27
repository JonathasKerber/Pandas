#   Example of how to access and manipulate large datasets
#   with pandas
#   Reference: https://www.youtube.com/watch?v=xKMyk4wDHnQ

#   IMPORT PACKAGES AND MODULES
import numpy as np
import pandas as pd
import sqlite3
from sqlalchemy import create_engine


#   SET DATA DIRECTORY
DIR = '../documents/dataset/'
FILE_ALL = 'dispensacoes-all.csv'

file_all = DIR + FILE_ALL

print("Files to be processed", file_all)

#   PRINT THE HEAD OF THE DATASET
print(pd.read_csv(file_all, nrows=2))

#   CREATING A CONNECTOR TO THE DATABASE
print("Database: CREATING CONNECTION")
dispensacoesAll = create_engine('sqlite:///dispensacoesAll.db')
print("Database: CONNECTION CREATED")

print("Database: LOADING...")

#   LOADING THE FULL DATASET AT ONCE
#dispensacoes = pd.read_csv(file_all, header=0, encoding="iso-8859-1")

#   LOADING THE DATASET BY THE CHUNKS
chunksize = 35000       #   NUMBER OF ROWS TO BE READ AT EACH ITERACTION. SINCE THE EXAMPLE FILE I'M USING HAS ~3500000 REGISTERS, I WILL LOAD IT IN CHUNKS OF ~1% OF ITS SIZE.


dispensacoesTemp = []
queryTemp = []
query = pd.DataFrame()

for dispensacoes in pd.read_csv(file_all, header=0, chunksize=chunksize, encoding="iso-8859-1", iterator=True):#, low_memory=False):

    #REPLACING BLANK SPACES AT COLUMNS' NAMES FOR SQL OPTIMIZATION
    dispensacoes = dispensacoes.rename(columns = {c: c.replace(' ', '') for c in dispensacoes.columns})

    #BUFFERING CHUNKS
    dispensacoesTemp.append(dispensacoes)

    #DO YOUR DATA PROCESSING HERE
    query = dispensacoes[dispensacoes["Medicamento"].str.startswith('DIPIRONA')]   
    #BUFFERING PROCESSED DATA
    queryTemp.append(query)
    
#!  NEVER DO pd.concat OR pd.DataFrame() INSIDE A LOOP
print("Database: CONCATENATING CHUNKS INTO A SINGLE DATAFRAME")
dispensacoes = pd.concat(dispensacoesTemp)
print("Database: LOADED")

print("Database: DATAFRAME INFO")
print("\tCOLUMNS:", dispensacoes.columns)
print("\tSIZE:", dispensacoes.size)
print("\tSHAPE (Registers, Columns):", dispensacoes.shape)
print("\tDIMENSIONS:", dispensacoes.ndim)

print('-' * 30 + "QUERY TEST" + '-' * 30)
query = pd.concat(queryTemp)
print(query)
print("Database: QUERY DATAFRAME INFO")
print("\tCOLUMNS:", query.columns)
print("\tSIZE:", query.size)
print("\tSHAPE (Registers, Columns):", query.shape)
print("\tDIMENSIONS:", query.ndim)

