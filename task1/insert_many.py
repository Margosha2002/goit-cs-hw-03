from sqlmodel import SQLModel, Session


def insert_many(engine, items: list[SQLModel]):
    rows = []

    try:
        with Session(engine) as session:
            session.add_all(items)
            session.commit()

            for item in items:
                session.refresh(item)
                rows.append(item)

    except Exception as error:
        print(error)
    finally:
        return rows
