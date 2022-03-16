# Shrtnr

Simple flask app which works with docker-compose to test scalling with swarm
```bash
docker-compose up
docker-compose down

docker-compose build

docker stack deploy -c docker-compose.yml shortenerApp

docker service ls

docker service scale shortenerApp_shrtnr_app=4

curl 127.0.0.1/getURL/CEXIA

```
