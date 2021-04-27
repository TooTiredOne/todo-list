from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    finished = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return str(self.description)


def get_tasks_from_db(status, str_filter):
    """
    function for acquiring tasks from database by given filters

    :param status: str or None
    :param str_filter: str or None
    :return: Task.query object
    """

    tasks = Task.query
    if status:
        is_finished = None
        if status == 'finished':
            is_finished = True
        elif status == 'active':
            is_finished = False

        tasks = Task.query.filter_by(finished=is_finished)

    if str_filter:
        # pylint: disable=no-member
        tasks = tasks.filter(Task.description.contains(str_filter))

    return tasks
