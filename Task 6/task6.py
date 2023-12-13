from datetime import datetime
def logger(func):
    logs = []
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()

        log_entry = {
            'time': start_time,
            'function': func.__name__,
            'arguments': args,
            'result': result,
            'execution_time': end_time - start_time
        }
        logs.append(log_entry)
        return result
    return wrapper
def get_logs():
    for log_entry in logs:
        yield log_entry
@logger
def multiply(a, b):
    return a * b
multiply(3, 4)
multiply(5, 6)
log = get_logs()
print(next(log))
print(next(log))