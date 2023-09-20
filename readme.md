# Django 시작하기

## ※ PyCharm IDE 환경에서 개발
 
- 기간: 23.08.31 ~ 23.09.19
- Python 설치 필수: 3 버전 이상
- 개발 지침서: https://docs.djangoproject.com/ko/4.2/intro/tutorial01/

### 1. 프로젝트 생성
#### 1.1 IDE에서 생성 
1. New Project
2. Django 선택
3. Python Interpreter: New Virtualenv Environment 설정
   - 설정 정보
     - New environment using: Virtualenv ← 기본 선택
     - Location: 자동 생성
     - Base interpreter: 설치한 Python 경로 선택

#### 1.2 명령어로 생성
```
\> django-admin startproject mysite
```
- Python 경로가 맞지 않으면 django-admin가 실행되지 않을 수 있음.
- 해결 못해서 IDE애서 프로젝트 생성함.

#### 파일 구조
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
- manage.py
  - 커맨드라인 유틸리티, Django를 실행하는 관리자 기능을 담당하며 진입점.
- mysite/
  - 프로젝트를 위한 실제 Python 패키지 저장. 디렉토리 내의 이름을 이용하여 프로젝트 내에서 패키지 import 해줌.
- mysite/__init__.py
  - Python에게 이 디렉토리가 패키지임을 알려주는 용도. 빈 파일.
- mysite/settings.py
  - 프로젝트의 환경 및 구성 저장, Django 설정을 모듈 변수로 표현한 Python 모듈.
  - INSTALLED_APPS 변수
    - 현재 Django 인스턴스에서 활성화된 모든 Django 애플리케이션 이름이 자동으로 입력됨.
    - 이 앱들은 다수의 프로젝트에서 사용하거나 다를 프로젝트에서 쉽게 사용할 수 있도록 패키징하여 배포 가능.
      - django.contrib.admin: 관리용 사이트
      - django.contrib.auth: 인증 시스템
      - django.contrib.contenttypes: 콘텐츠 타입을 위한 프레임워크
      - django.contrib.sessions: 세션 프레임워크
      - django.contrib.messages: 메세징 프레임워크
      - django.contrib.staticfiles: 정적 파일을 관리하는 프레임워크
- mysite/urls.py
  - URL 선언 정의하여 View 연결. 사이트의 목차. URL Dispatcher(파견자)
- mysite/wsgi.py
```python
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
```
  - 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점. 프로젝트와 웹서버를 연결.
  - 로컬에서 테스트할 때 쓰이는 개발 서버(runserver)와 프로덕션 WSGI 배포에서 모두 이용.
  - WSGI 서버는 settigns.py에 있는 WSGI_APPLICATION을 통해 호출 가능한 애플리케이션 경로를 얻음.
    - {프로젝트명}.wsgi.application
  - WSGI 서버가 애플리케이션을 로드할 때 Django는 전체 애플리케이션이 정의된 설정 모듈을 DJANGO_SETTINGS_MODULE 키를 이용해 가져옴.
  - 실제 운영에서는 'mysite/profiles' 폴더 생성하여 dev.py(개발용)/production.py(운영용)/staging.py(테스트용) 등에 따라 여러 설정 관리 가능.
- mysite/asgi.py: 프로젝트를 서비스하기 위한 ASGI 호환 웹 서버의 진입점.

### 2. 개발 서버
- http://127.0.0.1:8000/ 
#### 1.1 IDE에서 실행 
1. New Project
2. Django 선택
3. Python Interpreter: New Virtualenv Environment 설정
   - 설정 정보
     - New environment using: Virtualenv ← 기본 선택
     - Location: 자동 생성
     - Base interpreter: 설치한 Python 경로 선택

#### 1.2 명령어로 실행
- mysite 디렉토리로 이동한 후 아래 명령어 입력
```
\> py manage.py runserver
```
- 명령어 직접 입력하지 않고 IDE 환경에서 설정해주면 간편하게 서버 실행 가능.
- IDE 실행 > /manage.py 오른쪽 클릭 > More Run/Debug > Modify Run Configuration
  - Script Parameter : 'runserver' 입력

