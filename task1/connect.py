from load_config import load_config
from sqlmodel import create_engine, SQLModel


def connect(config):
    engine = create_engine(
        f'postgresql://{config["user"]}:{config["password"]}@{config["host"]}:5432/{config["database"]}'
    )
    SQLModel.metadata.create_all(engine)
    return engine


if __name__ == "__main__":
    config = load_config()
    connect(config)
