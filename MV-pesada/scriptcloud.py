import os
from subprocess import call

os.system("sudo apt update")
os.system("sudo apt install python3-pip")
os.system("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git")
os.chdir("practica_creativa2/bookinfo/src/productpage")
os.system("pip3 install -r requirements.txt")
os.environ['group_number']="17"
os.chdir("templates")

# CAMBIAMOS EL INDEX HTML Y INCLUIMOS LA VAR DE ENTORNO

fin = open("index.html", "r")
fout = open("index2.html", "w")
	
for x in fin:
    if "Simple Bookstore App" in x:
        x = x.replace("Simple Bookstore App", "Simple Bookstore App Group: " + os.environ.get('group_number'))
        fout.write(x)
    elif "three services as shown below" in x:
        x = x.replace("three services as shown below", "three services as shown below Group: " + os.environ.get('group_number'))
        fout.write(x)
    else:
        fout.write(x)
fin.close()
fout.close()

call(["rm", "index.html"])
call(["mv", "index2.html", "index.html"])

# CAMBIAMOS EL PRODUCTPAGE HTML Y INCLUIMOS LA VAR DE ENTORNO

fin = open("productpage.html", "r")
fout = open("productpage2.html", "w")
	
for x in fin:
    if "Simple Bookstore App" in x:
        x = x.replace("Simple Bookstore App", "Simple Bookstore App Group: " + os.environ.get('group_number'))
        fout.write(x)
    elif "three services as shown below" in x:
        x = x.replace("three services as shown below", "three services as shown below Group: " + os.environ.get('group_number'))
        fout.write(x)
    else:
        fout.write(x)
fin.close()
fout.close()

call(["rm", "productpage.html"])
call(["mv", "productpage2.html", "productpage.html"])

os.chdir("..")

os.system("python3 productpage_monolith.py 9080")
