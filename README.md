# Tutorial de Django Framework

Este es el repositorio de la sección Django del [curso maestro de Python](https://www.hektorprofe.net/cupon/python) por Héctor Costa Guzmán.

## Instalación y uso

Se requiere `pipenv`, viene configurado en la versión de **Python 3.10**, se puede cambiar en el `Pipfile`.

Podéis clonar el repositorio e instalar el entorno virtual así:

```bash
git clone https://github.com/hektorprofe/tutorial-django-blog.git
cd tutorial-django-blog/
pipenv install
```

Para poner en marcha el proyecto:

```bash
cd tutorial/
pipenv run server
```

El usuario del administrador es `admin` con contraseña `1234`, podéis crear uno al gusto con:

```bash
cd tutorial/
pipenv run python manage.py createsuperuser
```

Cuando ya no necesitéis el proyecto podéis desinstalar el entorno:

```bash
cd tutorial-django-blog/
pipenv --rm
```
