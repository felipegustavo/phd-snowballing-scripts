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

## Conceitos

### Linked Backward Snowballing

Lista de posts fora do starset que são apontados por algum post dentro do starset via um link do tipo linked.

hits = quantidade de vezes que um post X, fora do dataset, foi apontado por um post dentro do startset via um lined link. Por exemplo, os posts 26070, 28023 e 29724 estão no startset e eles tem um linked link apontando para o post 26011, que está fora do startset, logo o post 26011 tem 3 hits.

### Linked Forward Snowballing

Lista de posts fora do startset que têm algum link do tipo linked que aponta para um post no startset.

hits = quantidade de links que um post X tem que apontam para o startset. Por exemplo, o post 27453 (que se encontra fora do startset) tem dois links apontando para 7904 e 16361 (ambos partes do starset), logo o post 27453 tem 2 hits.

### Related Backward Snowballing

Lista de posts fora do starset que são apontados por algum post dentro do starset via um link do tipo related.

hits = quantidade de vezes que um post X, fora do dataset, foi apontado por um post dentro do startset via um related link. Por exemplo, o post 8793 (que se encontra dentro do startset) tem um link related para o post 7852 (fora do startset), logo tem 1 hit.

### Related Forward Snowballing

Lista de posts fora do startset que têm algum link do tipo related que aponta para um post no startset.

hist = quantidade de links related que um post X tem que apontam para o startset. Por exemplo, o post 7954 (fora do startset) tem 3 links related para posts no startset (são el2043, 11980 e 14345), logo o post 7945 tem 3 hits.
