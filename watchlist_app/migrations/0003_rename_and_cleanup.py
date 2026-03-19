from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_streamplatfrom_watchlist_delete_movie'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StreamPlatfrom',
            new_name='StreamPlatform',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='storyline',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='watchlist',
                to='watchlist_app.streamplatform',
            ),
        ),
    ]
