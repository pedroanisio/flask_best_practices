#!/bin/bash

cd /home/pals/code/_temp/flask_best_practices;

app_UUID=`docker ps | grep flask_best_practices | awk '{print $1}'`;

if [ $app_UUID ]; then
  docker stop $app_UUID ;
  echo "stop success";
fi

echo y | docker system prune
docker build -t 'flask_best_practices' .
echo "build success"
docker run -d --network host --name flask_best_practices flask_best_practices
# docker run -d -p 5000:5000 --name flask_best_practices flask_best_practices
echo "run success"