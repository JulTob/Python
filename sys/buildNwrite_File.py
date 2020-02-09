from sys import argv


script, filename = argv

print("Creando el archivo %r"%filename)

file = open(filename,'w')
{

    file.write("Python build file.")

}
file.close()
