from tgbot.infrastucture.database.models.users import User


def select_user(session, telegram_id):
    user = session.query(User).filter(User.telegram_id == telegram_id).first()
    return user
