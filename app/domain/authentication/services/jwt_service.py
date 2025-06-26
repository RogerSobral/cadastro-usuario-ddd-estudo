import jwt
from datetime import datetime,UTC,timedelta

import os

SECRET_KEY = os.environ.get("JWT_SECRET", "fallback_inseguro_somente_para_dev")

def generate_token(user, expires_in_hours=1):
    if SECRET_KEY == "fallback_inseguro_somente_para_dev":
        raise ValueError("Não há Key secret")
    
    payload = {
        "sub": str(user.id),
        "email": user.email,
        "exp": datetime.now(UTC)+ timedelta(hours=expires_in_hours)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token
