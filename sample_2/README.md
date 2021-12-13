# python mono repo sample_2 

## project setup

you have to install poetry 1.1.12 version

```bash
cd python-monorepo/sample_2
poetry install
poetry run python -m api
# access to localhost:8080/docs
``` 


## project structure

```
.
├── README.md
├── api
│   ├── README.md
│   ├── __main__.py
│   ├── api
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── tests
├── core
│   ├── README.md
│   ├── core
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── tests
├── database
│   ├── README.md
│   ├── database
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── tests
├── poetry.lock
└── pyproject.toml
```

`core`
Include domain, interface, service class here
This package has no depend

`database`
Include repository class here
This package has depend for `core`

`api`
Include fastapi setting and controller class here
This package has depend for `core` and `database`

