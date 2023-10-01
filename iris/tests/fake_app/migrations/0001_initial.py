# Generated by Django 4.2.5 on 2023-10-01 08:47

from django.db import migrations, models
import django.db.models.deletion
import iris.fields.sequential_number_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sequential_number', iris.fields.sequential_number_field.SequentialNumberField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fake_app.order')),
            ],
        ),
    ]