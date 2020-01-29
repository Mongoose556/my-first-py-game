file_ext=(input("enter file extension, no dot (txt, py, etc): "))
file_name=(input("enter file name: "))

if file_name.isalnum() and file_ext.isalnum():
    f= open(file_name+"."+file_ext, "w+")
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
    f.close()
else:
    print("file name/extension must be alphanumeric! Not: " + file_name)

