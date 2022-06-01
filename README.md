https://learning.oreilly.com/library/view/test-driven-development-with/9781491958698/ch08.html#idm140633358806080

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