#### IP 포트 변경
- 기본적으로 8000번 포트로 개발 서버 실행됨
- 변경하려면 아래 명령어 입력
```
\> py manage.py runserver 0.0.0.0:8080
```
### 3. 앱 생성
- 지금까지 작업을 시작하기 위해 환경(프로젝트)을 설치 했고 실제 기능 구현을 위한 앱을 생성해줘야 함.
- Django는 애플리케이션을 Python 패키지로 구성. 기본 디렉토리 구조(Scaffolding)를 자동 생성 해줌
```
\> py manage.py startapp polls
```
- 생성되는 파일
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
### 4. DB 설치, 복수 DB 사용
- DB 설치를 위한 설정값 입력
   - mysite/setting.py > DATABASES 키에 입력
   - Django는 Python에서 기본적으로 제공하는 SQLite를 기본 값으로 사용하도록 구성해 놓음.
   - SQLite DB는 컴퓨터 파일이여서 NAME 키만 설정하면 됨.
   - 그 외 DB는 추가 설정이 필요함.
    ```python
    # Database
    # https://docs.djangoproject.com/en/4.2/ref/settings/#databases 
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        },
        'second': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': 3306,
            'USER': 'root',
            'PASSWORD': '12qw#$ER',
            'NAME': 'mysite',
        }
    }
    ```    
  - mysql 사용시 mysqlclient 설치 선행
    ```commandline
    > pip install mysqlclient
    ```
  - mysite/dbrouter.py 생성
      - DB용 라우터 생성(클래스)
    ```python
    class MultiDBRouter(object):
    def __init__(self):
        self.route_app_labels = ['default', 'second']
    
    """
    user_data 앱의 모델을 조회하는 경우 users_db로 중계한다.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return model._meta.app_label
    
        return None
    
    """
    user_data 앱의 모델을 기록하는 경우 users_db로 중계한다.
    """
    def db_for_writer(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None;
    
    """
    user_data 앱의 모델과 관련된 관계 접근을 허용한다.
    """
    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None;
    
    
    """
    user_data 앱의 모델에 대응하는 표가 users_db 데이터베이스에만 생성되도록 한다.
    """
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return self.db_name
        return None;
    ```
- DB 복수 설치를 위해 키 입력
   - mysite/setting.py > DATABASE_ROUTERS 키에 입력
    ```python
    DATABASE_ROUTERS = [
        'common.db_Router.UserRouter',
    ]
    ```
- DB migrations 을 위한 명령어 실행
    ```commandline
    > py manage.py migrate
    > py manage.py migrate --database=second ## second 디비와 마이그레이션
    ```
  - migrate 명령
    - settings.py의 INSTALLED_APPS의 설정을 탐색하여 settings.py의 DB 설정과 app과 함께 제공되는 DB migrations에 따라 필요한 DB 테이블을 생성.
    - → migration들을 실행시켜주고 자동으로 데이터베이스 스키마를 관리해줌.
    - 명령어 실행 시 각 migration이 적용한 메시지가 화면에 출력됨.
  
  
### 5. 표준시간대 설정
- mysite/setting.py > #Inernationalization 부분 수정
```python
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False
```
#### ※ 표준 시간대
  - Default time zone: TIME_ZONE 변수로 지정한 시간대
  - Current time zone
    - 템플릿 랜더링에 사용되는 시간대 (특별히 설정하지 않으면 Default time zone과 동일)
    - activate() 함수를 사용하여 사용자의 실제 표준 시간대를 설정.
  - Django는 TIME_ZONE 설정 값으로 환경변수를 설정해주어서 Default time zone
- 표준 시간대 참조: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
- datetime 객체
  - datetime.datetime 객체는 표준 시간대 정보를 담고 있는 tzinfo 속성(datetime.tzinfo)을 지님.
  - 종류
    - Naive 객체: tzinfo 속성을 설정하지 않은 datetime 객체 (TIME_ZONE 변수로 지정한 시간대 사용)
    - Aware 객체: tzinfo 속성을 설정한 datetime 객체 (명확하게 기준이 되는 시간대를 tzinfo 속성으로 지정)
- USE_TZ 변수
  - = False : 내부적으로 Naive datetime 객체 사용 
  - = True
    - 내부적으로 Awawre datetime 객체 사용
    - 폼에 입력된 날짜 값은 Current time zone으로 해석 → Aware datetime 객체로 변환함.
    - 템플릿 랜더링할 때는 Aware datetime 객체를 Current time zone으로 변환함.
- 관련 라이브러리
  - pytz : Olson tz database 를 Python으로 가져오는 라이브러리. 정확한 교차 플랫폼 Timezone 계산 가능.  
    ```python
    from datetime import datetime, date, timedelta
    from django.utils import timezone
    import pytz # Olson tz database 
    
    datetime.now()  # Naive (TIME_ZONE)
    
    datetime.now(pytz.UTC)  # Aware (UTC)
    
    timezone.now()  # Aware (UTC)
    
    timezone.localtime(datetime.now(pytz.UTC))  # Aware (UTC) → Aware (TIME_ZONE)
    
    timezone.localtime(timezone.now())  # Aware (UTC) → Aware (TIME_ZONE)
    
    timezone.make_aware(datetime.now())  # Naive (TIME_ZONE) → Aware (TIME_ZONE)
    ```

### 6. 모델 만들기
- 모델
  - 부가적인 메타데이터를 가진 DB의 구조(layout).
  - 데이터에 대한 오직 하나의 확실한 정보 출처 의미. 저장 중인 데이터의 필드 및 동작도 포함.
  - 목표: 데이터 모델을 한 곳에서 정의, 데이터 모델을 자동으로 파생. ← DRY Principle

