# Django_Skeleton_Project
원티드 프리온보딩 Django 스켈레톤 프로젝트

### 설정방법 
| 사전에 Postgresql을 Docker로 띄워주셔야 합니다 :)

1. app_name은 서비스 이름으로 변경
2. app_name로 적혀있는 것들 서비스 이름으로 변경
```
CI.yml
pyproject.toml
mypy.ini
settings.py -> DATABASE NAME
docker-compose.yml -> Postgres
```

### 실행 방법
1. poetry 설치 https://yeslab.tistory.com/136

2. dependencies 설치
```
poetry install
```

3. pre-commit (코드 포맷터) 설치
```
poetry run pre-commit install
```

4. 서버 실행
```
poetry run python manage.py runserver
```

### 프로젝트 구조
```
.
├── Dockerfile
├── LICENSE
├── README.md
├── app.log
├── app_name # 도메인 이름
│   ├── __init__.py
│   ├── app # 앱 이름
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── root_urls.py
│   ├── settings.py
│   └── wsgi.py
├── docker-compose.yml
├── manage.py
├── mypy.ini
├── poetry.lock
├── pyproject.toml
└── setup.cfg
```
