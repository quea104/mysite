# Django 시작하기

## ※ PyCharm IDE 환경에서 개발
 
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

USE_TZ = True
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

---
# 프로그래밍
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
---

# 참조
- https://velog.io/@han0707/WSGI%EB%8A%94-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C
- https://wookkl.tistory.com/45
- https://it-eldorado.tistory.com/13
- https://spoqa.github.io/2019/02/15/python-timezone.html
- https://docs.djangoproject.com/en/3.0/topics/i18n/timezones/