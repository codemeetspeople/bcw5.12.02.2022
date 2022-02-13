def run_N_times(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@run_N_times(2)
def hello(username):
    print(f'Hello, {username}!')


@run_N_times(2)
def hello2(username1, username2):
    print(f'Hello, {username1} and {username2}!')


if __name__ == '__main__':  # pragma: no cover
    hello2('caiman', 'saruman')
