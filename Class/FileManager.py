class fileManager():

    def writeOnFile(self,fileName,Text):
        try:
            #fileName = "/Users/michelealloggio/PycharmProjects/FlyPooling/"+ fileName
            file= open(fileName, "a+")
            file.write(Text)
            file.close()
        except Error as e:
            print (e)
