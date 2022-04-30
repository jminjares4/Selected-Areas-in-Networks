# Assignment 4 :computer:

Create a network that consists of 2 subnets joined by switch. Each subnet will have a total of 2 hosts
and these hosts will be connected to the same switch, which will interact with the hosts by using Layer 2
protocols. Both subnet's switches will be connected to a third switch, which will use Layer 3 protocol. 
The task is to be able to ping all of the hosts and test the bandwidth of each of the host pairs successfully.

# Dependencies

Install [Mininet](http://mininet.org/download/)
- From source
```bash
git clone https://github.com/mininet/mininet
cd mininet
git tag  # list available versions
git checkout -b mininet-2.3.0 2.3.0  # or whatever version you wish to install
cd ..
mininet/util/install.sh 
```
- Verify mininet is properly installed
  - `sudo mn --switch ovsbr --test pingall`

# Software Development
| Software | Enviroment |
| :---:    | :--:       |
| ![Python](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=Python&color=3670A0&logoColor=ffdd54) | ![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=flat&logo=visual%20studio%20code&logoColor=white) |

## Author:
* [**Jesus Minjares**](https://github.com/jminjares4)<br>
  * Master of Science in Computer Engineering<br>
[![Outlook](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white&style=flat)](mailto:jminjares4@miners.utep.edu) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat)](https://www.linkedin.com/in/jesus-minjares-157a21195/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&style=flat)](https://github.com/jminjares4)