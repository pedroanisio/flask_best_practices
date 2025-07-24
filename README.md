# Flask_BestPractices

## Forked from

> https://github.com/yangyuexiong/Flask_BestPractices

## Flask Best Practices

> This is a project structure that can be used directly to start developing business logic.
>
> It includes both a front-end/back-end separated RESTful API and a non-separated Jinja2 template rendering approach.
>
> Below, this structure is used in combination with Vue to implement an automated testing platform.
>
> Automated Testing Platform Web Frontend: https://github.com/ExileLine/ExileTestPlatformWeb
>
> Automated Testing Platform Backend: https://github.com/ExileLine/ExileTestPlatformServer
>
> Aiohttp Best Practices: https://github.com/yangyuexiong/AioHttp_BestPractices
>
> FastAPI Best Practices (Coming Soon...): https://github.com/yangyuexiong/FastApi_BestPractices
>
> **Flask Official Documentation**
>
> https://flask.palletsprojects.com/
>

```text
flask_best_practices
├── app (Application)
│   ├── __init__.py
│   ├── all_reference.py (Common Imports)
│   ├── api
│   │   ├── __init__.py (Register URLs)
│   │   ├── method_view_demo (Example of MethodView Usage)
│   │   │   ├── __init__.py
│   │   │   └── method_view_demo.py
│   │   ├── restful_demo (Example of flask_restful Usage)
│   │   │   ├── __init__.py
│   │   │   └── restful_demo.py
│   │   └── route_demo (Example of Flask Route Usage)
│   │       ├── __init__.py
│   │       └── route_demo.py
│   ├── controllers (Other Business Logic)
│   ├── models (Database Models)
│   ├── static (Static Files: JS, CSS, Images)
│   ├── templates (Templates for Jinja2 Rendering)
├── common (Common Files)
├── config (Configuration Files)
├── ExtendRegister (Unified Extension Registration)
├── logs (Logs Directory)
├── migrations (Database Migration Files)
├── tasks (Scheduled and Asynchronous Tasks)
├── test (Testing)
├── ApplicationExample.py (Application Example)
├── LICENSE
├── Pipfile (Environment Dependencies)
├── Pipfile.lock
├── README.md
├── run.py (Startup File)
└── test_run.py (Debug Startup File)
```

## 1. Installation

- Python 3.12+
- pip3
- pipenv
- ansible

  ```shell
  sudo apt install ansible
  pip3 install pipenv
  ```

## 2. Configure Virtual Environment

- Navigate to the project root directory

  ```shell
  cd /flask_best_practices
  ```

- Install virtual environment and dependencies

  ```shell
  pipenv install
  ```

- Activate virtual environment

  ```shell
  pipenv shell
  ```

- Check virtual environment path

  ```shell
  pipenv --venv
  ```


## 3. Generate and check Configuration Files

- Pre-setup (check and modify var files)
  
**Ansible role `Application` vars**

```shell
/flask_best_practices/meta/playbooks/roles/application/vars/main.yaml
```

```shell
ansible-playbook meta/playbooks/configure_project.yaml
```


- Pre-setup (e.g., creating databases)

    - [/config/dev.ini](./config/dev.ini)
    - [/config/pro.ini](./config/pro.ini)

## 4. ORM

- Includes a simple backend permission management system for database migration testing.

- [command_register.py](./ExtendRegister/command_register.py) contains registered Flask CLI commands for initializing data, creating tables, etc.

- Enter project environment:
  ```shell
  pipenv shell
  ```

- List all Flask CLI scripts and commands:
  ```shell
  flask
  ```

- Run database migrations

  ```shell
  flask orm
  ```

## 5. Route Registration

- Example routes, APIs, and views:

    - [restful_demo.py](./app/api/restful_demo/restful_demo.py)
    - [method_view_demo.py](./app/api/method_view_demo/method_view_demo.py)
    - [route_demo.py](./app/api/route_demo/route_demo.py)

## 6. Hooks (Interceptors)

- Example:

    - [/flask_best_practices/common/interceptors/ApiHook.py](./common/interceptors/ApiHook.py)

## 7. Custom Exceptions

- Define in [customException.py](./common/libs/customException.py)

## 8. API Endpoints

- API: `http://0.0.0.0:9999/api/`
- CMS: `http://0.0.0.0:9999/cms/`
- Other Modules:
    - `http://0.0.0.0:9999/m1/`
    - `http://0.0.0.0:9999/m2/`
    - `http://0.0.0.0:9999/m3/`

## 9. Tasks

- Asynchronous Tasks (Celery 5.2)

- Scheduled Tasks

## 10. Deployment

- Method 1: Local Deployment
- Method 2: Docker Deployment
- Method 3: Execute `server_start.sh` (Recommended)

## Notes

- There may be numerous `print()` debug statements in the code. Feel free to comment them out or remove them.
- Now, quickly implement your business logic! 😆

