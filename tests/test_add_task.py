import pytest

from todo_list.model import Task


@pytest.mark.parametrize(
    'tasks_to_add',
    [['task1'], ['task1', 'task2'], ['some', 'descriptions', 'of', 'tasks'], []],
)
def test_add_task_post(client, tasks_to_add):

    for task_description in tasks_to_add:
        client.post('/add_task', data={'description': task_description})

    query_tasks = Task.query.all()

    assert {task.description for task in query_tasks} == set(tasks_to_add)


def test_add_task_get(client):

    response = client.get('/add_task')

    assert response.status_code == 200
