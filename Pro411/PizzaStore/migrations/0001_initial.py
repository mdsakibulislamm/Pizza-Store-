# Generated by Django 3.0.3 on 2020-03-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('catagory', models.CharField(choices=[('pizza', 'pizza'), ('pasta', 'pasta'), ('drinks', 'drinks'), ('deals', 'deals'), ('appetiser', 'appetiser')], max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='PizzaStore/images')),
            ],
        ),
    ]