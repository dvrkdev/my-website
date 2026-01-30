# my-website

> [!TIP]
> How to create a `SECRET_KEY` for a project?
>
```python
from secrets import token_hex
print(token_hex())
```

> [!TIP]
> How to create tables?
>
```bash
flask shell
```
```python
from app.extensions import db
db.create_all()
```
```bash
ls instance/default.db
```
