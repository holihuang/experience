import pandas as pd, datetime as dt, sys;
from sqlalchemy import create_engine;

db, table  = sys.argv[1], sys.argv[2];
rename_map = {
    'name': '书名',
    'author': '作者'
};
outfile = f'{table}_{dt.date.today()}.xlsx';
engine = create_engine(
    f"mysql+pymysql://root:root@localhost:3306/{db}?charset=utf8mb4"
)
df = pd.read_sql(f'select * from {table}', engine).rename(columns=rename_map);
print(df);
df.to_excel(outfile, index=False);
print('->', outfile, df.shape);
