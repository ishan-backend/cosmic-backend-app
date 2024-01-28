### Installation steps:
Since this is my first time using Python3 and FastAPI for development, mentioning all related articles and steps for better documentation of learning.

### Python3, Pip and FastAPI installation
```bash
infra@IM-BAN-LAP-0243  ~/Desktop  python3 --version                                              ✔  10021  14:28:04
infra@IM-BAN-LAP-0243  ~/Desktop  pip3 --version                                               1 ↵  10019  14:27:55
infra@IM-BAN-LAP-0243  ~/Desktop  python3.11 -m pip install --upgrade pip                        ✔  10023  14:34:32
infra@IM-BAN-LAP-0243  ~/Desktop  pip3 install fastapi uvicorn                                   ✔  10022  14:28:21
infra@IM-BAN-LAP-0243  ~/Desktop  pip3 install motor
```
https://fastapi.tiangolo.com/
https://www.linkedin.com/pulse/creating-apis-fastapi-mongodb-using-motorasync-pymongo-suraj-singh/

### MongoDB docker container, MongoDB Compass GUI installation
```bash
docker pull mongo:latest
docker run -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=root -p 27017:27017 mongo

 infra@IM-BAN-LAP-0243  ~/Desktop  docker ps                                                      ✔  10030  14:55:24
CONTAINER ID   IMAGE     COMMAND                  CREATED             STATUS             PORTS                      NAMES
b32bfedbc535   mongo     "docker-entrypoint.s…"   About an hour ago   Up About an hour   0.0.0.0:27017->27017/tcp   focused_chatelet

# install mongodb compass for arm64 device and use connection string: mongodb://root:root@localhost:27017/admin
# admin is the database that holds your user
```


### Backend server specific library installations:
```bash
# create virtual environment inside project folder and activate it
 infra@IM-BAN-LAP-0243  ~/Desktop/cosmic-backend-app   main ✚ ● ?  python3 -m venv venv                                                                                      127 ↵  10034  15:17:30
 infra@IM-BAN-LAP-0243  ~/Desktop/cosmic-backend-app   main ✚ ● ?  source venv/bin/activate
# add venv in .gitignore
# to deactivate venv use: deactivate
 infra@IM-BAN-LAP-0243  ~/Desktop/cosmic-backend-app   main ✚ ● ?  pip3 --version                                                                                                ✔  10036  15:18:23
pip 23.3.1 from /Users/infra/Desktop/cosmic-backend-app/venv/lib/python3.11/site-packages/pip (python 3.11)
 infra@IM-BAN-LAP-0243  ~/Desktop/cosmic-backend-app   main ✚ ● ?  pip3 install fastapi uvicorn motor 
 infra@IM-BAN-LAP-0243  ~/Desktop/cosmic-backend-app   main ✚ ● ?  pip freeze > requirements.txt 
 infra@IM-BAN-LAP-0243  ~/Desktop/cosmic-backend-app   main ✚ ● ?  pip install -r requirements.txt
 # update python interpreter to local existing interpreter, and select venv, now start imports
```