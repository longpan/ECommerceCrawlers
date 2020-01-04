from peewee import *

database = MySQLDatabase('mytest', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '47.112.28.50', 'port': 3306, 'user': 'root', 'password': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class BossModel(BaseModel):
    area = CharField(null=True)
    company_name = CharField(null=True)
    edu_leve = CharField(null=True)
    name = CharField(null=True)
    salary = CharField(null=True)
    url = CharField(null=True)
    work_exp = CharField(null=True)
    city = CharField(null=True)
    key_word = CharField(null=True)
    salary_max = CharField(column_name='salaryMax', null=True)
    salary_min = CharField(column_name='salaryMin', null=True)

    class Meta:
        table_name = 'boss'

class Lagou(BaseModel):
    area = CharField(null=True)
    city = CharField(null=True)
    company_name = CharField(null=True)
    detail = TextField(null=True)
    edu_level = CharField(column_name='eduLevel', null=True)
    id = BigAutoField()
    key_word = CharField(null=True)
    position_advantage = CharField(column_name='positionAdvantage', null=True)
    position_name = CharField(column_name='positionName', null=True)
    salery = CharField(null=True)
    salery_max = CharField(column_name='saleryMax', null=True)
    salery_min = CharField(column_name='saleryMin', null=True)
    url = CharField(null=True)
    working_exp = TextField(column_name='workingExp', null=True)

    class Meta:
        table_name = 'lagou'

class Qcwy(BaseModel):
    area = CharField(null=True)
    city = CharField(null=True)
    company_info = CharField(null=True)
    company_name = CharField(null=True)
    detail = TextField(null=True)
    id = BigAutoField()
    key_word = CharField(null=True)
    salery = CharField(null=True)
    salery_max = CharField(column_name='saleryMax', null=True)
    salery_min = CharField(column_name='saleryMin', null=True)
    time = CharField(null=True)
    title = CharField(null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 'qcwy'

class User(BaseModel):
    add_time = DateTimeField(null=True)
    id = BigAutoField()
    modify_time = DateTimeField(null=True)
    name = CharField(null=True)

    class Meta:
        table_name = 'user'

class Zhilian(BaseModel):
    city = CharField(null=True)
    company_area = CharField(null=True)
    company_id = CharField(null=True)
    company_name = CharField(null=True)
    company_scale = CharField(null=True)
    company_type = CharField(null=True)
    edu_level = CharField(column_name='eduLevel', null=True)
    empl_type = CharField(column_name='emplType', null=True)
    id = BigAutoField()
    job_name = CharField(column_name='jobName', null=True)
    key_word = CharField(null=True)
    number = CharField(null=True)
    position_url = CharField(column_name='positionURL', null=True)
    salery = CharField(null=True)
    salery_max = CharField(column_name='saleryMax', null=True)
    salery_min = CharField(column_name='saleryMin', null=True)
    state = CharField(null=True)
    update_date = CharField(column_name='updateDate', null=True)
    url = CharField(null=True)
    welfare = CharField(null=True)
    working_exp = TextField(column_name='workingExp', null=True)

    class Meta:
        table_name = 'zhilian'

