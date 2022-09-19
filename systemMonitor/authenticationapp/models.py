# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TblBenchmark(models.Model):
    bnc_id = models.AutoField(primary_key=True)
    bnc_process = models.CharField(
        unique=True, max_length=255, db_collation='utf8mb3_general_ci')
    bnc_normal = models.IntegerField(blank=True, null=True)
    bnc_warning = models.IntegerField(blank=True, null=True)
    bnc_critical = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_benchmark'


class TblClients(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(
        max_length=255, db_collation='utf8mb3_general_ci')
    client_email = models.CharField(
        max_length=200, db_collation='utf8mb3_general_ci')
    client_contact = models.CharField(
        max_length=30, db_collation='utf8mb3_general_ci')
    client_address = models.TextField()
    client_creation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_clients'
        unique_together = (('client_name', 'client_email'),)

    def __str__(request):
        return(request.client_name)


class TblEvent(models.Model):
    event_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    site_id = models.IntegerField()
    system_id = models.IntegerField()
    bnc_id = models.IntegerField()
    event_value = models.IntegerField()
    event_type = models.CharField(
        max_length=15, db_collation='utf8mb3_general_ci')
    event_email = models.TextField(db_collation='utf8mb3_general_ci')
    event_emaildelivery = models.IntegerField()
    event_creation_date = models.DateTimeField(blank=True, null=True)
    tmp_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_event'


class TblEventTmp(models.Model):
    client = models.CharField(
        max_length=255, db_collation='utf8mb3_general_ci')
    site = models.CharField(max_length=255, db_collation='utf8mb3_general_ci')
    system = models.CharField(
        max_length=255, db_collation='utf8mb3_general_ci')
    bench = models.CharField(max_length=255, db_collation='utf8mb3_general_ci')
    event_value = models.IntegerField()
    event_email = models.TextField(db_collation='utf8mb3_general_ci')
    event_emaildelivery = models.CharField(
        max_length=50, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'tbl_event_tmp'


class TblSites(models.Model):
    site_id = models.AutoField(primary_key=True)
    site_name = models.CharField(
        max_length=255, db_collation='utf8mb3_general_ci')
    site_email = models.CharField(
        max_length=200, db_collation='utf8mb3_general_ci')
    site_contact = models.CharField(
        max_length=30, db_collation='utf8mb3_general_ci')
    site_address = models.TextField()
    site_status = models.IntegerField()
    client_id = models.IntegerField()
    site_creation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_sites'
        unique_together = (('site_name', 'site_email', 'client_id'),)

    def __str__(request):
        return(request.site_name)

class TblStatus(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status_name = models.CharField(
        unique=True, max_length=50, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'tbl_status'


class TblSystem(models.Model):
    system_id = models.AutoField(primary_key=True)
    system_name = models.CharField(
        max_length=200, db_collation='utf8mb3_general_ci')
    system_ip = models.CharField(
        max_length=30, db_collation='utf8mb3_general_ci')
    system_use = models.TextField()
    system_status = models.IntegerField()
    site_id = models.IntegerField()
    system_creation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_system'
        unique_together = (('system_name', 'system_ip', 'site_id'),)

    def __str__(request):
        return(request.system_name)

class TblTmpclear(models.Model):
    tmp_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbl_tmpclear'
