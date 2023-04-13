from fastapi_users.authentication import AuthenticationBackend, CookieTransport, JWTStrategy
import sys
import os

sys.path.append(os.path.join(sys.path[0].replace('/src', '')))

import config as conf

cookie_transport = CookieTransport(cookie_name='study', cookie_max_age=3600)

SECRET = conf.SECRET


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