1. file:polls/models.py에 모델 클래스 생성
  - :class:`django.db.models.Model`의 하위 클래스로 표현
  - polls/models.py 파일 생성하고 아래 코드 작성
    ```python
    from django.db import models
  
    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField("date published")
    
    
    class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)
    ```
  - 모델마다 여러 클래스 변수 존재하고 각 클래스 변수는 모델에서 DB 필드를 표현.
  - DB의 각 필드는 Field 클래스의 인스턴스로 표현.
    - CharField: 문자(character) 필드, max_length 필수 입력 인수
    - DateTimeField: 날짜 시간(datetime) 필드
    - Field 인스턴스의 이름은 기계가 읽기 좋은 형식(machine-friendly format)임
    - Field 클래스의 생성자의 첫번째 인수를 사용하여 사람이 일기 좋은 이름(human-readable)을 생성해줌.
    - Field는 다양한 선택적 인수를 가짐. default 인수는 기본값을 지정해줌.
  - 외래키 작성
    - models.ForeignKey({참조 테이블 모델}, on_delete={개체 삭제시 수행할 동작 값 지정})
    - on_delete 값
      - models.CASCADE: 외래키를 포함하는 행도 함께 삭제
      - models.PROTECT: 해당 요소가 함께 삭제되지 않도록 오류 발생 (ProtectedError)
      - models.SET_NULL: 외래키 값을 NULL 값으로 변경 (null=True일 때 사용 가능)
      - models.SET(func): 외래키 값을 func 행동 수행 (func는 함수나 메서드 등을 의미)
      - models.DO_NOTHING: 아무 행동을 하지 않음

2. 모델 활성화
   1. 위 모델이 활성화 되기 위해서 현재 프로젝트에 polls 앱이 설치되어 있음을 알려야 함
      - mysite/setting.py polls 앱 추가
       ```python
       INSTALLED_APPS = [
           "polls.apps.PollsConfig",
           "django.contrib.admin",
           "django.contrib.auth",
           "django.contrib.contenttypes",
           "django.contrib.sessions",
           "django.contrib.messages",
           "django.contrib.staticfiles",
       ]
       ```
      - polls 앱의 모델이 새로 생성되었다는 변경 사항을 migration으로 저장시키기 위해 Django에게 알림.
       ```commandline
       > py manage.py makemigrations polls
       ...
       Migrations for 'polls':
         polls/migrations/0001_initial.py
           - Create model Question
           - Create model Choice
       ...
       ```
      - migration을 통해 실행한 SQL 문장 확인
       ```commandline
       > py manage.py sqlmigrate polls 0001
       ```        
    - Django는 위 모델을 가지고 DB 스키마 생성(CREATE TABLE문), Question과 Choice 객체에 접근하기 위한 Python DB 접근 API 생성

## 7. DB 제어(추가, 검색, 삭제)
- Shell 에서 DB 제어
1. Shell 열기
   - manage.py에 설정된 DJANGO_SETTINGS_MODULE 환경변수에 입력된 mysite/settings.py의 Python 가져오기 경로를 Django에게 제공.
```commandline
> py manage.py shell
```
2. 데이터 저장
```commandline
>>> from polls.models import Choice, Question

# default DB(sqlite)에 저장된 Question 테이블의 모델 객체 출력
>>> Question.objects.all()
<QuerySet []>

# second DB(mariadb)에 저장된 Question 테이블의 모델 객체 출력
>>> Question.objects.using("second")
<QuerySet []>

# Question 객체 생성
>>> from django.utils import timezone
>>> q = Question(question_txt="what's new?", pub_date=timezone.now())

# 객체 DB에 저장
>>> q.save()

# Question 객체의 question_txt 속성 값 호출
>>> q.question_txt
"what's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)

# Question 객체의 question_txt 속성 값 수정
>>> q.question_text = "What's up?"
>>> q.save()

# 종료
>>> exit()
```
3. 모델 객체 출력 시 실제 데이터 출력되도록 수정
- polls/models.py
```python
import datetime
from django.db import models
# 시간대 관련 유틸리티
from django.utils import timezone

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_txt

    # Custom Method 추가 - 24시간 이전에 등록한 데이터인지 여부 확인
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_txt
```
4. 모델 객체 데이터 검색
- API에서 이중 밑줄(__) 을 이용해서 검색
- 참조: https://docs.djangoproject.com/ko/4.2/topics/db/queries/#field-lookups-intro
```commandline
>>> from polls.models import Choice, Question

# Question 객체의 데이터 중 id(PK, 자동 생성) 값이 1인 데이터 가져오기
>>> Question.objects.get(id=1)
<Question: What's up?>
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Question 객체의 데이터 중 question_text 속성의 앞 글자가 "What"으로 시작하는 데이터 가져오기
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

# 날짜 검색
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.filter(pub_date__year=current_year)
<QuerySet [<Question: what's new?>, <Question: what's new?>]>

# Question 객체의 함수 호출
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True
```

5. 참조 테이블에 데이터 저장
```commandline
# Question 객체 중 PK=1 인 데이터 가져오기
>>> q = Question.objects.get(pk=1)
# Question 객체를 참조한 Choice 객체 불러오기
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not Much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: Not much>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice 객체에 참조된 Question 객체 불러오기 - Choice 객체는 Question 객체에 대한 API 권한 있음
>>> c.question
<Question: what's new?>

>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()

>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Choice 객체 데이터 중 choice_text 속성의 앞 내용이 "Just hacking"인 데이터 삭제
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```

