from flask import request, url_for


def test_index_redirection(client, active_tasks):

    response = client.get('/', follow_redirects=True)

    assert response.status_code == 200
    assert request.path == url_for('listing.list_tasks')

    # checking that todo-list is showing up
    for task in active_tasks:
        assert task.description.encode() in response.data
