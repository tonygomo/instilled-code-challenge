# Instilled Code Challenge


## To Run Locally

```
python main.py 0-1000 2000-3000 2500-4000
```

Notes:
* Requires Python 3 (https://www.python.org/downloads/).
* Some systems may name the Python executable `python3`.
* App has been tested against Python 3.7.4.


## To Run With Docker

```
docker-compose run --rm app sh -c "python main.py 0-1000 2000-3000 2500-4000"
```


## To Run Tests

```
python test.py
```

```
docker-compose run --rm app sh -c "python test.py"
```