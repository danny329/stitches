# Generated by Django 2.2.3 on 2019-07-30 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Back',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('back_style', models.CharField(max_length=50)),
                ('back_image', models.ImageField(upload_to='pics/Back')),
            ],
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_style', models.CharField(max_length=50)),
                ('button_image', models.ImageField(upload_to='pics/Button')),
            ],
        ),
        migrations.CreateModel(
            name='ButtonHole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_hole_style', models.CharField(max_length=50)),
                ('button_hole_image', models.ImageField(upload_to='pics/ButtonHole')),
            ],
        ),
        migrations.CreateModel(
            name='ClothMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('back', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='back_cm', to='selection.Back')),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='button_cm', to='selection.Button')),
                ('button_hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buttonhole_cm', to='selection.ButtonHole')),
            ],
        ),
        migrations.CreateModel(
            name='ClothType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_type_style', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Collar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collar_style', models.CharField(max_length=50)),
                ('collar_image', models.ImageField(upload_to='pics/Collar')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_style', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuff_style', models.CharField(max_length=50)),
                ('cuff_image', models.ImageField(upload_to='pics/Cuff')),
            ],
        ),
        migrations.CreateModel(
            name='Front',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_style', models.CharField(max_length=50)),
                ('front_image', models.ImageField(upload_to='pics/Front')),
            ],
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern_style', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pocket_style', models.CharField(max_length=50)),
                ('pocket_image', models.ImageField(upload_to='pics/Pocket')),
            ],
        ),
        migrations.CreateModel(
            name='ShirtFit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shirt_fit_style', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StandardSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_size_style', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=25)),
                ('neck', models.DecimalField(decimal_places=2, max_digits=5)),
                ('chest', models.DecimalField(decimal_places=2, max_digits=5)),
                ('waist', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hips', models.DecimalField(decimal_places=2, max_digits=5)),
                ('shirt_length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('shoulders', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sleeve_length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cuff', models.DecimalField(decimal_places=2, max_digits=5)),
                ('arm_hole', models.DecimalField(decimal_places=2, max_digits=5)),
                ('biceps', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('shirt_fit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shirtfit', to='selection.ShirtFit')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userm', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('back', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='back', to='selection.Back')),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='button', to='selection.Button')),
                ('button_hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buttonhole', to='selection.ButtonHole')),
                ('cloth_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothmenu', to='selection.ClothMenu')),
                ('collar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collar', to='selection.Collar')),
                ('cuff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuff', to='selection.Cuff')),
                ('front', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='front', to='selection.Front')),
                ('pocket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pocket', to='selection.Pocket')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Measurement', to='selection.Measurement')),
                ('standard_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='standardsize', to='selection.StandardSize')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Design',
                'verbose_name_plural': 'Designs',
            },
        ),
        migrations.AddField(
            model_name='clothmenu',
            name='cloth_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothtype', to='selection.ClothType'),
        ),
        migrations.AddField(
            model_name='clothmenu',
            name='collar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collar_cm', to='selection.Collar'),
        ),
        migrations.AddField(
            model_name='clothmenu',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Color', to='selection.Color'),
        ),
        migrations.AddField(
            model_name='clothmenu',
            name='cuff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuff_cm', to='selection.Cuff'),
        ),
        migrations.AddField(
            model_name='clothmenu',
            name='front',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='front_cm', to='selection.Front'),
        ),
        migrations.AddField(
            model_name='clothmenu',
            name='pattern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pattern', to='selection.Pattern'),
        ),
        migrations.AddField(
            model_name='clothmenu',
            name='pocket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pocket_cm', to='selection.Pocket'),
        ),
        migrations.AddField(
            model_name='clothmenu',
            name='standard_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standardsize_cm', to='selection.StandardSize'),
        ),
    ]
