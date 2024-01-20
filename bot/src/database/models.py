from datetime import datetime
from peewee import Model, SqliteDatabase, IntegerField, DateTimeField, CharField, FloatField

db = SqliteDatabase('../database.db')


class _BaseModel(Model):
    class Meta:
        database = db


class ReferralLink(_BaseModel):
    class Meta:
        db_table = 'referral_links'

    name = CharField(unique=True)
    user_count = IntegerField(default=0)
    passed_op_count = IntegerField(default=0)


class User(_BaseModel):
    class Meta:
        db_table = 'users'

    name = CharField(default='Пользователь')
    telegram_id = IntegerField(unique=True, null=False)
    registration_timestamp = DateTimeField(default=datetime.now())
    referral_link = CharField(null=True)
    onewin_id = IntegerField(null=True, default=None)
    language_code = CharField(max_length=2, null=True, default=None)


class Admin(_BaseModel):
    class Meta:
        db_table = 'admins'

    telegram_id = IntegerField(unique=True, null=False)
    name = CharField()


class Channel(_BaseModel):
    class Meta:
        db_table = 'channels'

    channel_id = IntegerField()
    title = CharField()
    url = CharField()


class OneWinRegistration(_BaseModel):
    class Meta:
        db_table = 'one_win_registrations'

    one_win_id = IntegerField(primary_key=True)
    timestamp = DateTimeField(default=datetime.now)


class OneWinDeposit(_BaseModel):
    class Meta:
        db_table = 'one_win_deposits'
    
    id = IntegerField(primary_key=True)
    one_win_id = IntegerField()
    amount = FloatField()
    timestamp = DateTimeField(default=datetime.now)


def register_models() -> None:
    for model in _BaseModel.__subclasses__():
        model.create_table()