6. 관리 사이트 생성
    1. 관리자 계정 생성
        ```commandline
        > py manage.py createsuperuser
        사용자 이름:
        이메일 주소: 
        Password:
        Password (again):
        Superuser created successfully.
        ```
        - 관리자 비밀번호 변경
        ```commandline
        > py manage.py changepassword {사용자 이름}
        Changing password for user '{사용자 이름}'
        Password:
        Password (again):
        Password changed successfully for user '{사용자 이름}'
        ```
    2. 관리자 페이지 접속
       - http://127.0.0.1:8000/admin/
       - 언어 변경: mysite/settings.py > LANGUAGE_CODE 수정
       - django.contrib.auth 모듈에서 제공 
    3. 관리 사이트에서 poll app 변경 가능하도록 설정
       - 관리자에게 Question 대상에는 관리 인터페이스가 있음을 알려줌.
       - mystie/admin.py 작성
       ```python
       from django.contrib import admin
       from .models import Question
       
       admin.site.register(Quesiton)               
       ```
       - 관리 사이트에서 poll.Question 객체 DML 가능. 자동으로 과거 내력 저장 및 확인 가능 

## 8. URL 설계
- web-poll 애플리케이션 공용 인터페이스 'views' 작성하기
- view: 특정한 기능을 제공하고 특정한 템플릿을 가진 Django 애플리케이션에 있는 웹 페이지의 'type'.
- Django는 웹페이지와 기타 콘텐츠가 view로 전달<br>→ 각 view는 Python 함수(또는 클래스 기반 view의 경우 메소드)로 표현<br>→ Django는 요청한 URL(도메인 이름 뒤의 URL 부분)을 왁인하여 보기를 선택.
- URL로부터 뷰를 얻기 위해 Django는 'URLconfs' 사용하여 URL 패턴을 뷰에 연결함.
1. 뷰 추가
   - polls/views.py
     ```python
     def detail(request, question_id):
         return HttpResponse("You're looking at question %s." % question_id)

     def results(request, question_id):
         response = "You're looking at the results of question %s."
         return HttpResponse(response % question_id)

     def vote(request, question_id):
         return HttpResponse("You're voting on question %s." % question_id)
     ```
2. 새로운 뷰를 polls.urls 모듈 연결
    ```python
    from django.urls import path
    from . import views
    
    urlpatterns = [
       path("", views.index, name="index"),
       path("<int:question_id>", views.detail, name="detail"),
       path("<int:question_id>/results", views.results, name="results"),
       path("<int:question_id>/vote/", views.vote, name="vote"),
    ]
    ```
   - 처리 순서
     - "/polls/34" 요청<br>
       → Django는 ROOT_URLCONF 설정이 가리키는 mystie.urls Python 모듈 로드<br>
       → urlpatterns 변수를 찾아서 패턴을 순서대로 순회함<br>
       → polls/ 에서 일치하는 패턴을 찾은 후 일치하는 텍스트("polls/")를 제거하고 나머지 텍스트(–"34/"–)를 추가 처리를 위해 'polls.urls' URLconf로 보냄.<br>
       → 일치하는 패턴을 찾아 detail() 뷰를 호출
   - "<int:question_id>"
     - urlpatterns에서 꺽쇠 괄호를 사용하면 URL의 일부가 캡처되어 키워드 인수로 view 함수에 전송함.
     - question_id: 일치하는 패턴을 식별하는 데 사용할 이름을 정의
     - int: URL 경로의 이 부분과 일치하는 패턴을 결정하는 변환기
     - 콜론(:): 변환기와 패턴이름을 구분
3. index URL 접속시 Question 객체 출력하기
  - polls/view.py 추가
    ```python
    from django.http import HttpResponse
    from .models import Question
    
    # 새로운 index() 뷰 하나를 호출했을 때, 시스템에 저장된 최소한 5 개의 투표 질문이 콤마로 분리되어, 발행일에 따라 출력                
    def index(request):   
        latest_question_list = Questino.objects.order_by("-pub_date")[:5]
        output = ", ".join([q.question_text for q in latest_question_list])
        return HttpRespone(output)
    ```
