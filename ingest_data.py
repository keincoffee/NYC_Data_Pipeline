#!/usr/bin/env python
# coding: utf-8

#import libraries

import os       
import argparse
import pandas as pd
from sqlalchemy import create_engine
from time import time


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    
    parquet_name = 'output.parquet'
    csv_name = 'output.csv'

    #download parquet

    os.system(f'wget {url} -O {parquet_name}')

    #connect to postgres container using SQLalchemy
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    #convert parquet to csv
    df = pd.read_parquet(parquet_name)
    df.to_csv(csv_name, index=False)

    #read csv data into a dataframe with chunksize set
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    df = next(df_iter)

    #convert pickup_datetime and dropoff_datetime to timestamps
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    #load columns to postgresql
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    #load data to postgres
    df.to_sql(name=table_name, con=engine, if_exists='append')

    #loop to load data into postgres
    while True:
        t_start = time()
        df = next(df_iter)
    
        #convert pickup_datetime and dropoff_datetime to timestamps
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    
        #load data to postgres
        df.to_sql(name=table_name, con=engine, if_exists='append')
    
        t_end = time()
    
        #print confirmation and time elapsed
        print('inserted another chunk..., took %.3f second' %(t_end - t_start))


if __name__ == '__main__':
    #setup argparse
    parser = argparse.ArgumentParser(description = 'Convert parquet to CSV and Ingest CSV to Postgres')

    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of table where we will write the results to')
    parser.add_argument('--url', help='url of parquet file')

    args = parser.parse_args()

    main(args)

