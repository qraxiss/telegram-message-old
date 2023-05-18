def handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            response = {"message": "success", "data": result}
            status_code = 200
        except Exception as e:
            response = {"error": {"message": str(e), "type": type(e).__name__}}
            status_code = getattr(e, "status", 500)
        return response, status_code
    return wrapper
