# python mono repo sample_1 

## project setup

you have to install poetry 1.0.8 version

```bash
cd python-monorepo/sample_1
poetry install
``` 

## generate new project

```bash
cd python-monorepo/sample_1/projects
poetry new {new project name}
cd {new project name}
poetry add ./../../libs/{project dependency lib module name}
```


## project structure

```
.
├── README.md
├── libs
│   ├── lib-one
│   └── logger
├── poetry.lock
├── projects
│   ├── __init__.py
│   ├── project-one
│   └── project-two
└── pyproject.toml
```

`/projects`

Project code (Python modules) go here.  
Each project has its own dependencies.  

`/libs`

Each lib specifies its dependencies.  
Each lib has its own dependencies.  


## reference

https://medium.com/opendoor-labs/our-python-monorepo-d34028f2b6fa
