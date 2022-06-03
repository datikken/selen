https://learning.oreilly.com/library/view/test-driven-development-with/9781491958698/ch13.html#idm140633354934496

https://github.com/hjwp/book-example/tree/chapter_13/lists

[//]: # ()
[//]: # (Running the Django dev server:<br/>)

[//]: # (```python manage.py runserver```)

[//]: # (Running the unit tests:<br/>)

[//]: # (```p3 selen_tests/tests.py```<br/>)

[//]: # ()
[//]: # (```docker exec -it selen_web_1 python manage.py test```)
Tests:</br>
```python manage.py test```

```python manage.py test tests--functional.test_list_item_validation```

Migrations<br/>
```docker exec -it selen_web_1 python manage.py makemigrations```<br/>

``` docker exec -it selen_web_1  python manage.py migrate```

To create project:<br/>
```django-admin startproject [name]```

To create app:<br/>
``` python manage.py startapp [name]```