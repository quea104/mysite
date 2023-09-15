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