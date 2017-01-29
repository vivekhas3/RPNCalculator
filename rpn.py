class Queue(object):
	def __init__(self):
		self.data = []
	def push(self, item):
		self.data.append(item)
	def pop(self):
		return self.data.pop(-1)

class FloatFormatter(object):
	def format(self, number):
		return float("%.1f"%float(number))

FORMATTERS = {'float':FloatFormatter}

class PercentFactory(object):
	def calculate(self, item):
		return float(item)/100.0

class FactorialFactory(object):
	def calculate(self, item):
		if item == 1:
			return item
		return int(item)*self.calculate(int(item)-1)


UNARY_FACTORY = {'%':PercentFactory, '!':FactorialFactory}

class RPNCalculator(object):
	def __init__(self):
		self.queue = Queue()
		self.__allowed_operators = ['+', '-', '*', '/']
		self._VALIDATION_MESSAGE = {'empty':"Please enter some value",
									'error':"Error"
									}

	def __is_operator(self, item):
		return True if item in self.__allowed_operators else False

	def __is_operand(self, item):
		try:
		   val = float(item)
		except ValueError:
		   return False
		return True


	def __is_valid(self, expression):
		if expression == '':
			return self._VALIDATION_MESSAGE['empty']

	def __format_output(self, output, format='float'):
		return FORMATTERS[format]().format(output)
		
	def __is_unary_operator(self, item):
		return True if item in UNARY_FACTORY.keys() else False

	def evaluate(self, expression, separator=','):

		validity = self.__is_valid(expression)
		if validity:
			return validity

		for item in expression.split(separator):
			if self.__is_operator(item):
				try:
					item2 = self.queue.pop()
					item1 = self.queue.pop()
					result = eval(item1 + item + item2)
					self.queue.push(str(result))
				except IndexError:
					return self._VALIDATION_MESSAGE['error']
			elif self.__is_unary_operator(item):
				try:
					item1 = self.queue.pop()
					result = UNARY_FACTORY[item]().calculate(item1)
					self.queue.push(str(result))
				except IndexError:
					return self._VALIDATION_MESSAGE['error']
			elif self.__is_operand(item):
				self.queue.push(str(float(item)))

		if(len(self.queue.data) == 1 and self.__is_operand(self.queue.data[-1])):
			return self.__format_output(self.queue.pop())
		if(len(self.queue.data) != 0):
			return self._VALIDATION_MESSAGE['error']
		return self._VALIDATION_MESSAGE['empty']