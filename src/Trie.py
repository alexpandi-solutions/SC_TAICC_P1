from functools import reduce
import sys

class Tree:
	def __init__(self):
		self.root = { }

	def insertKey(self, key):
		count = 0
		node = self.root
		for item in key:
			if item not in node:
				node[item] = { }
				count += 1
			node = node[item]
		node['@'] = True
		count += 1
		return count

	def isEnlisted(self, key):
		node = self.root
		for item in key:
			if item not in node:
				return False
			node = node[item]
		if '@' in node:
			return True
		else:
			return False

	def getSize(self):
		result = 0
		flattenedSeries = self.__flatten(self.root)
		convertedSeries = self.__modelKeysList(flattenedSeries)
		result = sys.getsizeof(convertedSeries)
		return result
	
	def tearDown(self):
		root = { }
	
	def __flatten(self, startNode, separator = '_', prefix = ''):
		return {
			prefix + separator + key if prefix else key : value
			for keys, values in startNode.items()
			for key, value in self.__flatten(values, separator, keys).items()
		} if isinstance(startNode, dict) else { prefix : startNode}

	def __splitKey(self, key, separator = '_'):
		result = [ ]
		for item in key.split(separator):
			result.append(item)
		return result

	def __modelKeysList(self, startNode):
		result = [ ]
		for key in startNode.keys():
			for item in self.__splitKey(key):
				result.append(item)
		return result

	def __normalizeList(self, container):
		result = list(filter(('@').__ne__, container))
		return result