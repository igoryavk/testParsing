from bs4 import BeautifulSoup as Soup
class XmlDestroyer:
    def __init__(self,path):
        self.__path=path
        with open(self.__path,"r",encoding="utf-8") as file:
            content=file.read()
        self.__document=Soup(content,"xml")
        self.__project=self.__document.project
        self.__tag_pous=self.__project.types.pous
        self.__list_pous=[pou for pou in self.__project.types.pous.children if pou.name is not None]
    def printTypes(self):
        print(f"The document has a type {type(self.__document)} and name {self.__document.name}")
        print(f"The project has a type {type(self.__project)}")
        print(f"The pous has a type {type(self.__list_pous)}")
    def clearPous(self):
        with open("D://export//pous.xml","w") as output:
            output.write(str(self.__tag_pous))
            output.flush()
            output.close()
        self.__tag_pous.decompose()
        with open("D://export//clear.xml","w") as clear:
            clear.write(str(self.__document))
            clear.flush()
            clear.close()
        # print(str(self.__tag_pous))
    def showNewTree(self):
        with open("D://export//pous.xml","r") as file:
            saved=file.read()
        self.__saved_document=Soup(saved,"xml")
        with open("D://export//clear.xml","r") as clear_tree:
            clear=clear_tree.read()
        self.__output_document=Soup(clear,"xml")
        pous=self.__saved_document.pous
        self.__output_document.project.types.append(pous)
        with open("D://export//output.xml","w",encoding="utf-8") as output:
            output.write(str(self.__output_document).encode().decode("utf-8"))
            output.flush()
            output.close()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    destroyer=XmlDestroyer("D://export//export.xml")
    destroyer.clearPous()
    destroyer.showNewTree()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
