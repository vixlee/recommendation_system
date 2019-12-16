from environs import Env

env = Env()
env.read_env()

SECRET_KEY = env(
    "FLASK_SECRET_KEY",
    default="9gjscni6(l0l)1qzs$=ba^*8t=ol+(5wzn6je-uq878(mk1h+=",
)

DEBUG = env.bool("FLASK_DEBUG", False)

SQLALCHEMY_DATABASE_URI = env(
    "DATABASE_URI",
    default="sqlite:///rs_web.developement.db"
)
SQLALCHEMY_TRACK_MODIFICATIONS=False