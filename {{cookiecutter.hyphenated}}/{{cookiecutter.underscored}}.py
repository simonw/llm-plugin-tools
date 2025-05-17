import llm


def {{ cookiecutter.function_name }}(input: str) -> str:
    """
    Description of tool goes here.
    """
    return f"hello {input}"


@llm.hookimpl
def register_tools(register):
    register({{ cookiecutter.function_name }})
