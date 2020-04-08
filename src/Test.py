from src.Handler import File
from src.Trie import Tree
import time

class Executor:
    def __init__(self):
        self.tree = Tree()
        self.file = File()
        self.nodeCount = 0

    def setUp(self, fileName):
        self.file.upload(fileName)
        self.file.extractContent()

    def scenario(self, content):
        for word in content:
            self.nodeCount += self.tree.insertKey(word)

    def tearDown(self):
        self.tree = Tree()
        self.file = File()
        self.nodeCount = 0

class Evaluator:
    def __init__(self):
        self.elapsedTime = " "

    def run(self, task, content):
        start = time.perf_counter()
        task(content)
        stop = time.perf_counter()
        self.elapsedTime = str(stop - start)

    def assessWords(self, executor):
        print(" # Number of uploaded words: " + str(executor.file.wordCount))

    def assessTime(self):
        print(" # Seconds elapsed: " + self.elapsedTime)

    def assessNodes(self, executor):
        print(" # Number of nodes: " + str(executor.nodeCount))

    def assessMemory(self, executor):
        print(" # Memory footprint in bits: " + str(executor.tree.getSize()))

    def tearDown(self):
        self.elapsedTime = " "