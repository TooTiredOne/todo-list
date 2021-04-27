import pytest

from todo_list.model import Task


@pytest.mark.usefixtures('active_tasks', 'finished_tasks')
def test_finish_non_existing_task(client):

    response = client.patch('/finish/15')

    assert response.status_code == 404


@pytest.mark.usefixtures('active_tasks')
def test_finish_existing_task(client, finished_tasks):

    client.patch('/finish/3')

    tasks = Task.query.all()

    ids_of_finished_tasks = [task.id for task in finished_tasks] + [3]

    for task in tasks:
        if task.id in ids_of_finished_tasks:
            assert task.finished
        else:
            assert not task.finished
