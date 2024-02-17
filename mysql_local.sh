# buildando a imagem mysql_db a partir do Dockerfile.MySQL:
docker build -t mysql_db:1.0.0 -f Dockerfile.MySQL .

# rodando o container:
docker run -de MYSQL_ROOT_PASSWORD=123456 --name mysql_db mysql_db:1.0.0

# adicionando o ip do container no arquivo .env
DB_HOST=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql_db)

# substituindo DB_HOST no arquivo .env
sed -i "s/DB_HOST=.*/DB_HOST=$DB_HOST/g" .env

# Setando pythonpath
export PYTHONPATH=./
