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
		self.number.set_alias(radio_types.D878, 'No.')

		self.radio_id = DataColumn(fmt_name='digital_id', fmt_val=cols['digital_id'], shape=int)
		self.radio_id.set_alias(radio_types.D878, 'Radio ID')

		self.name = DataColumn(fmt_name='name', fmt_val=cols['name'], shape=str)
		self.name.set_alias(radio_types.D878, 'Name')

		self.call_type = DataColumn(fmt_name='call_type', fmt_val=cols['call_type'], shape=str)
		self.call_type.set_alias(radio_types.D878, 'Call Type')
		return

	def headers(self, style):
		switch = {
			radio_types.DEFAULT: self._headers_default,
			radio_types.D878: self._headers_d878,
		}

		return switch[style]()

	def output(self, style):
		switch = {
			radio_types.DEFAULT: self._output_default,
			radio_types.D878: self._output_d878,
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

	def _headers_d878(self):
		output = ''
		output += f"{self.number.get_alias(radio_types.D878)},"
		output += f"{self.radio_id.get_alias(radio_types.D878)},"
		output += f"{self.name.get_alias(radio_types.D878)},"
		output += f"{self.call_type.get_alias(radio_types.D878)},"
		output += f"Call Alert,"
		return output

	def _output_d878(self):
		call_type = 'All Call'
		if self.call_type.fmt_val() == 'group':
			call_type = 'Group Call'

		output = ''
		output += f"{self.number.fmt_val()},"
		output += f"{self.radio_id.fmt_val()},"
		output += f"{self.name.fmt_val()},"
		output += f"{call_type},"
		output += f"None,"
		return output

