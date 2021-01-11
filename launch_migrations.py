import os 
import json
import queries

from models import db

def launch_migrations():
    SECRETS = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'secrets.json'
    )

    with open(SECRETS, 'r') as f:
        raw = json.loads(f.read().strip())

    DB_INFO = {
        'host': raw["DATABASE_HOST"],
        'port': 5433,
        'dbname': raw["DATABASE_NAME"],
        'user': raw["DATABASE_USER"],
        'password': raw["DATABASE_PASS"],
    }

    db_endpoint = queries.uri(**DB_INFO)
    
    import sqlalchemy as sa
    
    db_engine = sa.create_engine(db_endpoint)

    db.create_all(bind=db_engine)

    db_engine.dispose()


if __name__ == '__main__':
    launch_migrations()
    