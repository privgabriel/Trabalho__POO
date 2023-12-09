# Generated by Django 4.2.7 on 2023-12-09 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='CriarUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AlterField(
            model_name='matricula',
            name='periodo',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno')], default='Matutino', max_length=10),
        ),
    ]