# Generated by Django 3.2.20 on 2023-08-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('benefits', models.TextField()),
                ('duration', models.IntegerField()),
                ('sessions_needed', models.IntegerField()),
                ('duration_of_results', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('faq1', models.CharField(max_length=500)),
                ('faq1_answer', models.TextField()),
                ('faq2', models.CharField(max_length=500)),
                ('faq2_answer', models.TextField()),
                ('faq3', models.CharField(max_length=500)),
                ('faq3_answer', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
