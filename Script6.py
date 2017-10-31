import datetime
r"""
This Script creates an empty file.
"""
fileName =datetime.datetime.now()

#Create empty file
def create_file():
    """This function creates an empty file"""
    with open(fileName.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
        file.write("")

create_file()
