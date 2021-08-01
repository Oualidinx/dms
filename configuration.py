class Config:
    LANGUAGES = ['en', 'fr', 'ar']
    SECRET_KEY = 'a152a07d90532b5ceebbcae3e69dab2f352fb70c4591c25d8742794959c8d35bb512f7974dfaed93915ba93dd773536156 \
                    5c3942f45ff32ab65e75cb2ae1ccf214a83362ee9e5e953c6aae9ea0c3ed177393d9de8c7ccafa80ab6f9833e619e9f3d\
                    845a49fed707ffe5d000146a240a0b38acd969600ed4a4464db0d1f325f7a'

    @staticmethod
    def init_app(self):
        pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'


class ProdConfig(Config):
    DEBUG = False
    SQLACHEMY_DATABASE_URI = 'sqlite:///prod.db'


class TestConfig(Config):
    DEBUG = True
    SQLACHEMY_DATABASE_URI = 'sqlite:///test.db'


config = {
    'developpment': DevConfig,
    'test': TestConfig,
    'production': ProdConfig
}
