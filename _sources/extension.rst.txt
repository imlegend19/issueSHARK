How to Extend
=============
**issueSHARK** can be extended by adding new backends from which issues can be collected.

All backends are stored in the issueshark/backends folder. There are conditions, which must be fulfilled by the
backends so that it is accepted by the **issueSHARK**:

1. The \*.py file for this backend must be stored in the issueshark/backends folder.
2. It must inherit from :class:`~issueshark.backends.basebackend.BaseBackend`
and implement the methods defined there.

The process of chosing the backend is the following:

*	Every backend gets instantiated

*	If the by the user choosen backend identifier matches the :func:`~issueshark.backends.basebackend.BaseBacken.identifier` it is chosen

There are several important things to note:

1.	If you want to use a logger for your implementation, get it via

	.. code-block:: python

		logger = logging.getLogger("backend")


2.	The execution logic is in the application class and explained here :class:`~issueshark.issueshark.IssueSHARK`.

3. If you want to have an example how to implement this class, look in the issueshark/backends folder.

    .. WARNING:: Take care that you save the **original** state of the issue, like it is explained in the introduction.
