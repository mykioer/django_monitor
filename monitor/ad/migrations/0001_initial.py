# Generated by Django 2.0.1 on 2018-06-11 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=30, unique=True)),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='RuleIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(0, '无响应'), (1, 'CPU使用率'), (2, '内存使用率'), (3, '磁盘Inode'), (4, '磁盘空间'), (5, '磁盘IOPS'), (6, '网络流量'), (7, '连接数')])),
                ('time', models.IntegerField(choices=[(1, '1分钟')])),
                ('triggers_times', models.IntegerField(choices=[(0, '连续1次'), (1, '连续3次'), (2, '连续5次'), (3, '连续10次'), (4, '连续15次'), (5, '连续30次')])),
                ('triggers_diff', models.IntegerField(choices=[(0, '>='), (1, '>'), (2, '<='), (3, '<'), (4, '='), (5, '!=')])),
                ('triggers_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RuleResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('date', models.IntegerField()),
                ('host', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('memo', models.TextField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Triggers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.IntegerField(choices=[(0, '普通管理员'), (1, '超级管理员')])),
                ('name', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('memo', models.TextField(null=True)),
                ('atime', models.DateTimeField(auto_now=True)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='templates',
            name='triggers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad.Triggers'),
        ),
        migrations.AddField(
            model_name='ruleindex',
            name='triggers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad.Triggers'),
        ),
        migrations.AddField(
            model_name='hostgroup',
            name='templates',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad.Templates'),
        ),
        migrations.AddField(
            model_name='asset',
            name='hostgroup',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ad.HostGroup'),
        ),
        migrations.AddField(
            model_name='asset',
            name='user_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad.UserGroup'),
        ),
    ]