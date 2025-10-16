# examen n°02

creacion de un api rest don django para gestionar // paciente y doctor

# instalar
mkdir healthtrack_api
cd healthtrack_api
# craer un entorno virtual
python -m venv venv
venv\Scripts\activate

# instalar dependecias
 pip install pip django
 pip requiremenst.txt

 # base de datos
 python manage.py migrate

# levantar servidor
python manage.py runserver

# crear carpetas 
django-admin starapp patientes
# configurar en healthtrack_api / settings.py 
"patients"
# crear un archivo en serializer.py
# modificar la vistas en 
# modificar el urls.py