4. html 페이지에 Question 객체 출력
  - polls/templates/polls/index.html 생성
     - polls/templates/polls/index.html 생성
     - 프로젝트의 TEMPLATES 설정은 Django가 어떻게 템플릿을 불러오고 렌더링 할 것인지 기술
     - APP_DIRS 옵션이 True로 설정된 DjangoTemplates 백엔드를 구성
     - DjangoTemplates은 각 INSTALLED_APPS 디렉토리의 “templates” 하위 디렉토리를 탐색
       ```html
        {% if latest_question_list %}
            <ul>
            {% for q in latest_question_list %}
                <li><a href="/polls/{{ q.id }}">{{ q.question_text }}</li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No polls are available.</p>
        {% endif %}
        ```
  - index 뷰에 template 적용
    - 템플릿에 context를 채워넣어 표현한 결과를 HttpResponse 객체와 함께 돌려줌.
    ```python
    import django.http import HttpResponse
    import django.template import loader
    import .modesl import Question
    
    def index(request):
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        template = loader.get_template("polls/index.html")
        context = { 'latest_question_list': latest_question_list }
        return HttpResponse(template.render(context, template))
    ```
    - 단축 기능(shortcuts)으로 코딩
    ```python
    import django.shortcuts import render
    from .models import Question
    
    def index(request):
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        context = {'latest_question_list':latest_question_list}
        return render(request, "polls/index.html", context)
    ```
    - 404 에러 발생
      ```python
      from django.http import Http404
      from django.shortcuts import render, get_object_or_404
      from .models import Question
    
      def detail(request, question_id):
          try:
              question = Question.objects.get(pk=question_id)
          except Question.DoesNotExist:
              raise Http404("Question does not exist")
          return redner(request, "polls/detail.html", {"question": question})
      ```
    - 단축 기능(shortcuts)으로 코딩
    ```python
    from django.shortcuts import render, get_object_or_404
    from .models import Question
    
    def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return redner(request, "polls/detail.html", {"question": question})
    ```
    - detail.html 추가
    ```html
    <h1>{{ question.question_text }}</h1>
    <ul>
    {% for choice in question.choice_set.all %}
        <li>{{ choice.choice_text }}</li>
    {% endfor %}
    </ul>
    ```
  - 하드코딩 제거
    ```html
    /* 하드 코딩 */
    <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    
    /* 소프트 코딩 */
    <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
    ```
    - polls.urls 모듈의 path() 함수에서 인수의 이름을 정의하였으므로 {% url %} template 태그를 사용하여 url 설정에 정의된 특정한 URL 경로들의 의존성 제거 가능.
- URL namespace 설정 
  - 프로젝트 안에 앱이 다수일 경우 앱의 URL을 구별해줌.
  - polls/urls.py
    ```python
    from django.urls import path
    from . import views
        
    app_name = "polls"
    urlpatterns = [
        path("", view.index, name="index"),
        path("/<int:question_id>", view.detail, name="detail"),
        path("<int:question_id>/results/", views.results, name="results"),
        path("<int:question_id>/vote/", views.vote, name="vote"),
    ]
    ```
  - polls/index.html
    ```html
    <li><a href="{% url "polls.detail" question.id %}">{{ question.question_text }}</a></li>
    ```

## 9. 폼 작성
1. polls/detail.html 수정
   ```html
   <form action="{% url 'polls:vote' question.id %}" method="post">
   {% csrf_token %}
   <fieldset>
       <legend><h1>{{ question.question_text }}</h1></legend>
       {% if error_message %}
       <p><strong>{{ error_message }}</strong></p>
       {% endif %}
    
       {% for choice in question.choice_set.all %}
       <input type="radio" name="choice" id="choice{{ forloop.counter }}">
       <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
       {% endfor %}
   </fieldset>
   <input type="submit" value="Vote">
   <input type="submit" value="Vote">
   </form>
   ```
   - csrf_token: 하단 '정리' 참조
   - forloop.counter: for 태그 반복한 횟수(숫자)
2. polls/views.py
    ```python
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    from django.shortcuts import render, get_object_or_404
    from .models import Choice, Question
    
    def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = questio.choice_set.get(pk=requeste.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            return render(request, "polls/detail.html", {"question": question, "error_message": "You didn't select a choice."})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse("polls:results", args=(question.id)))
    ```
    - request.POST
      - 키로 전송된 자료에 접근할 수 있도록 해주는 객체
      - request.POST['choice']는 선택된 설문의 ID를 문자열로 반환해줌.
      - request.GET 존재.
      - 만약 POST에 choice가 없을 경우 KeyError 발생
      - HttpResponseRedirect
        - POST 데이터 처리 후에는 항상 HttpResponseRedirect를 반환해야 함.
      - reverse({viewname}, {args})
        - 뷰 함수에서 URL 소프트 코딩 해줌.
        - 제어를 전달하기 원하는 뷰의 이름(viewname)을 URL 패턴의 변수 부분을 조합해서 해당 뷰를 가리킴.
3. results 페이지 만들기
- polls/results.html
    ```html
    <h1>{{ question.question_text }}</h1>
    <ul>
    {% for c in question.choice_set.all %}
        <li>{{ c.choice_text }} -- {{ c.votes }} vote {{ c.votes|pluralize }}</li>
    {% endfor %}
    </ul>
    <a href="{% url 'polls:detail' question.id %}">Vote again?</a>
    ```
    - {value}|pluralize: 복수 접미사 필터. value 변수값이 1이 아니면 복수 접미사 s 붙임

