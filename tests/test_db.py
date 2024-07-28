from sqlalchemy import select

from learning_fastapi.models import Todo, User


def test_create_user(session):
    new_user = User(
        username='lara', password='secret', email='lara@example.com'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'lara'))

    assert user.username == 'lara'


def test_create_todo(session, user: User):
    todo = Todo(
        title='Test Todo',
        description='Test Desc',
        state='draft',
        user_id=user.id,
    )

    session.add(todo)
    session.commit()
    session.refresh(todo)

    user = session.scalar(select(User).where(User.id == user.id))

    assert todo in user.todos
