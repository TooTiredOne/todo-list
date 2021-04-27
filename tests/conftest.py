import pytest

from todo_list import create_app
from todo_list.model import Task
from todo_list.model import db as db_instance

# used to populate database
ACTIVE_TASK_IDS = list(range(1, 6))
FINISHED_TASK_IDS = list(range(6, 11))
ALL_TASK_IDS = FINISHED_TASK_IDS + ACTIVE_TASK_IDS


@pytest.fixture(name='app')
def _app():
    cur_app = create_app()
    with cur_app.app_context():
        yield cur_app


@pytest.fixture(name='db')
def _db(app):
    yield db_instance


@pytest.fixture()
def active_tasks(db):
    tasks = []
    # adding active tasks
    for task_id in ACTIVE_TASK_IDS:
        task = Task(description=f'task{task_id}')
        db.session.add(task)
        tasks.append(task)
    db.session.commit()
    return tasks


@pytest.fixture()
def finished_tasks(db):
    tasks = []
    # adding finished tasks
    for task_id in FINISHED_TASK_IDS:
        task = Task(description=f'task{task_id}')
        task.finished = True
        db.session.add(task)
        tasks.append(task)

    db.session.commit()
    return tasks


# client with empty database
@pytest.fixture()
def client(app):
    with app.test_client() as cur_client:
        yield cur_client
