
def pipeline(depends_on):
    def register_with(func):
        def wrapper_register(*args, **kwargs):
            for extra_step in range(depends_on):
                method_to_call = getattr(extra_step)

                method_to_call()

                return func

        return wrapper_register

    return register_with(depends_on)
