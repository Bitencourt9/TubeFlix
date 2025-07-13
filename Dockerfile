# Use uma imagem base Python otimizada para ser leve
FROM python:3.11-slim-bullseye

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Define variáveis de ambiente para desativar o buffer de saída do Python
# e garantir que a saída seja direcionada para o terminal (logs)
ENV PYTHONUNBUFFERED 1

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências Python listadas no requirements.txt
# O --no-cache-dir evita que o pip crie caches desnecessários no contêiner,
# economizando espaço
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da sua aplicação para o contêiner
# O . (ponto) significa "o diretório atual" tanto na origem quanto no destino
COPY . .

# Expõe a porta que o Django usará (padrão 8000) para que o Docker saiba
EXPOSE 8000

# Comando padrão que será executado quando o contêiner iniciar.
# Usaremos Gunicorn aqui, que é mais robusto para produção que o runserver.
# 0.0.0.0 permite que o servidor seja acessível de fora do contêiner.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tubeflix.wsgi:application"]