# Start Docker-Conatiner
```bash
docker-compose up
```
by runnind this comman you can started the docker container when your code write any file its reflected to the app folder and if your code need to read any file, you have to coy this files in app folder so its reflect to appfolder(in container)
if you neet any other dependencies tobe add just add this pip name in requirements file in app 
# updating code
for updating code just update code.py in py in app folder an the run this commands
*note:* for add image just add on app/image folder and run these command
```bash
docker-compose down
docker-compose up
```