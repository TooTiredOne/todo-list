import pytest

from todo_list.model import get_tasks_from_db


def get_descriptions(status, str_filter):
    """
    function for acquiring list of tasks' descriptions

    :param status: str
    :param str_filter: str

    :return: list of str
    """

    return [
        task.description
        for task in get_tasks_from_db(status=status, str_filter=str_filter).all()
    ]


@pytest.mark.usefixtures('client')
def test_get_all_tasks_without_filter(active_tasks, finished_tasks):

    descriptions = get_descriptions(status=None, str_filter=None)

    assert set(descriptions) == {
        task.description for task in active_tasks + finished_tasks
    }


@pytest.mark.usefixtures('client', 'active_tasks', 'finished_tasks')
def test_get_all_tasks_with_matching_filter():

    descriptions = get_descriptions(status=None, str_filter='1')

    assert len(descriptions) == 2
    assert 'task1' in descriptions and 'task10' in descriptions


@pytest.mark.usefixtures('client', 'finished_tasks')
def test_get_active_tasks_without_filter(active_tasks):

    descriptions = get_descriptions(status='active', str_filter=None)

    assert set(descriptions) == {task.description for task in active_tasks}


@pytest.mark.usefixtures('client', 'finished_tasks')
def test_get_active_tasks_with_matching_filter(active_tasks):

    descriptions = get_descriptions(status='active', str_filter=str(active_tasks[0]))

    assert len(descriptions) == 1
    assert descriptions[0] == active_tasks[0].description


@pytest.mark.usefixtures('client', 'active_tasks')
def test_get_finished_tasks_without_filter(finished_tasks):

    descriptions = get_descriptions(status='finished', str_filter=None)

    assert len(descriptions) == len(finished_tasks)

    assert set(descriptions) == {task.description for task in finished_tasks}


@pytest.mark.usefixtures('client', 'active_tasks')
def test_get_finished_tasks_with_matching_filter(finished_tasks):

    descriptions = get_descriptions(
        status='finished', str_filter=str(finished_tasks[0])
    )

    assert len(descriptions) == 1
    assert descriptions[0] == finished_tasks[0].description


@pytest.mark.usefixtures('client', 'active_tasks', 'finished_tasks')
@pytest.mark.parametrize(
    ('status', 'str_filter'), [(None, 'no matches'), ('active', '9'), ('finished', '3')]
)
def test_get_tasks_with_not_matching_filter(status, str_filter):

    descriptions = get_descriptions(status=status, str_filter=str_filter)

    assert not descriptions
