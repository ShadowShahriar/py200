def look(fn):
    def wrapper():
        print(f"\nExecuting {fn.__name__}")
        fn()

    return wrapper


@look
def call_tushan():
    print("Oi Tushan")


@look
def call_dolon():
    print("Dolon")


call_dolon()
call_tushan()
