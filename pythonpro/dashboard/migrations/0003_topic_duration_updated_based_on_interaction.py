# Generated by Django 3.0.2 on 2020-01-31 12:44

from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Topic = apps.get_model('modules', 'Topic')

    db_alias = schema_editor.connection.alias
    for topic in Topic.objects.using(db_alias).all():
        interaction_duration_dct = topic.topicinteraction_set.order_by('-creation').values('topic_duration').first()
        if interaction_duration_dct is not None:
            topic.duration = interaction_duration_dct['topic_duration']
            topic.save()


def reverse_func(apps, schema_editor):
    """
    Set Topic's duration back to 0
    :param apps:
    :param schema_editor:
    :return:
    """
    Topic = apps.get_model('modules', 'Topic')
    Topic.objects.all().update(duration=0)


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0002_auto_20190812_1627'),
        ('modules', '0011_created_duration_on_topic'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
