# Generated by Django 4.0.3 on 2022-04-24 08:07

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='GroupService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'type_service',
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.DateField()),
                ('sex', models.CharField(max_length=1)),
                ('operations', models.TextField()),
                ('contraindications', models.TextField()),
                ('code_klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pet',
            },
        ),
        migrations.CreateModel(
            name='PetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'pet_type',
            },
        ),
        migrations.CreateModel(
            name='MedicalCard',
            fields=[
                ('pet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='site_vetclinic.pet')),
            ],
            options={
                'db_table': 'medical_card',
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabinet_number', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'timetable',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('group_service', models.ManyToManyField(to='site_vetclinic.groupservice')),
            ],
            options={
                'db_table': 'speciality',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('price', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_vetclinic.groupservice')),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.AddField(
            model_name='pet',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_vetclinic.pettype'),
        ),
        migrations.CreateModel(
            name='VetProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_of_birth', models.DateField()),
                ('date_employment', models.DateField()),
                ('residence_address', models.CharField(max_length=30)),
                ('passport', models.CharField(max_length=30)),
                ('personal_information', models.TextField()),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_vetclinic.speciality')),
            ],
            options={
                'db_table': 'vet_profile',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Клиент', to=settings.AUTH_USER_MODEL)),
                ('code_timetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_vetclinic.timetable')),
                ('code_typeservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_vetclinic.service')),
                ('code_vet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Врач', to=settings.AUTH_USER_MODEL)),
                ('code_medicalcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_vetclinic.medicalcard')),
            ],
            options={
                'db_table': 'record',
            },
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms', models.CharField(max_length=20)),
                ('diagnosis', models.CharField(max_length=20)),
                ('treatment_regimen', models.CharField(max_length=20)),
                ('recomendations', models.CharField(max_length=20)),
                ('code_typeservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_vetclinic.service')),
                ('code_medicalcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_vetclinic.medicalcard')),
            ],
            options={
                'db_table': 'medical_record',
            },
        ),
    ]