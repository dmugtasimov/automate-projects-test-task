Local development environment setup
===================================

This section describes how to setup development environment for Linux Mint 18.3.

Initial setup
-------------
Once initial setup is done only corresponding `Update`_ section should be performed
to get the latest version for development.

#. Install PyCharm to use as IDE
#. Install prerequisites::

    apt update
    apt install git

#. [if you have not configured it globally] Configure git::

    git config user.name 'Firstname Lastname'
    git config user.email 'youremail@youremail_domain.com'

#. Install prerequisites (
   as prescribed at https://github.com/pyenv/pyenv/wiki/Common-build-problems )::

    apt update &&
    apt install make build-essential libssl-dev zlib1g-dev libbz2-dev \
                libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
                libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

#. Install and configure `pyenv` according to https://github.com/pyenv/pyenv#basic-github-checkout
#. Install Python 3.9.1::

    pyenv install 3.9.1

#. Clone the repo::

    git clone git@github.com:dmugtasimov/automate-projects-test-task.git

#. Setup development environment::

    # Ensure you are in `automate-projects-test-task` repo root directory
    make dev-env-setup

Run
---

#. Run script::

    poetry python -m automate_projects_test_task.console
