from datetime import datetime
from peewee import Model, SqliteDatabase, TextField, IntegerField, DateTimeField, CharField, ForeignKeyField, FloatField

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


class OneWinRegistration(Model):
    class Meta:
        db_table = 'one_win_registrations'

    sub_id = IntegerField(primary_key=True)
    one_win_id = IntegerField()


class OneWinDeposit(Model):
    class Meta:
        db_table = 'one_win_deposits'

    sub_id = IntegerField()
    one_win_id = IntegerField()
    amount = FloatField()


def register_models() -> None:
    for model in _BaseModel.__subclasses__():
        model.create_table()
