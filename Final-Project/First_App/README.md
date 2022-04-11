# **RYU First Application**
Ryu applications are just python scripts. Therefore, they are easy to developed and test with the ability of reconfiguration.

## **How to run RYU-Applications**
As previously mention, Ryu applications are python scripts. However, inorder to run application `ryu-manager`.
```bash
ryu-manager filename.py

```

## *Dummpy Application*
```.py
# Dummy application to demostrate ryu-applications
from ryu.base import app_manager

class L2Switch(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)

```
## *Output*
Excepted output:
```bash
loading app {filename}.py
instantiating app {filename.py} of L2Switch
```
