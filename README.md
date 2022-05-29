Running the Django dev server:<br/>
```python manage.py runserver```

Running the functional tests:<br/>
```python functional_tests.py```

Running the unit tests:<br/>
```p3 selen_tests/main_test.py```<br/>

```docker exec -it selen_web_1 python manage.py test```

Migrations<br/>
```docker exec -it selen_web_1 python manage.py makemigrations```<br/>

``` docker exec -it selen_web_1  python manage.py migrate```