from faker import Faker
from connect import connect
from load_config import load_config
from insert_many import insert_many
from entities.Status import Status
from entities.User import User
from entities.Task import Task
from random import randint


fake = Faker()

status_values = [
    Status(name="new"),
    Status(name="in progress"),
    Status(name="completed"),
]


def create_seed():
    config = load_config()

    engine = connect(config)

    statuses: list[Status] = insert_many(engine, status_values)
    print(statuses)

    new_users: list[User] = []

    for _ in range(0, 100):
        new_users.append(User(fullname=fake.name(), email=fake.email()))

    users: list[User] = insert_many(engine, new_users)
    print(users)

    new_tasks: list[Task] = []

    for user in users:
        tasks_count = randint(0, 3)
        if tasks_count == 0:
            continue

        for _ in range(0, tasks_count):
            new_tasks.append(
                Task(
                    title=fake.sentence(),
                    description=fake.text(),
                    status_id=statuses[randint(0, 2)].id,
                    user_id=user.id,
                )
            )

    tasks: list[Task] = insert_many(engine, new_tasks)
    print(tasks)


if __name__ == "__main__":
    create_seed()
    print("Success")
