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
pip install -U flask-cors sqlalchemy pygame flask openpyxl flask_cors Flask-SQLAlchemy 

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

## Para gerar uma dieta e retornar um JSON

```sh
python3  main.py
```

Acessar a url do flask com o /get-diet.

## Para gerar uma dieta personalizada

 - Via insomnia utilize a josn abaixo:
 
 ```
 {
	"meta": {
		"porcoes": 5,
		"calorias": 700,
		"proteinas": 15,
		"lipidios": 14,
		"carboidratos": 75,
		"fibras=data": 8,
		"categorias": [
			"Frutas", "Pescados"
		]
	},
	"config": {
		"tamanho_populacao": 1000,
		"maximo_evolucoes": 100,
		"elite_proporcao": 0.1,
		"mutacao_proporcao": 0.05
	}
}
 ```
