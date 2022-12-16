from dataclasses import dataclass
from sqlalchemy.engine import URL

from environs import Env


@dataclass
class DbConfig:  # база данных
    host: str
    password: str
    user: str
    database: str
    port: int

    def construct_sqlalchemy_url(self, library='asyncpg'):
        return str(URL.create(
            drivername=f"postgresql+{library}",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        ))

@dataclass
class TgBot:  # управление ботом
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous
    db: DbConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('POSTGRES_PASSWORD'),
            user=env.str('POSTGRES_USER'),
            database=env.str('POSTGRES_DB'),
            port=env.str('DB_PORT'),
        ),
        misc=Miscellaneous()
    )


banned_users = [123456789, 987654321]

