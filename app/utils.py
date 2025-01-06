from datetime import datetime


api_version = "1.0.0"

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
