from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0028_remove_projectai_id_alter_projectai_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectai',
            name='project',
        ),
        migrations.AddField(
            model_name='projectai',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectai',
            name='link',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='projectai',
            name='title',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
    ]
