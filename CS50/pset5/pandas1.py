import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

df = pd.read_sql_table('my_table', engine, columns=['ColA','ColB'])