4. 제너릭 뷰 사용
   - views 수정: polls/views.py
       ```python
       from django.http import HttpResponseRedirect
       from django.shortcuts import get_object_or_404, render
       from django.urls import reverse
       from django.views import generic
    
       from .models import Chocie, Question
    
       class IndexView(generic.ListView):
           template_name = 'polls/index.html'
           context_object_name = 'latest_question_list'
    
           def get_queryset(self):
               return Question.objects.order_by('-pub_date')[:5]
    
       class DetailView(generic.DetailView):
           model = Question
           template_name = 'polls/detail.html'
    
       class ResultsView(generic.DetailView):
           model = Question
           template_name = 'polls/results.html'
       # 이하 동일 #
       ```
   - URLConf 수정: polls/urls.py
      ```python
      from django.urls from path
      from . import views
    
      app_name = 'polls'
      urlpatterns = [
          path('', views.IndexView.as_view(), name='index'),
          path('<int:pk>/', views.DetailView.as_view(), name='detail'),
          path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
          path('<int:question_id>/votes/', views.vote, name='vote')
      ]
      ```
   - generic view
     - 각 제너릭 뷰는 model 속성을 사용하여 표현할 모델 지정. 모델명을 활용하여 컨텍스트 변수명이 자동 명명됨.
     - .ListView
       - '개체 목록 표시' 개념을 추상화.
       - 기본 컨텍스트 변수명: <model_name>_list(소문자)
       - 기본 템플릿 이름: <app_name>/<model_name>_list.html
     - .DetailView
       - '특정 개체 유형에 대한 세부 정보 페이지 표시' 개념을 추상화.
       - 기본 컨텍스트 변수명: <model_name>(소문자)
       - 기본 템플릿 이름: <app_name>/<model_name>_detail.html
       - URL에서 캡처된 기본 키 값이 pk라고 기대하여 question_id 이름을 pk로 변경함.
     - template_name: 기본 템플릿 이름 대신 특정 이름 사용.
     - context_object_name: 기본 컨텍스트 변수명 대신 특정 이름 사용. 

## 10. 테스트 자동화
1. 테스트 케이스 작성
   - polls/tests.py
     - 미래의 pub_date를 가진 Question 인스턴스 생성하는 메소드를 가진 django.test.TestCase 하위 클래스 생성
       ```python
       from django.test import testcases
       import datetime
       from django.utils import timezone
    
       from .models import Question
    
       class QuestionModelTests(TestCase):
         def test_was_published_recently_with_future_question(self):
             time = timezone.now() + datetime.timedelta(days=30)
             future_question = Question(pub_date=time)
             self.assertIn(future_question.was_published_recently(), False)
       ```

2. 테스트 케이스 실행
    ```commandline
    > py manage.py test polls
    Found 1 test(s).
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    F
    ======================================================================
    FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/path/to/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_question
        self.assertIs(future_question.was_published_recently(), False)
    AssertionError: True is not False
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
    
    FAILED (failures=1)
    Destroying test database for alias 'default'...
    ```
   1. polls 앱에서 테스트 찾아서 실행.
   2. django.test.TestCase 클래스의 서브 클래스 탐색.
   3. Creating test database for alias 'default' → 테스트 목적으로 특별한 DB 생성.
   4. 테스트 메소드 이름이 test로 시작하는 메소드 탐색.
   5. test_was_published_recently_with_future_question 에서 pub_date 필드가 현재 시간의 30일 지난 Question 인스턴스 생성.
   6. ...assertIn() 메소드 사용하여 False가 반환되야 함을 알림.
   7. 하지만 테스트 결과는 True이므로 버그.

3. 버그 수정
   - polls/models.py
       ```python
       def was_published_recently(self):
           now = timezone.now()
           return now >= self.pub_date >= now - datetime.timedelta(days=1)
       ```
     - pub_date 날짜가 과거인 경우에만 true가 되도록 수정

4. 테스트 케이스 보강
   - Question 모델의 was_recently_published() 메소드의 포괄적인 테스트를 위해<br>
    pub_date가 미래, 과거, 최근인 Question 인스턴스를 사용한 테스트 메소드 추가 
       ```python
       def was_recently_published_with_old_question(self):
           time = timezone.now() - datetime.timedelta(days=1, seconds=1)
           old_question = Question(pub_date=time)
           self.asserIs(old_question.was_recently_published(), False)
    
       def was_recently_published_with_recent_question(self):
           time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
           recent_question = Question(pub_date=time)
           self.asserIs(recent_question.was_recently_published(), False)
       ```
