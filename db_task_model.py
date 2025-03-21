from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select

#Define a Task model clsas that inherits from SQLModel

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str = Field(default="")
    isComplete: bool = Field(default=False)

#Database Name
mysql_name = "test_db"

# Construct MySQL connection URL using PyMySQL driver
# Format: mysql+pymysql://username:password@host:port/database_name
mysql_url = f"mysql+pymysql://root:Smollbean0203@localhost:3306/{mysql_name}"
#Create database engien using the connection URL
engine = create_engine(mysql_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        #yield the session to the caller
         # This allows the session to be used as a context manager or dependency
        yield session