# Snowballing scripts

Contém conjunto de scripts para apoiar a minha extração de dados para a constrção de uma modelo de snowballing no Stack Exchange (SE).

## Dependências

* Python 3 ou superior
* Postgres 16 ou superior

## Montando ambiente

* Criando ambiente local
```
python3 -m venv myenv
```

* Ativando ambiente
```
source myenv/bin/activate (Linux/MacOS)
myenv\Scripts\activate (Windows)
```

* Instalando pacotes no ambiente
```
pip install -r requirements.txt
```

## Links interessantes

Documentação do schema do SE

https://meta.stackexchange.com/questions/2677/database-schema-documentation-for-the-public-data-dump-and-sede

Links sobre links Related

https://meta.stackexchange.com/questions/20473/how-are-related-questions-selected

https://stackoverflow.blog/2008/10/17/stack-overflow-search-now-51-less-crappy/

https://stackoverflow.blog/2010/04/26/new-linked-posts/?_ga=2.201252078.1532454634.1711292722-150477141.1684451486
