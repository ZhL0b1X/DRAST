# DNS_resolver
<img width="513" src="https://user-images.githubusercontent.com/85976942/191089269-0918c8c1-db83-4f67-bfcb-7218697960d6.png">


The purpose of this program is to collect records data for domains that are stored in the DNS server.

The program is currently under development and will have more flexible and convenient functionality in the future.

____

The following functions are currently available:

+ Collect A, AAAA, MX, NS, SOA, TXT, CNAME records;
+ Collect data into .txt file;
+ Add custom DNS IP adress;
+ Location information for type A record





#  Installation process


### [Python3](https://www.python.org/downloads/)  is required for installation.

#### ! Currently being tested only on macOS and Linux operating systems !


To install the program, enter the following commands in the terminal:

```
git clone https://github.com/ADK200/DNS_resolver.git 
```
```
cd DNS_resolver
```
```
pip3 install -r requirements.txt
```



# Usage

### At the moment, the program can only collect data from a bulk list, as well as a single domain. 
To add and edit a bulk list with domains, you need to go into the "Domain_list" directory by entering the following command in the terminal:
```
cd Domain_list
```
Then, using your favorite text editor, change the "dns_domains.txt" file.

For example:
```
vim dns_domains.txt
```
Then you can add the domains each from a new line to the file in the following formats:
```
example.com
www.example.com
https://example.com
```

After you have edited the file, you can launch the program:

```
cd ..
```
```
python3 main.py
```
During operation the program will create a directory called "Output" in which the data files will be saved.
File names are represented as date and time.
```
cd Output
```
# Advice for Advanced
For more advanced interaction with the data, you can go to the "lib" directory<br /> 
and edit the "Domaininfo.py" file by commenting out line 248 and adding the "types" variable to the "return" statement

From this:
```python
types = A, AAAA, MX, TXT, CNAME, NS, SOA
json_object = json.dumps(types, indent = 10)	
return json_object
```
To this:
```python
types = A, AAAA, MX, TXT, CNAME, NS, SOA
#json_object = json.dumps(types, indent = 10)	
return types
```
_______
