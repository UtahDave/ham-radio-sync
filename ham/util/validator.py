import logging

from ham.radio.radio_channel import RadioChannel
from ham.util import radio_types
from ham.util.data_column import DataColumn
from ham.util.validation_error import ValidationError


class Validator:
	def __init__(self):
		self._radio_channel_template = RadioChannel.create_empty()
		return

	def validate_radio_channel(self, cols, line, file_name):
		needed_cols_dict_gen = dict(self._radio_channel_template.__dict__)
		return self._validate_generic(cols, line, file_name, needed_cols_dict_gen)

	def _validate_generic(self, cols, line, file_name, needed_cols_dict_gen):
		errors = []
		needed_cols = dict()

		for val in needed_cols_dict_gen.values():
			if not isinstance(val, DataColumn):
				logging.debug(f"Skipping adding `{val}` to needed cols")
				continue
			needed_cols[val.get_alias(radio_types.DEFAULT)] = val

		for key in cols.keys():
			if key not in needed_cols.keys():
				err = ValidationError(f"`{key}` missing from entry.", line, file_name)
				errors.append(err)
				continue
			data_column = needed_cols[key]

			if cols[key] == '':
				continue

			try:
				data_column.shape(cols[key])
			except ValueError as e:
				shape_name = str(data_column.shape).replace("<class '", '').replace("'>", '')
				err = ValidationError(
										f"Error parsing `{cols[key]}` in column `{key}` as `{shape_name}`",
										line,
										file_name
									)
				logging.debug(err.message)
				errors.append(err)
		return errors
