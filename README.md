check it -> config.py

```python
class Settings(BaseSettings):
    db_name = "xxx"
    db_host = 'x.x.x.x'
    db_port = 0000
    db_user = 'xxx'
    db_password = 'xxx'
```

run it

```
$ uvicorn main:app --reload
```

get it -> http://127.0.0.1:8000/check_db_connection