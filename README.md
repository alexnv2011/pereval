# pereval
The program implements the saving of passes, their coordinates, authors and pictures.
Used by Django REST API
All objects are stored in the database using the Django model.
The PostgreSQL database is used, but any other DBMS is possible. The database connection parameters are specified in the environment variables file.

Main uri addresses:
/perevals/ - passes

Example POST request to add passes and authors. Authorization is not required. New passes will be in the new status.
The email field is unique to users, so if a user exists, they will be bound as the author of the pass, otherwise a new user will be created.

http://158.160.36.161:8000/perevals/
Format: form-data; Authorization: none
'coords.latitude': 45,
'coords.longitude': 55,
'coords.height': 75,
'title': 'asdadasdsaad',
'winter': '1',
'spring': '4',
'email': 'nveiwioj555@kasd.ri',
'first_name': 'Ivan'


example response (201 Created)
{"id":21,"coords":{"id":21,"latitude":99.0,"longitude":77.0,"height":88},"images":[],"date_added":"2023-04-02T17:12:02.262117Z","beauty_title":null,"title":"asdadasdsaad","other_titles":null,"connect":null,"winter":"1","summer":null,"autumn":null,"spring":"4","status":"new","author":8}


/images/ - pictures for passes
http://158.160.36.161:8000/images/

An example of a POST request for adding pictures of a pass. The number of pictures is not limited. Saved on the server to the folder specified in settings.py.

"title":"Заголовок картинки перевала"
"pereval":2
"image": file

example response (201 Created)
{"id":2,"title":"Заголовок картинки перевала","image":"http://158.160.36.161:8000/media/2023/04/02/06.jpg","pereval":2}

