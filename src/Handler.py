class File:
    def __init__(self):
        self.content = [ ]
        self.location = "some location"
        self.wordCount = 0

    def upload(self, address):
        self.location = address

    def extractContent(self):
        with open(self.location,'r') as file:
            for line in file:
                for word in line.split():
                    self.content.append(word)
                    self.wordCount += 1;

    def tearDown(self):
        self.content = [ ]
        self.location = "some location"
        self.wordCount = 0
