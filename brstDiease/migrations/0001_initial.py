# Generated by Django 3.0.6 on 2021-04-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrstPredResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radius_mean', models.FloatField()),
                ('texture_mean', models.FloatField()),
                ('perimeter_mean', models.FloatField()),
                ('area_mean', models.FloatField()),
                ('smoothness_mean', models.FloatField()),
                ('compactness_mean', models.FloatField()),
                ('concavity_mean', models.FloatField()),
                ('concave_points_mean', models.FloatField()),
                ('symmetry_mean', models.FloatField()),
                ('fractal_dimension_mean', models.FloatField()),
                ('radius_se', models.FloatField()),
                ('texture_se', models.FloatField()),
                ('perimeter_se', models.FloatField()),
                ('area_se', models.FloatField()),
                ('smoothness_se', models.FloatField()),
                ('compactness_se', models.FloatField()),
                ('concavity_se', models.FloatField()),
                ('concave_points_se', models.FloatField()),
                ('symmetry_se', models.FloatField()),
                ('fractal_dimension_se', models.FloatField()),
                ('radius_worst', models.FloatField()),
                ('texture_worst', models.FloatField()),
                ('perimeter_worst', models.FloatField()),
                ('area_worst', models.FloatField()),
                ('smoothness_worst', models.FloatField()),
                ('compactness_worst', models.FloatField()),
                ('concavity_worst', models.FloatField()),
                ('concave_points_worst', models.FloatField()),
                ('symmetry_worst', models.FloatField()),
                ('fractal_dimension_worst', models.FloatField()),
                ('PredictRes', models.CharField(max_length=30)),
                ('Accuracy', models.FloatField()),
            ],
        ),
    ]
