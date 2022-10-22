#!/usr/bin/env python
# coding: utf-8

# # Atividade 10

# In[ ]:


import psycopg2


# In[ ]:


import csv


# In[ ]:


conn = psycopg2.connect(database="loja10DB",
                        user='postgres', password='postgres', 
                        host='127.0.0.1', port='5432'
)


# In[ ]:


conn.autocommit = True
cur = conn.cursor()


# In[ ]:


sql = '''CREATE TABLE VENDAS (idvenda serial NOT NULL,idproduto int NOT NULL
,idvendedor int NOT NULL,valortotal decimal(7,2) NOT NULL,comissao decimal(6,2) NOT NULL,idfornecedor int NOT NULL);'''


# In[ ]:


cur.execute(sql)


# In[ ]:


sql2 = '''COPY 
        vendas(idproduto, idvendedor, valortotal, comissao, idfornecedor)
        FROM '\Cursos\SoulCode\Vendas.csv' DELIMITER ',' CSV HEADER;'''


# In[ ]:


cur.execute(sql2)


# In[ ]:


sql3 = '''select * from details;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)


# In[ ]:


conn.commit()
conn.close()


# In[ ]:




