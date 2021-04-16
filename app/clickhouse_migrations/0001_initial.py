from django_clickhouse import migrations

from app.clickhouse_models import ClickHouseHistory


class Migration(migrations.Migration):
    operations = [
        migrations.CreateTable(ClickHouseHistory)
    ]