# Diet AG

Gerador de dietas baseado em algoritmo genéticos

## IDE Setup recomendado

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Flask Setup

Dentro da pasta do projeto, rodar os seguintes comandos:

```sh
# Prepara o ambiente
python3 -m venv env
source env/bin/activate

# Instalar o Flask
pip install Flask

# Instalar o Flask-Cors
pip install -U flask-cors

# Rodar o servidor
flask run
```

## Vue Setup

Para rodar o front-end:

```sh
# Acessar a pasta 'client'
cd client

# Instalar as dependências
npm install

# Compila e roda o projeto com hot-reload
npm run dev
```

## Testar a aplicação original

Ainda foi mantida a aplicação original em modo texto. Basta executar:

```sh
python3  app_original.py
```
