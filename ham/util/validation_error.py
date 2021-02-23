
class ValidationError(Exception):
	def __init__(self, message, line, file_name):
		self.message = message
		self.line = line
		self.file_name = file_name
		return
