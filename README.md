# Django CRUDCharts

## A simple Python/Django CRUD project with graphical visualization with Google Charts
- **Setting up and runing the project;**
- **Create;**
- **Read;**
- **Update;**
- **Delete;**
- **Charts**
- **Final considerations**
## Setting up 
The first step in any Python project, is to create the virtual environment to install the dependencies:
```
python -m venv venv
```
Then start the venv.
In Windows:
```
source venv/Scripts/activate
```
In Linux or Mac:
```
source venv/bin/activate
```

It should look like this:
<img src="https://uploaddeimagens.com.br/images/004/266/297/original/bash.PNG?1671469153">

Install the dependencies contained in the "requirements.txt" file.
In bash, type:

``` 
pip install -r requirements.txt
```

### Database
The project runs a PostgreSQL database, so you will need PostgreSQL on your computer. Or you can use the standard database SQLite, to do this skip the postgres configuration step.

[How to install PostgreSQL](https://www.youtube.com/watch?v=0n41UTkOBb0)

With PostgreSQL installed, create the project database, with the administrator logged in, in psql bash, type:
``` SQL
postgres= CREATE DATABASE crud;
```
After, enter your Postgres information in the project settings:
<img src="https://uploaddeimagens.com.br/images/004/266/274/original/db_settings.PNG?1671467553">

> Default port is 5432

## To switch to the default Django database (SQLite): 
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
```
Apply the migrations:

```
python manage.py migrate
```
And finally run the server:
```
python manage.py runserver
```
### Create:
Page for create "Users":
<img src="https://uploaddeimagens.com.br/images/004/266/331/original/djangocrud.PNG?1671471073">

### Read/View
Page for view "Users":
<img src="https://uploaddeimagens.com.br/images/004/266/334/full/ReadView.PNG?1671471210">

### Read:
<img src="https://uploaddeimagens.com.br/images/004/266/362/full/read.PNG?1671471643">

### Update: 
<img src="https://uploaddeimagens.com.br/images/004/266/345/full/Capturar.PNG?1671471410">
<img src="https://uploaddeimagens.com.br/images/004/266/355/full/edited.PNG?1671471518">

### Delete:
<img src="https://uploaddeimagens.com.br/images/004/266/370/full/delete.PNG?1671471771">

### Charts:
<img src="https://uploaddeimagens.com.br/images/004/266/395/full/Charts.PNG?1671472196">

# Final considerations
Thank you for getting this far, if you have any questions feel free to contact me through my social networks! 
I hope this content helps you in some way. good studies!
