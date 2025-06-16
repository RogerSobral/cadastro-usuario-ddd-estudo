import jwt
import datetime

import os

SECRET_KEY = os.environ.get("JWT_SECRET", "fallback_inseguro_somente_para_dev")

def generate_token(user, expires_in_hours=1):
    payload = {
        "sub": str(user.id),
        "email": user.email.value,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=expires_in_hours)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token
