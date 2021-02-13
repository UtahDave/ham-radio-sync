from ham.data_column import DataColumn

from ham import radio_types


class DmrContact:
	@classmethod
	def create_empty(cls):
		cols = dict()
		cols['number'] = ''
		cols['digital_id'] = ''
		cols['name'] = ''
		cols['call_type'] = ''
		return DmrContact(cols)

	def __init__(self, cols):
		self.number = DataColumn(fmt_name='number', fmt_val=cols['number'], shape=int)
		self.radio_id = DataColumn(fmt_name='digital_id', fmt_val=cols['digital_id'], shape=int)
		self.name = DataColumn(fmt_name='name', fmt_val=cols['name'], shape=str)
		self.call_type = DataColumn(fmt_name='call_type', fmt_val=cols['call_type'], shape=str)
		return

	def headers(self, style):
		switch = {
			radio_types.DEFAULT: self._headers_default,
		}

		return switch[style]()

	def output(self, style):
		switch = {
			radio_types.DEFAULT: self._output_default,
		}

		return switch[style]()

	def _headers_default(self):
		output = ''
		output += f"{self.number.get_alias(radio_types.DEFAULT)},"
		output += f"{self.radio_id.get_alias(radio_types.DEFAULT)},"
		output += f"{self.name.get_alias(radio_types.DEFAULT)},"
		output += f"{self.call_type.get_alias(radio_types.DEFAULT)},"
		return output

	def _output_default(self):
		output = ''
		output += f"{self.number.fmt_val()},"
		output += f"{self.radio_id.fmt_val()},"
		output += f"{self.name.fmt_val()},"
		output += f"{self.call_type.fmt_val()},"
		return output

