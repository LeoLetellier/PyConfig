# Docstrings

Dosctrings are essential in Python since its the way to describe what your functions do, how they do it, and what are the parameters involved. It helps to convey the purpose of the described code and allows external contributors and users to easily understand what's happening under the hood.

Documentation can be added to a function, a class, and to the whole file (top of document).

They are several dosctrings formats, the most common being reStructuredText, Numpy and Google.

## ReStructured Text

RST is a versatile plaintext markup language used by Docutils and Sphinx (see [Sphinx page](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html), [writing docstrings](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)).

````python
"""[Summary]

:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
"""
````

## Numpy / Scipy Docstrings

````python
def my_function():
    """Brief description of the function

    More detailled description

    Parameters
    ----------
    x : type
        Description of parameter `x`.
    y
        Description of parameter `y` (with type not specified).

    Returns
    -------
    int
        Description of anonymous integer return value.

    Raises
    ------
    LinAlgException
        If the matrix is not numerically invertible.
    """
````

Other rubrics exist, like: See Also, Notes, Examples...

For the class: Attributes, Methods...

## Google Docstrings

````python
def my_function():
    """Brief description

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.

    Raises:
      ConnectionError: If no available port is found.
    """
````

## With Mkdocstrings

Close to the Google dosctrings, in plain MarkDown, example from [mkdocstring github](https://github.com/mkdocstrings/mkdocstrings/blob/main/src/mkdocstrings/loggers.py).

````python
"""Log a message.

Arguments:
    context: The template context, automatically provided by Jinja.
    msg: The message to log.
    **kwargs: Additional arguments passed to the logger function.

Returns:
    An empty string.
""""
````

## Documentation Generation

The dosctrings can be extracted to generate a complete documentation book. One of the most famous system on this topic is [Doxygen](https://www.doxygen.nl/), which works well for languages such as C++, but is less integrated for Python.

For that reason, I will present here:

* [Sphinx](./sphinx.md)
* [Mkdocs](./mkdocs.md)