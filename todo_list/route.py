from flask import Blueprint, redirect, render_template, request, url_for

from todo_list.model import Task, db, get_tasks_from_db

bp = Blueprint('listing', __name__)


@bp.route('/')
def index():
    """
    redirecting to /tasks
    """

    return redirect(url_for('listing.list_tasks', status='active', filter=None))


@bp.route('/tasks')
def list_tasks():
    """
    showing todo-list by applying corresponding filters
    """

    # filtering
    status = request.args.get('status')
    str_filter = request.args.get('filter')
    tasks = get_tasks_from_db(status, str_filter)

    # pagination
    page = request.args.get('page', 1, type=int)
    tasks = tasks.paginate(page=page, per_page=10)

    return render_template(
        'tasks.html', tasks=tasks, status=status, filter=str_filter, page=page
    )


@bp.route('/add_task', methods=['GET', 'POST'])
def add_task():
    """
    adding task to database
    """

    if request.method == 'POST':
        # create task
        description = request.form.get('description')
        if description:
            task = Task(description=description)
            # commit changes
            db.session.add(task)
            db.session.commit()

    return render_template('add_task.html')


@bp.route('/finish/<int:task_id>', methods=['POST', 'PATCH'])
def finish_task(task_id: int):
    """
    marking task as finished

    :param task_id:
    :return:
    """

    # get task
    task = Task.query.get_or_404(task_id)
    task.finished = True

    # commit changes
    db.session.add(task)
    db.session.commit()

    return redirect(request.referrer)
