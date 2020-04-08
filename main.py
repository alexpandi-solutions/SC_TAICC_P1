from src.Test import Executor
from src.Test import Evaluator

fileNames = [   'samples/sample1.txt',
                'samples/sample2.txt',
                'samples/sample3.txt',
                'samples/sample4.txt',
                'samples/sample5.txt',
                'samples/words.txt'   ]

executor = Executor()
evaluator = Evaluator()

for fileName in fileNames:
    executor.setUp(fileName)
    evaluator.run(executor.scenario, executor.file.content)
    print("\n #---------------- RESULTS -----------------")
    print(" # File: " + fileName)
    evaluator.assessWords(executor)
    evaluator.assessNodes(executor)
    evaluator.assessTime()
    evaluator.assessMemory(executor)
    print(" #------------------------------------------ \n")
    executor.file.tearDown()
    executor.tree.tearDown()
    executor.tearDown()
    evaluator.tearDown()