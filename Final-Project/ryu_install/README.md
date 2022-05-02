# **RYU Installation Setup** :dragon:

The installation for RYU Network Operating System (NOS) is straightforward.
I will be listing the most popular ones.

# **Prerequisites**
```bash
# must be run as super-user
apt install gcc python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev zlib1g-dev 
```

# **Quick Setup**
I have developed a script to install all the dependencies and RYU. The script will install RYU from source. Here is the set to install RYU.
```bash
chmod +x ryu_install/install.sh
./install.sh 
```

# **Installation Guideline**
1. Install with pip
```bash
pip install ryu
```
2. Install from source
```bash
git clone https://github.com/faucetsdn/ryu.git
cd ryu; pip install .   
```
The final step is the install the optional dependencies for application that require:
 * OF-Config 
 * NETCONF
 * BGP speaker (SSH console) 
 * Zebra protocol service (database)     
```bash
# RYU must be install from source
pip install -r tools/optional-requires
```

## **Author:**
* [**Jesus Minjares**](https://github.com/jminjares4)<br>
  * Master of Science in Computer Engineering<br>
[![Outlook](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white&style=flat)](mailto:jminjares4@miners.utep.edu) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat)](https://www.linkedin.com/in/jesus-minjares-157a21195/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&style=flat)](https://github.com/jminjares4)