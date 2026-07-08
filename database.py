from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://neondb_owner:npg_1ljZA6PzHShX@ep-dark-field-ahrx4hta-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
# we are connecting to a postgresql database based on the cloud

# click the show password and copy the complete connection string


# create sqlalchemy engine
# the engine is responsible for connecting for connecting fastapi

engine = create_engine(DATABASE_URL)

# create session as every database tables will inherit from this class

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
# dependency injection this function provides a databse session whenever an API requires database access

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

