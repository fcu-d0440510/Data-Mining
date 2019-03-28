import pandas as pd

#要先記事本另存utf-8，再讀入googleplaystore.csv檔
df = pd.read_csv('googleplaystore.csv', encoding='utf-8')

#刪除缺值的row
df = df.dropna()
#刪除整個row重複的，保留第一次出現
df = df.drop_duplicates(keep='first')

#保存修改過後的mod_file.csv檔
df.to_csv('mod_file.csv', index=False, encoding='utf_8_sig')
