class FileWriter:


    def __init__(self, file):
        self.file = file
        self.stream = None

    def __del__(self):
        if self.stream and not self.stream.closed:
            self.stream.flush()
            self.stream.close()

    def write(self, text: str):

        if not self.stream: self._open_file()

        self.stream.write(text)
        self.stream.write("\n")


    def _open_file(self):
        
        try:
            #import os.path
            #if not os.path.exists(self.file):
            #    dir_ = os.path.dirname(self.file)
            #    os.mkdir(dir_)

            self.stream = open(self.file, 'w')
        except Exception as error:
            raise Exception(f"Cannot open file {self.file}. {error}")