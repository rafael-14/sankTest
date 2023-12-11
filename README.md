Utilizando o FastAPI
---
# Dependências
  
Utilize o `pip` para baixar as dependências do projeto:

``` shell
pip install fastapi[all] sqlalchemy uvicorn python-dotenv
```

# Banco de dados

A aplicação usa o **SQLite3** e criará automaticamente o banco de dados

# Execução

Para executar o servidor use:

``` shell
uvicorn main:app
```

O servidor estará escutando a porta 8000.
Para interomper a execução pressione «Ctrl»+«C».