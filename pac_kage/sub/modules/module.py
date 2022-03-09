from prefect import task, Flow


@task(log_stdout=True)
def no_name_so_in_docs(x: int, y: int):
    """Task to add two numbers together

    .. note::
    Admonitions work too!

    Parameters
    ----------
    x: int
        The first int
    y: int
        The second int

    Returns
    -------
    int
        Stuff
    """
    print("Hello world")


@task(name="foo bar!")
def not_in_docs(x: int, y: int):
    """Task to add two numbers together

    .. note::
    Admonitions work too!

    Parameters
    ----------
    x: int
        The first int
    y: int
        The second int

    Returns
    -------
    int
        Stuff
    """
    print("Hello world")


@task
def add(x: int, y: int):
    """Task to add two numbers together

    .. note::
    Admonitions work too!

    Parameters
    ----------
    x: int
        The first int
    y: int
        The second int

    Returns
    -------
    int
        Stuff
    """
    print("Hello world")


with Flow(name="foo") as flow:
    add(1, 2)
