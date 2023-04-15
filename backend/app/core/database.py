import edgedb

from app.core.config import settings

edgedb_client = edgedb.create_async_client(dsn=settings.EDGEDB_DSN)
