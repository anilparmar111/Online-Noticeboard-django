# Generated by Django 3.0.5 on 2020-04-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_uploadmetirial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadMetirial_CE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('file', models.FileField(upload_to='CE/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UploadMetirial',
        ),
    ]