import os
from datetime import datetime
from contextlib import contextmanager
from flask_sqlalchemy import event
import jwt
from freezegun import freeze_time

from db.shared import db

SYSTEM_TIME = "Thu, 31 Mar 2022 19:19:35 GMT"


def make_token(user_id):
    jwt.encode({"id": user_id}, os.environ.get("SESSION_SECRET"), algorithm="HS256")


@contextmanager
def patch_time(time_to_freeze):
    with freeze_time(time_to_freeze, tick=False) as frozen_time:

        def set_timestamp(mapper, connection, target):
            now = datetime.now()
            if hasattr(target, "created_on"):
                target.created_on = now
            if hasattr(target, "updated_on"):
                target.updated_on = now

        event.listen(db.Model, "before_insert", set_timestamp, propagate=True)
        yield frozen_time
        event.remove(db.Model, "before_insert", set_timestamp)
