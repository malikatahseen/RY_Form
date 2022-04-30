# Generated by Django 4.0.4 on 2022-04-28 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RY_Enquiry_Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id', models.IntegerField(max_length=200)),
                ('Reg_no', models.IntegerField(max_length=200)),
                ('Mill', models.TextField(max_length=200)),
                ('Customer', models.TextField(max_length=200)),
                ('Marketing_Zone', models.TextField(max_length=200)),
                ('Payment_Term', models.TextField(max_length=200)),
                ('Narration', models.TextField(max_length=200)),
                ('Reason_For_Non_Acception', models.TextField(max_length=200)),
                ('Replied_From_the_mill', models.TextField(max_length=200)),
                ('Acceptance_from_the_mill', models.TextField(max_length=200)),
                ('Date', models.TextField(max_length=200)),
                ('Email_Details', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RY_Enquiry_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Counts', models.TextField(max_length=200)),
                ('Quality', models.TextField(max_length=200)),
                ('Type', models.TextField(max_length=200)),
                ('Blend', models.TextField(max_length=200)),
                ('Shade', models.TextField(max_length=200)),
                ('Shade_Ref', models.TextField(max_length=200)),
                ('Depth', models.TextField(max_length=200)),
                ('UOM', models.TextField(max_length=200)),
                ('Quantity', models.TextField(max_length=200)),
                ('Status', models.TextField(max_length=200)),
                ('Reg_no', models.IntegerField(max_length=200)),
                ('Id', models.IntegerField(max_length=200)),
            ],
        ),
    ]
