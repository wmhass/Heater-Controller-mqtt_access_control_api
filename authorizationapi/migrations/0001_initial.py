# Generated by Django 2.2 on 2019-10-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MqttAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('pw', models.CharField(max_length=100)),
                ('superuser', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.RunSQL("""
            ALTER TABLE
              authorizationapi_mqttaccount
            ADD
              CONSTRAINT superuser CHECK (superuser = 0 OR superuser = 1)
        """),
        migrations.RunSQL("""
            INSERT INTO authorizationapi_mqttaccount(username, pw, superuser)
            VALUES
            ('admin', '21232f297a57a5a743894a0e4a801fc3', 1)
        """),
        migrations.RunSQL("""
            INSERT INTO authorizationapi_mqttaccount(username, pw, superuser)
            VALUES
            ('admin2', '21232f297a57a5a743894a0e4a801fc3', 1)
        """),
        migrations.RunSQL("""
            INSERT INTO authorizationapi_mqttaccount(username, pw, superuser)
            VALUES
            ('mqtt_observer', '21232f297a57a5a743894a0e4a801fc3', 1)
        """),
        migrations.RunSQL("""
            INSERT INTO authorizationapi_mqttaccount(username, pw, superuser)
            VALUES
            ('mqtt_http_api', '21232f297a57a5a743894a0e4a801fc3', 1)
        """),
        migrations.CreateModel(
            name='MqttAcl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('topic', models.CharField(max_length=100)),
                ('rw', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.RunSQL("""
            ALTER TABLE
              authorizationapi_mqttacl
            ADD
              CONSTRAINT rw CHECK (rw >= 1 AND rw <= 4)
        """),
        migrations.RunSQL("""
            INSERT INTO authorizationapi_mqttacl(username, topic, rw)
            VALUES
            ('admin', 'user/admin', 3)
        """),
        migrations.RunSQL("""
            INSERT INTO authorizationapi_mqttacl(username, topic, rw)
            VALUES
            ('admin2', 'user/admin2', 3)
        """)
    ]
