# Standalone

Standalone lets you access Django shell from your Python modules or to run your django module as a standalone module with access to Django shell.


## Installation

    pip install standalone

## Configuration
#### 1. Use Django shell of the current project.

Configuration for accessing the shell of project `mysite` with in a module in same Django project.

```python
# mysite.polls.views.py

import standalone
standalone.run('mysite.settings')

from django.contrib.auth.models import User
User.objects.all() # Users from project mysite
```
#### 2. Use Django shell of another project.

Configuration for accessing the Django shell of a secondary project `mysite2` with in a module in project `mysite`.

Provide settings module of the secondary project along with the abosolute path of the Django project.

```python
# mysite.polls.views.py

import standalone
standalone.run('mysite2.settings', path='/home/user/mysite2/')

from django.contrib.auth.models import User
User.objects.all()  # Users from project mysite2
```

####  Note
> To prevent the code from exeuting while importing the modules, always move your expensive code to the following block.
```python
import standalone
standalone.run('mysite.settings',)

# access django project
from django.contrib.auth.models import User
def get_users():
   return User.objects.all()

if __name__ == '__main__':
    get_users()


```
# License
[Apache License 2.0](LICENSE)
