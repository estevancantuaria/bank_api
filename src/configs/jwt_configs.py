import os

jwt_infos = {
    "key": os.getenv("KEY"),
    "algorithm": os.getenv("ALGORITHM"),
    "hours": os.getenv("JWT_HOURS")
}