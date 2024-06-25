from sqlalchemy import select

from learning_fastapi.models import User


def test_create_user(session):
    new_user = User(
        username='lara', password='secret', email='lara@example.com'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'lara'))

    assert user.username == 'lara'