5. 뷰 테스트
    - 뷰 레벨에서 코드와 상호 작용하는 사용자를 시뮬레이트하기 위해 테스트 클라어인트 클래스 Client를 사용.
    - shell에서 테스트 환경 구성
        - setup_test_environment(): 템플릿 renderer 설치 해줌.
    ```commandline
    > py manage.py shell
    >>> from django.test.utils import setup_test_envrionment
    >>> setup_test_environment()
    >>> from django.test import Client
    >>> client = Client()
    >>> response = client.get('/')
    Not Found: /
    >>> response.status_code
    404
    >>> from django.urls import reverse
    >>> response = client.get(reverse('polls:index'))
    >>> response.status_code
    200
    >>> response.content 
    b'<h1>POLL LIST</h1>\n\n    <ul>\n        \n            \n            <li><a href="/polls/2/">what&#x27;s new?</a></li>\n        \n            \n            <li><a href="/polls/1/">what&#x27;s up?</a></li>\n        \n    </ul>\n'
    >>> response.context['latest_question_list']
    <QuerySet [<Question: what's new?>, <Question: what's up?>]>
    >>> exit()
    ```
   
    - polls/views.py - 게시 되지 않은 설문조사는 출력 안되게끔 수정
    ```python
    from django.utils import timezone
    
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    ```
    - polls/tests.py - Index View 테스트 케이스 추가
    ```python
    from django.urls import reverse
      
    def create_question(question_text, days):
        """
        Create a question with the given `question_text` and published the
        given number of `days` offset to now (negative for questions published
        in the past, positive for questions that have yet to be published).
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)
    
    
    class QuestionIndexViewTests(TestCase):
        def test_no_questions(self):
            """
            If no questions exist, an appropriate message is displayed.
            """
            response = self.client.get(reverse("polls:index"))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "No polls are available.")
            self.assertQuerySetEqual(response.context["latest_question_list"], [])
    
        def test_past_question(self):
            """
            Questions with a pub_date in the past are displayed on the
            index page.
            """
            question = create_question(question_text="Past question.", days=-30)
            response = self.client.get(reverse("polls:index"))
            self.assertQuerySetEqual(response.context["latest_question_list"], [question],)
    
        def test_future_question(self):
            """
            Questions with a pub_date in the future aren't displayed on
            the index page.
            """
            create_question(question_text="Future question.", days=30)
            response = self.client.get(reverse("polls:index"))
            self.assertContains(response, "No polls are available.")
            self.assertQuerySetEqual(response.context["latest_question_list"], [])
    
        def test_future_question_and_past_question(self):
            """
            Even if both past and future questions exist, only past questions
            are displayed.
            """
            question = create_question(question_text="Past question.", days=-30)
            create_question(question_text="Future question.", days=30)
            response = self.client.get(reverse("polls:index"))
            self.assertQuerySetEqual(response.context["latest_question_list"], [question],)
    
        def test_two_past_questions(self):
            """
            The questions index page may display multiple questions.
            """
            question1 = create_question(question_text="Past question 1.", days=-30)
            question2 = create_question(question_text="Past question 2.", days=-5)
            response = self.client.get(reverse("polls:index"))
            self.assertQuerySetEqual(response.context["latest_question_list"], [question2, question1],)
    ```
6. DetailView 테스트
    - polls/views.py - 미래의 설문 번호를 알아도 접근 못하도록 수정
    ```python
    class DetailView(generic.DetailView):
        ...
    
        def get_queryset(self):
            """
            Excludes any questions that aren't published yet.
            """
            return Question.objects.filter(pub_date__lte=timezone.now())
    ```
   - polls/tests.py - 테스트 케이스 추가
    ```python
    class QuestionDetailViewTests(TestCase):
        def test_future_question(self):
            """
            The detail view of a question with a pub_date in the future
            returns a 404 not found.
            """
            future_question = create_question(question_text="Future question.", days=5)
            url = reverse("polls:detail", args=(future_question.id,))
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)
    
        def test_past_question(self):
            """
            The detail view of a question with a pub_date in the past
            displays the question's text.
            """
            past_question = create_question(question_text="Past Question.", days=-5)
            url = reverse("polls:detail", args=(past_question.id,))
            response = self.client.get(url)
            self.assertContains(response, past_question.question_text)
    ```

## 11. 앱 꾸미기
- 정적 파일: Django에서 웹 페이지를 랜더링하는데 필요한 추가 파일(html을 제외한 JS, CSS 등)
- INSTALLED_APPS > django.contrib.staticfiles 을 통해 각 앱의 정적 파일들을 프로덕션 환경에서 제공 할 수 있는 단일 위치로 수집.
1. static 디렉토리 생성
   - polls/static
   - Django의 STATICFILES_FINDERS 설정은 다양한 소스에서 정적 파일을 찾는 방법을 알고 있는 파인더 목록을 보유함.
    ```python
    [
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    ] 
    ```
    - AppDirectoriesFinder: INSTALLED_APPS 에서 “정적” 하위 디렉토리 탐색
2. style.css 생성
   - polls/static/polls/style.css
    ```css
    li a {
        color: green;
    }
    ```
3. style 적용
   - polls/templates/polls/index.html
    ```html
    {% load static %}
   
    <link rel="stylesheet" href="{% static 'polls/style.css' %}">
    ```
   - {% static %} 템플릿 태그: 정적 파일의 절대 URL을 생성
4. 배경 이미지 추가
   - polls/static/polls/images 디렉토리 추가, background.png 이미지 업로드
   - polls/static/polls/style.css 
    ```css
    body {
        background: white url("images/background.png") no-repeat;
    }
    ```

