# Stepik_Selenium_Final_task
Курс: "Автоматизация тестирования с помощью Selenium и Python"
Финальное задание - полноценный тестовый проект.

# Selenium with python
This is the final project to the course: https://stepik.org/course/575

The project implemented autotests based on a Page Object pattern for the [Training site](http://selenium1py.pythonanywhere.com/) 


### Requirements
```
selenium~=4.4.3
pytest~=7.1.2
pip~=20.1.1
pytest-rerunfailures
```
### Getting started
These instructions will get you a copy of the project up and running on your local machine for testing purposes.
```
git clone https://github.com/AlexanderZhilin/Stepik_Selenium_Final_task.git
cd Stepik_Selenium_Final_task
python -m venv PyTest_env
PyTest_env\Scripts\activate.bat (for Windows)     or    source PyTest_env/bin/activate (for Linux и MacOS)
pip install -r requirements.txt
```
## Running tests
To run basic tests for a review:
```
pytest -v -s --tb=line --reruns 3 --language=en --browser_name=chrome -m need_review test_product_page.py
```

### More tests

The project also presents autotests of two different pages for guests and authorized users:

```
pytest -v -s --tb=line --reruns 3 --language=en --browser_name=chrome test_main_page.py
pytest -v -s --tb=line --reruns 3 --language=en --browser_name=chrome test_product_page.py
pytest -v -s --tb=line --reruns 3 --language=en --browser_name=chrome -m need_review
pytest -v -s --tb=line --reruns 3 --language=en --browser_name=chrome -m login_guest
pytest -v -s --tb=line --reruns 3 --language=en --browser_name=chrome -m login_user
or you can use: --browser_name=firefox
```
