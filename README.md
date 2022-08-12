# Tutorial de Django Framework

Este es el repositorio de la sección Django del [curso maestro de Python](https://www.hektorprofe.net/cupon/python) por Héctor Costa Guzmán.

## Instalación y uso

Podéis clonar el repositorio e instalar el entorno virtual así, se requiere `pipenv`:

```bash
git clone https://github.com/hektorprofe/tutorial-django-blog.git
cd tutorial-django-blog/
pipenv install -r requirements.txt
```

Para poner en marcha el proyecto:

```bash
pipenv run python manage.py runserver
```

El usuario del administrador es `admin` con contraseña `1234`, podéis crear uno al gusto con:

```bash
pipenv run python manage.py createsuperuser
```

Cuando ya no necesitéis el proyecto podéis desinstalar el entorno:

```bash
pipenv --rm
```
