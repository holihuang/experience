import pandas as pd, datetime as dt, sys;
from sqlalchemy import create_engine;

db, table  = sys.argv[1], sys.argv[2];
# 将后端字段映射成业务上的字段
# rename_map = {
#     'name': '书名',
#     'author': '作者'
# };
rename_map = {
    'name': '姓名',
    'age': '年龄',
    'sex': '性别'
};
outfile = f'{table}_{dt.date.today()}.xlsx';
# 拼 URI（格式：dialect+driver://user:pwd@host:port/db?charset=utf8mb4）
engine = create_engine(
    f"mysql+pymysql://root:root@localhost:3306/{db}?charset=utf8mb4"
)
df = pd.read_sql(f'select * from {table}', engine).rename(columns=rename_map);
print(df);
df.to_excel(outfile, index=False);
print('->', outfile, df.shape);
