# python mono repo sample 

## what is this?

This is a sample to implement a multi-project structure in python.  
I am using poetry to manage my dependencies.  

## project setup

you have to install poetry 1.0.8 version

```bash
cd python-monorepo
poetry install
``` 

## generate new project

```bash
cd python-monorepo/projects
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

`lib`

Each lib specifies its dependencies.  
Each lib has its own dependencies.  


## reference

https://medium.com/opendoor-labs/our-python-monorepo-d34028f2b6fa
