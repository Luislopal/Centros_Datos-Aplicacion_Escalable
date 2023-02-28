import os
from subprocess import call
group_number = str(os.getenv("GROUP_NUMBER"))

# CAMBIAMOS EL INDEX HTML Y INCLUIMOS LA VAR DE ENTORNO

fin = open("index.html", "r")
fout = open("index2.html", "w")
	
for x in fin:
    if "Simple Bookstore App" in x:
        x = x.replace("Simple Bookstore App", "Simple Bookstore App Group: " + str(group_number))
        fout.write(x)
    elif "three services as shown below" in x:
        x = x.replace("three services as shown below", "three services as shown below Group: " + str(group_number))
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
        x = x.replace("Simple Bookstore App", "Simple Bookstore App Group: " + str(group_number))
        fout.write(x)
    elif "three services as shown below" in x:
        x = x.replace("three services as shown below", "three services as shown below Group: " + str(group_number))
        fout.write(x)
    else:
        fout.write(x)
fin.close()
fout.close()

call(["rm", "productpage.html"])
call(["mv", "productpage2.html", "productpage.html"])