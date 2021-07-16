# Python API README

Back en Python pour le traitement de l'image et la récupération du texte.

## SETTINGS

How to launch the app

Commands :

Open a terminal and run
```
docker-compose up
```

Open another terminal and run to get the bash on the container
```
docker exec -it python-api_app_1 bash
```

Once you are well connected you can use the usual commands.
To run the app ...
```
python app.py
```

After that you can run in a new terminal the curl command or use Postman to test.
```
curl http://localhost:8080/
```