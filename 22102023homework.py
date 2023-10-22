import time

def logger(func):
    logs = []
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        call_info = {
            "timestamp": time.ctime(),
            "function_name": func.__name__,
            "args": args,
            "kwargs": kwargs,
            "result": result,
            "execution_time": end_time - start_time
        }
        logs.append(call_info)
        return result

    return wrapped

#-------------#
def get_logs():
    for log in logs:
        yield log

# Приклад використання
@logger
def add(a, b):
    return a + b

@logger
def subtract(a, b):
    return a - b

add(2, 3)
subtract(5, 1)

#-------------#
for log_entry in get_logs():
    print(log_entry)