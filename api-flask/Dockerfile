# Usando imagem oficial do Python
FROM python:3.9-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o arquivo requirements.txt para instalar as dependências
COPY requirements.txt .

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da aplicação
COPY . .

# Expõe a porta 80
EXPOSE 80

# Rodando a aplicação Flask usando Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]