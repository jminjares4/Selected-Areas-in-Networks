# **RYU First Application** :dragon:
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

## **Author:**
* [**Jesus Minjares**](https://github.com/jminjares4)<br>
  * Master of Science in Computer Engineering<br>
[![Outlook](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white&style=flat)](mailto:jminjares4@miners.utep.edu) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat)](https://www.linkedin.com/in/jesus-minjares-157a21195/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&style=flat)](https://github.com/jminjares4)