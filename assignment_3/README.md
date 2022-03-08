# Assignment 3 :card_file_box:

* ## Part A

  Capture flow data with pmacct to a CSV file. Write a python script that loads the flow 
  data into a PANDAS dataframe. Create a new dataframe that is a subset of the original 
  data frame using PANDAS to isolate the TCP flows where the number of flow bytes 
  exceeds 100. Submit this python script through Blackboard named lastname_3a.py. 

* ## Part B

  Add four colums to your original PANDAS dataframe from 4) called ‘src_as’, ‘src_org’, 
  ‘dst_as’, ‘dst_org’ using the data in the ‘as.csv’ file. Submit your Python script through 
  Blackboard named lastname_3b.py. 

# Dependencies
In order to read packet in the network, the assignment required to use `pmacctd` and `nfacctd`. Here is the link to install [**pmacct**](https://github.com/pmacct/pmacct).

* Install all dependencies:
- Debian/Ubuntu
  - `apt-get install libpcap-dev pkg-config libtool autoconf automake make bash libstdc++-dev g++`
- CentOS/RHEL
  - `yum install libpcap-devel pkgconfig libtool autoconf automake make bash libstdc++-devel gcc-c++`
* Install software
```bash
 ~# git clone https://github.com/pmacct/pmacct.git
 ~# cd pmacct
 ~#  ./autogen.sh
 ~# ./configure #check-out available configure knobs via ./configure --help
 ~#  make
 ~#  make install #with super-user permission
```
# Software Development
| Software | Enviroment |
| :---:    | :--:       |
| ![Python](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=Python&color=3670A0&logoColor=ffdd54) | ![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=flat&logo=visual%20studio%20code&logoColor=white) |

## Author
* [**Jesus Minjares**](https:/github.com/jminjares4)
  * Master of Science in Computer Engineering