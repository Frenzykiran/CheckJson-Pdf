class FileManager:

    def _init_(self):
        pass

    def sendFiles(self, files):
        if len(files) > 2:
            raise Exception('Only 2 files can be sent')

        if self.__can_send(files):
            # write code to send file
            print('Files sent successfully')
            return
        else:
            raise Exception('1 pdf and 1 json file must be sent')
        
    def __can_send(self, files):
        extensions = [file.split('.')[-1] for file in files]
        if 'pdf' in extensions and 'json' in extensions:
            return True
        else:
            return False
        

if __name__ == '_main_':

    fm = FileManager()

    fm.sendFiles(['/home/user/test1.pdf', '/home/user/test1.json'])
    fm.sendFiles(['/home/user/test1.pdf', '/home/user/test1.pdf'])
    fm.sendFiles(['/home/user/test1.json', '/home/user/test1.pdf', '/home/user/test1.pdf'])