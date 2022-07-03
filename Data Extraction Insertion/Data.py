#!/usr/bin/env python
# coding: utf-8

from application_logging.logger import App_Logger
from DatabaseConnection.Database import dataBaseOperation
import pandas as pd

logger = App_Logger('logFiles/Expo & Impo.log')

### Using Database ineurk

logger.info('INFO','Using The ineurk Database')

connection = dataBaseOperation()

logger.info('INFO','Creating The Connection With The DataStax Connection')


### Using Keyspace energy

logger.info('INFO','Using The energy Keyspace')
connection.useKeySpace()
logger.info('INFO','Using The energy Keyspace For Table Creation')

### Creating The Table

logger.info('INFO','Creating The Table With Name energies')
connection.createTable()
logger.info('INFO','Table Is Created Inside The Keyspace having a Name energies')


### Exporting  ENB2012_data.csv  File Into Database ineurk


logger.info('INFO','Trying To Put The Data Into The Database For Backup Purpose')
connection.insertIntoTable()
logger.info('INFO','The File Upload Into The Database')


### Getting The Data From The Database ineurk



logger.info('INFO','Trying To Get The Data Form The Database For EDA Purpose')
print(connection.getData())
logger.info('INFO','The Data Is Import Successfuly')


logger.info('INFO','Loading The Data Into Given IDE')
df = pd.DataFrame(connection.getData())
df_analysis=df.sort_values('id')

df_analysis

df_analysis.to_csv('Dataset/Analysis_Purpose.csv')