---
# 정리
## Scheduler
- 원하는 시간에 python script 를 실행하고 싶을 때 사용.
- 대표 라이브러리: APScheduler(**Advanced Python Scheduler**)
  - https://apscheduler.readthedocs.io/en/latest/
  1. 설치
    ```commandline
    > pip install apscheduler
    ```
  - 이미 존재하는 어플리케이션 내에서 실행.
  - 백엔드(Memory(default) SQLAlchemy, MongoDB, Redis 등), 프레임워크(asyncio, gevent, Tornado, Twisted, Qt 등)와 같이 사용 가능.
  - 실행 방식
    - Cron: Cron 표현으로 실행
    - Interval: 일정 주기로 실행
    - Date: 특정 날짜로 실행(사실상 Cron과 동일)
  - 스케줄러 종류
    - BlockingScheduler: 단일 스케줄러
    - BackgroundScheduler: 다중 스케줄러
    - AsyncIOScheduler
    - GeventScheduler
    - TornadoScheduler
    - TwistedScheduler
    - QtScheduler
  2. 코드
    ```python
    from apscheduler.jobstores.base import JobLookupError
    from apscheduler.schedulers.background import BackgroundScheduler
    import time
    
    class Scheduler:
        def __init__(self):
            self.scheduler = BackgroundScheduler()
            self.scheduler.start()
            self.job_id = ''
        
        def __del__(self):
            self.shutdown()
    
        def shutdown(self):
            self.scheduler.shutdown()
    
        def kill_sheduler(self, job_id):
            try:
                self.scheduler.remove_job(job_id)
            except JobLookupError as err:
                print("fail to stop Scheduler: {err}".format(err=err))
                return
        
        def hello(self, type, job_id):
            print("%s Scheduler process_id[%s] : %d" % (type, job_id, time.localtime().tm_sec))
    
        def scheduler(self, type, job_id):
            print("{type} Scheduler Start".format(type=type))
            if type == 'interval':
              self.scheduler.add_job(self.hello, type, seconds=10, id=job_id, args=(type, job_id))
            elif type == 'cron':
              self.scheduler.add_job(self.hello, type, day_of_week='mon_fri', hour='0-23', second='*/2',
                                     id=job_id, args=(type, job_id))
              
    if __name__ == '__main__':
      scheduler = Scheduler()
      scheduler.scheduler('cron', "1")
      scheduler.scheduler('interval', "2")
      
      count = 0
      while True:
        '''
        count 제한할 경우
        '''
        print("Running main process")
        time.sleep(1)
        count += 1
        if count == 10:
            scheduler.kill_sheduler("1")
            print("Kill cron Scheduler")
        elif count == 15:
            scheduler.kill_sheduler("2")
            print("Kill interval Scheduler")
    ```
- Django에서 Scheduler 사용
  1. 설치
    ```commandline
    > pip install django-apscheduler
    ```
    - settings.py 입력
    ```python
    INSTALLED_APP = [
        ...
        'django_apscheduler',
        ...
    ]
    
    # django 관리 사이트에서 런타임 타임스탬프를 표시하기 위한 형식 문자열
    APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"  # Default
    
    SCHEDULER_DEFAULT = True
    ```
  2. 코드: 하루에 한번 씩 실행하는 스케줄러
     1. operator.py 파일 작성
        - 스케줄 실행 설정 파일
  ```python
  from apschduler.schedulers.background import BackgroundScheduler
  from django_apscheduler.jobstores import register_events, DjangoJobStore
  from .views import expiry_check
  
  def start():
      scheduler = BackgroundScheduler()
      scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
      register_events(scheduler)
      @scheduler.scheduled_job('cron', hour=23, name='expiry_check')
      def auto_check():
          expiry_check()
      scheduler.start()
  ```
     2. operator.py 파일 작성
        - 작업 내용 작성 : 모델의 데이터들 중 날짜가 지난 데이터들을 자동으로 비활성화 해주기.
  ```python
  import datetime
  from .models import Subscription
  
  def expriry_check():
    today = datetime.date.today()
    
    subscriptions = Subscription.objects.filter(expiry=False)
  
    if len(subscriptions) != 0:
        for sub in subscriptions:
            if sub.end_date < today:
                sub.expiry = True
                sub.save()
  ```
     3. app.py 파일 작성
        - 서버가 실행될 때 Django가 Scheduler를 포함해서 실행시키기
  ```python
  from django.apps import AppConfig 
  from django.conf import settings
  
  class SubscriptionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subscription'
  
    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from . import operator
            operator.start()
  ```

## CSRF 방지
- 교차 사이트 요청 위조(Cross Site Request Forgeries) 방지를 위한 기능.
- POST 양식에서는 무조건 사용.
- 작성법
    ```html
    {% csrf_token %}
    ```
- 동작과정
  1. 사용자가 해당 페이지에 접속하면 Django에서 자동으로 csrf_token을 클라이언트로 보내어 cookie에 저장
  2. 사용자가 제출 버튼을 클릭하면 form과 cookie의 csrf_token을 함께 전송됨.(두 값이 다름)
  3. 전송된 token의 유효성 검증함.
  4. 유효한 요청이면 요청 처리, 유효하지 않거나(값이 없을 경우도 포함) 검증 오류시에는 403 Forbidden Response 반환
---

# 참조
- https://velog.io/@han0707/WSGI%EB%8A%94-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C
- https://wookkl.tistory.com/45
- https://it-eldorado.tistory.com/13
- https://spoqa.github.io/2019/02/15/python-timezone.html
- https://docs.djangoproject.com/en/3.0/topics/i18n/timezones/