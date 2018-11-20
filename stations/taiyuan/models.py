# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db import connection


class AdminInfo(models.Model):
    id = models.IntegerField()
    user_id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_info'


class AlarmInfo(models.Model):
    alarm_id = models.AutoField(primary_key=True)
    alarm_time = models.DateTimeField()
    camera_id = models.IntegerField()
    camera_ip = models.CharField(max_length=40)
    alarm_type = models.ForeignKey('AlarmType', models.DO_NOTHING)
    alarm_data = models.IntegerField(blank=True, null=True)
    alarm_level = models.CharField(max_length=50, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    ped_info = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    suggestion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alarm_info'


class AlarmType(models.Model):
    alarm_type_id = models.CharField(max_length=10)
    alarm_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'alarm_type'


class CameraInfo(models.Model):
    camera_id = models.IntegerField(primary_key=True)
    camera_ip = models.CharField(max_length=50, blank=True, null=True)
    camera_name = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    rtsp = models.CharField(max_length=100, blank=True, null=True)
    smart_function = models.CharField(max_length=100, blank=True, null=True)
    roi = models.CharField(db_column='ROI', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    api_url = models.CharField(max_length=100, blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    heat_map = models.CharField(max_length=10, blank=True, null=True)
    ped_dress = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camera_info'


class DevInvideo(models.Model):
    videoid = models.IntegerField(blank=True, null=True)
    devname = models.CharField(max_length=64)
    devtype = models.CharField(max_length=64, blank=True, null=True)
    videox = models.CharField(max_length=8, blank=True, null=True)
    videoy = models.CharField(max_length=8, blank=True, null=True)
    devx = models.CharField(max_length=8, blank=True, null=True)
    devy = models.CharField(max_length=8, blank=True, null=True)
    devinfo = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dev_invideo'


class Device(models.Model):
    tid = models.IntegerField(db_column='TID', primary_key=True)  # Field name made lowercase.
    epc = models.CharField(db_column='EPC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    devicearea = models.CharField(db_column='DeviceArea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isonline = models.CharField(db_column='IsOnline', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'device'


class EquipmentInfo(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    serial_number = models.IntegerField(blank=True, null=True)
    equipment_name = models.CharField(max_length=10)
    equipment_position = models.CharField(max_length=10)
    status = models.CharField(max_length=10, blank=True, null=True)
    ip_address = models.CharField(max_length=50)
    rtsp_address = models.CharField(max_length=100)
    alarm_type_id1 = models.ForeignKey(AlarmType, models.DO_NOTHING, db_column='alarm_type_id1')
    alarm_type_id2 = models.CharField(max_length=11, blank=True, null=True)
    server = models.ForeignKey('IntellegentServerInfo', models.DO_NOTHING, blank=True, null=True)
    intellegent_camera_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment_info'


class FlowcountCameraInfo(models.Model):
    camera_id = models.IntegerField()
    camera_name = models.CharField(max_length=10)
    camera_position = models.CharField(max_length=10)
    camera_ip = models.CharField(max_length=50)
    alarm_type = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'flowcount_camera_info'

class FlowcountInfoManager(models.Manager):
    def max_count(self,begin_time,end_time):
        cursor = connection.cursor()
        cursor.execute("select max(flowcount) from flowcount_info where alarm_time between %s and %s",([begin_time],[end_time]))
        max_value = cursor.fetchone()[0]
        if max_value == None:
            max_value = 0
        return max_value

class FlowcountInfo(models.Model):
    alarm_time = models.DateTimeField()
    camera_id = models.IntegerField()
    camera_ip = models.CharField(max_length=40)
    alarm_type_id = models.CharField(max_length=10)
    flowcount = models.IntegerField()
    img = models.CharField(max_length=100, blank=True, null=True)
    ped_info = models.CharField(max_length=500, blank=True, null=True)

    objects = FlowcountInfoManager()

    class Meta:
        managed = False
        db_table = 'flowcount_info'


class FlowcountInfoHis(models.Model):
    alarm_time = models.DateTimeField()
    start_time = models.DateTimeField()
    camera_id = models.IntegerField()
    camera_ip = models.CharField(max_length=40)
    alarm_type_id = models.CharField(max_length=10)
    flowcount = models.IntegerField()
    img = models.CharField(max_length=100, blank=True, null=True)
    ped_info = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flowcount_info_his'


class FlowcountInfoTotal(models.Model):
    id = models.IntegerField(primary_key=True)
    alarm_time = models.DateTimeField()
    direction = models.IntegerField()
    alarm_data = models.IntegerField()
    alarm_position = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'flowcount_info_total'


class IntellegentServerInfo(models.Model):
    server_id = models.AutoField(primary_key=True)
    server_ip = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'intellegent_server_info'


class MonStatusRfidmap(models.Model):
    s_fid = models.AutoField(db_column='S_FID', primary_key=True)  # Field name made lowercase.
    s_rfidlabcode = models.CharField(db_column='S_RFIDLABCODE', max_length=30)  # Field name made lowercase.
    s_statuscode = models.CharField(db_column='S_STATUSCODE', max_length=4)  # Field name made lowercase.
    d_updatetime = models.DateTimeField(db_column='D_UPDATETIME', blank=True, null=True)  # Field name made lowercase.
    s_description = models.CharField(db_column='S_DESCRIPTION', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mon_status_rfidmap'


class MonStatusRfidmapHis(models.Model):
    s_fid = models.CharField(db_column='S_FID', primary_key=True, max_length=50)  # Field name made lowercase.
    s_rfidlabcode = models.CharField(db_column='S_RFIDLABCODE', max_length=30)  # Field name made lowercase.
    s_statuscode = models.CharField(db_column='S_STATUSCODE', max_length=4)  # Field name made lowercase.
    d_updatetime = models.DateTimeField(db_column='D_UPDATETIME', blank=True, null=True)  # Field name made lowercase.
    s_description = models.CharField(db_column='S_DESCRIPTION', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mon_status_rfidmap_his'


class QueueInfo(models.Model):
    alarm_id = models.AutoField(primary_key=True)
    alarm_time = models.DateTimeField(db_column='alarm_Time')  # Field name made lowercase.
    camera_id = models.IntegerField()
    camera_ip = models.CharField(max_length=40)
    alarm_type_id = models.CharField(max_length=10)
    alarm_window = models.CharField(max_length=150, blank=True, null=True)
    alarm_data = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queue_info'


class RegioncountInfo(models.Model):
    alarm_time = models.DateTimeField()
    camera_id = models.IntegerField()
    camera_ip = models.CharField(max_length=40)
    alarm_type_id = models.CharField(max_length=10)
    alarm_data = models.IntegerField()
    heat_img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regioncount_info'


class TrackInfo(models.Model):
    alarm_id = models.AutoField(primary_key=True)
    alarm_time = models.DateTimeField(db_column='alarm_Time')  # Field name made lowercase.
    camera_id = models.IntegerField()
    camera_ip = models.CharField(max_length=40)
    alarm_type_id = models.CharField(max_length=10)
    person_id = models.CharField(max_length=40, blank=True, null=True)
    img = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'track_info'
