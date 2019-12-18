=================
API Documentation
=================

Main Module
===========
.. automodule:: main
    :members:
    :undoc-members:

Application
===========
.. autoclass:: issueshark.issueshark.IssueSHARK
   :members:

Configuration and Misc
======================

Configuration
-------------
.. autoclass:: issueshark.config.Config
   :members:


Backends
========

BaseBackend
-----------
.. autoclass:: issueshark.backends.basebackend.BaseBackend
   :members:

JiraBackend
-----------

.. autoclass:: issueshark.backends.jirabackend.JiraBackend
   :members:

GithubBackend
-------------

.. autoclass:: issueshark.backends.github.GithubBackend
   :members:

.. autoclass:: issueshark.backends.github.GitHubAPIError
   :members:


BugzillaBackend
---------------

.. autoclass:: issueshark.backends.bugzilla.BugzillaBackend
   :members:

.. autoclass:: issueshark.backends.helpers.bugzillaagent.BugzillaAgent
   :members:

.. autoclass:: issueshark.backends.helpers.bugzillaagent.BugzillaApiException
   :members:
