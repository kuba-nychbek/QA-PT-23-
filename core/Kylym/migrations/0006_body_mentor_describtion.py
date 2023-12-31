# Generated by Django 4.2.5 on 2023-10-02 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kylym', '0005_alter_mentor_options_sponsor_second_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='mentor',
            name='describtion',
            field=models.CharField(default='text field', max_length=100, verbose_name='describtion'),
        ),
    ]
