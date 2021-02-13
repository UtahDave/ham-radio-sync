from ham import radio_types
from ham.data_column import DataColumn


class RadioChannel:
	def __init__(self, cols, digital_contacts):
		self.number = DataColumn(fmt_name='number', fmt_val=cols['number'], shape=int)
		self.number.set_alias(radio_types.BAOFENG, 'Location')
		self.number.set_alias(radio_types.FTM400, 'Channel Number')
		self.number.set_alias(radio_types.D878, 'No.')

		self.name = DataColumn(fmt_name='name', fmt_val=cols['name'], shape=str)
		self.name.set_alias(radio_types.D878, 'Channel Name')

		self.medium_name = DataColumn(fmt_name='medium_name', fmt_val=cols['medium_name'], shape=str)
		self.medium_name.set_alias(radio_types.FTM400, 'Name')

		self.short_name = DataColumn(fmt_name='short_name', fmt_val=cols['short_name'], shape=str)
		self.short_name.set_alias(radio_types.BAOFENG, 'Name')

		self.rx_freq = DataColumn(fmt_name='rx_freq', fmt_val=cols['rx_freq'], shape=float)
		self.rx_freq.set_alias(radio_types.BAOFENG, 'Frequency')
		self.rx_freq.set_alias(radio_types.FTM400, 'Receive Frequency')
		self.rx_freq.set_alias(radio_types.D878, 'Receive Frequency')

		self.rx_ctcss = DataColumn(fmt_name='rx_ctcss', fmt_val=cols['rx_ctcss'], shape=float)
		self.rx_ctcss.set_alias(radio_types.BAOFENG, 'rToneFreq')
		self.rx_ctcss.set_alias(radio_types.FTM400, 'CTCSS')

		self.rx_dcs = DataColumn(fmt_name='rx_dcs', fmt_val=cols['rx_dcs'], shape=float)
		self.rx_dcs.set_alias(radio_types.BAOFENG, 'DtcsCode')
		self.rx_dcs.set_alias(radio_types.FTM400, 'DCS')

		self.rx_dcs_invert = DataColumn(fmt_name='rx_dcs_invert', fmt_val=cols['rx_dcs_invert'], shape=bool)
		self.tx_offset = DataColumn(fmt_name='tx_offset', fmt_val=cols['tx_offset'], shape=float)
		self.tx_offset.set_alias(radio_types.BAOFENG, 'Offset')
		self.tx_offset.set_alias(radio_types.FTM400, 'Offset Frequency')

		self.tx_ctcss = DataColumn(fmt_name='tx_ctcss', fmt_val=cols['tx_ctcss'], shape=float)
		self.tx_ctcss.set_alias(radio_types.BAOFENG, 'cToneFreq')

		self.tx_dcs = DataColumn(fmt_name='tx_dcs', fmt_val=cols['tx_dcs'], shape=float)

		self.tx_dcs_invert = DataColumn(fmt_name='tx_dcs_invert', fmt_val=cols['tx_dcs_invert'], shape=bool)

		self.digital_timeslot = DataColumn(fmt_name='digital_timeslot', fmt_val=cols['digital_timeslot'], shape=int)
		self.digital_timeslot.set_alias(radio_types.D878, 'Slot')

		self.digital_color = DataColumn(fmt_name='digital_color', fmt_val=cols['digital_color'], shape=int)
		self.digital_color.set_alias(radio_types.D878, 'Color Code')

		self.digital_contact = DataColumn(fmt_name='digital_contact_id', fmt_val=cols['digital_contact_id'], shape=int)

		self.tx_power = DataColumn(fmt_name='tx_power', fmt_val=cols['tx_power'], shape=str)
		self.tx_power.set_alias(radio_types.FTM400, 'Tx Power')
		self.tx_power.set_alias(radio_types.D878, 'Transmit Power')

		self.digital_contacts = digital_contacts

	@classmethod
	def make_empty(cls):
		col_vals = dict()
		col_vals['number'] = ''
		col_vals['name'] = ''
		col_vals['medium_name'] = ''
		col_vals['short_name'] = ''
		col_vals['rx_freq'] = ''
		col_vals['rx_ctcss'] = ''
		col_vals['rx_dcs'] = ''
		col_vals['rx_dcs_invert'] = ''
		col_vals['tx_power'] = ''
		col_vals['tx_offset'] = ''
		col_vals['tx_ctcss'] = ''
		col_vals['tx_dcs'] = ''
		col_vals['tx_dcs_invert'] = ''
		col_vals['digital_timeslot'] = ''
		col_vals['digital_color'] = ''
		col_vals['digital_contact_id'] = ''
		return RadioChannel(col_vals, None)

	def headers(self, style):
		switch = {
			radio_types.DEFAULT: self._headers_default,
			radio_types.BAOFENG: self._headers_baofeng,
			radio_types.FTM400: self._headers_ftm400,
			radio_types.D878: self._headers_d878,
		}

		return switch[style]()

	def output(self, style):
		switch = {
			radio_types.DEFAULT: self._output_default,
			radio_types.BAOFENG: self._output_baofeng,
			radio_types.FTM400: self._output_ftm400,
			radio_types.D878: self._output_d878,
		}

		return switch[style]()

	def _headers_default(self):
		output = ''
		output += f"{self.number.get_alias(radio_types.DEFAULT)},"
		output += f"{self.name.get_alias(radio_types.DEFAULT)},"
		output += f"{self.medium_name.get_alias(radio_types.DEFAULT)},"
		output += f"{self.short_name.get_alias(radio_types.DEFAULT)},"
		output += f"{self.tx_power.get_alias(radio_types.DEFAULT)},"
		output += f"{self.rx_freq.get_alias(radio_types.DEFAULT)},"
		output += f"{self.rx_ctcss.get_alias(radio_types.DEFAULT)},"
		output += f"{self.rx_dcs.get_alias(radio_types.DEFAULT)},"
		output += f"{self.rx_dcs_invert.get_alias(radio_types.DEFAULT)},"
		output += f"{self.tx_offset.get_alias(radio_types.DEFAULT)},"
		output += f"{self.tx_ctcss.get_alias(radio_types.DEFAULT)},"
		output += f"{self.tx_dcs.get_alias(radio_types.DEFAULT)},"
		output += f"{self.tx_dcs_invert.get_alias(radio_types.DEFAULT)},"
		output += f"{self.digital_timeslot.get_alias(radio_types.DEFAULT)},"
		output += f"{self.digital_color.get_alias(radio_types.DEFAULT)},"
		output += f"{self.digital_contact.get_alias(radio_types.DEFAULT)},"
		return output

	def _output_default(self):
		output = ''
		output += f"{self.number.fmt_val('')},"
		output += f"{self.name.fmt_val('')},"
		output += f"{self.medium_name.fmt_val('')},"
		output += f"{self.short_name.fmt_val('')},"
		output += f"{self.tx_power.fmt_val('')},"
		output += f"{self.rx_freq.fmt_val('')},"
		output += f"{self.rx_ctcss.fmt_val('')},"
		output += f"{self.rx_dcs.fmt_val('')},"
		output += f"{self.rx_dcs_invert.fmt_val('')},"
		output += f"{self.tx_offset.fmt_val('')},"
		output += f"{self.tx_ctcss.fmt_val('')},"
		output += f"{self.tx_dcs.fmt_val('')},"
		output += f"{self.tx_dcs_invert.fmt_val('')},"
		output += f"{self.digital_timeslot.fmt_val('')},"
		output += f"{self.digital_color.fmt_val('')},"
		output += f"{self.digital_contact.fmt_val('')},"
		return output

	def _headers_baofeng(self):
		output = ''
		output += f"{self.number.get_alias(radio_types.BAOFENG)},"
		output += f"{self.short_name.get_alias(radio_types.BAOFENG)},"
		output += f"{self.rx_freq.get_alias(radio_types.BAOFENG)},"
		output += f"Duplex,"
		output += f"{self.tx_offset.get_alias(radio_types.BAOFENG)},"
		output += f"{'Tone'},"
		output += f"{self.rx_ctcss.get_alias(radio_types.BAOFENG)},"
		output += f"{self.tx_ctcss.get_alias(radio_types.BAOFENG)},"
		output += f"{self.rx_dcs.get_alias(radio_types.BAOFENG)},"
		output += f"DtcsPolarity,"
		output += f"Mode,"
		output += f"TStep,"
		output += f"Skip,"
		output += f"Comment,"
		output += f"URCALL,"
		output += f"RPT1CALL,"
		output += f"RPT2CALL,"
		output += f"DVCODE,"
		return output

	def _output_baofeng(self):
		number = self.number.fmt_val() - 1

		duplex = ''
		if self.tx_offset.fmt_val() is not None:
			if self.tx_offset.fmt_val() < 0:
				duplex = '-'
			else:
				duplex = '+'

		tone = ''
		if self.tx_ctcss.fmt_val() is not None:
			tone = 'Tone'
			if self.rx_ctcss.fmt_val() is not None:
				tone = 'TSQL'
		if self.rx_dcs.fmt_val() != '':
			tone = 'DTCS'

		dtcs_polarity = 'NN'
		if self.rx_dcs_invert.fmt_val() is not None:
			invert_rx = self.rx_dcs_invert.fmt_val()
			if invert_rx:
				dtcs_polarity = 'R' + dtcs_polarity[1]

			invert_tx = self.tx_dcs_invert.fmt_val()
			if invert_tx:
				dtcs_polarity = dtcs_polarity[0] + 'R'

		output = ''
		output += f"{number},"
		output += f"{self.short_name.fmt_val().upper():.7s},"
		output += f"{self.rx_freq.fmt_val():.6f},"
		output += f"{duplex},"
		output += f"{abs(self.tx_offset.fmt_val(0.0)):.6f},"
		output += f"{tone},"
		output += f"{self.rx_ctcss.fmt_val(67.0):.1f},"
		output += f"{self.tx_ctcss.fmt_val(67.0):.1f},"
		output += f"{str(self.rx_dcs.fmt_val(23)).zfill(3)},"
		output += f"{dtcs_polarity},"
		output += f"FM,"
		output += f"{5.0:0.2f},"
		output += f","
		output += f","
		output += f","
		output += f","
		output += f","
		output += f","
		return output

	def _headers_ftm400(self):
		return \
			f"{self.number.get_alias(radio_types.FTM400)},"\
			f"{self.rx_freq.get_alias(radio_types.FTM400)},"\
			f"Transmit Frequency,"\
			f"{self.tx_offset.get_alias(radio_types.FTM400)},"\
			f"Offset Direction,"\
			f"Operating Mode,"\
			f"{self.medium_name.get_alias(radio_types.FTM400)},"\
			f"Show Name,"\
			f"Tone Mode,"\
			f"{self.rx_ctcss.get_alias(radio_types.FTM400)},"\
			f"{self.rx_dcs.get_alias(radio_types.FTM400)},"\
			f"{self.tx_power.get_alias(radio_types.FTM400)},"\
			f"Skip,"\
			f"Step,"\
			f"Clock Shift,"\
			f"Comment,"\
			f"User CTCSS,"

	def _output_ftm400(self):
		tx_freq = self.rx_freq.fmt_val() + self.tx_offset.fmt_val(0)

		tx_units = ''
		tx_offset = ''

		abs_tx_offset = abs(self.tx_offset.fmt_val(0))
		if abs_tx_offset > 0:
			tx_units = ' kHz'  # That whitespace is intentional and important
			tx_offset = f'{abs_tx_offset * 1000:.3f}'
			if abs_tx_offset > 1:
				tx_units = ' mHz'
				tx_offset = f'{abs_tx_offset:3f}'

		offset_direction = ''
		if self.tx_offset.fmt_val() is not None:
			if self.tx_offset.fmt_val() > 0:
				offset_direction = 'Plus'
			else:
				offset_direction = 'Minus'

		tone_mode = 'None'
		if self.tx_ctcss.fmt_val() is not None or self.rx_ctcss.fmt_val() is not None:
			if self.tx_ctcss.fmt_val() is not None:
				tone_mode = 'Tone'
			if self.tx_ctcss.fmt_val() is not None and self.tx_ctcss.fmt_val() is not None:
				tone_mode = 'T Sql'
		if self.rx_dcs.fmt_val() is not None:
			tone_mode = 'DCS'

		output = ''
		output += f"{self.number.fmt_val()},"
		output += f"{self.rx_freq.fmt_val():.5f},"
		output += f"{tx_freq:.5f},"
		output += f"{tx_offset}{tx_units},"
		output += f"{offset_direction},"
		output += f"FM Narrow,"
		output += f"{self.medium_name.fmt_val()},"
		output += f"Large,"
		output += f"{tone_mode},"
		output += f"{self.rx_ctcss.fmt_val('')},"
		output += f"{self.rx_dcs.fmt_val('')},"
		output += f"{self.tx_power.fmt_val('High')},"
		output += f"Off,"
		output += f"Auto,"
		output += f"Off,"
		output += f","
		output += f"300 Hz,"

		return output

	def _headers_d878(self):
		output = ''
		output += f"{self.number.get_alias(radio_types.D878)}," #"No.,"
		output += f"{self.name.get_alias(radio_types.D878)}," #"Channel Name,"
		output += f"{self.rx_freq.get_alias(radio_types.D878)}," #"Receive Frequency,"
		output += f"Transmit Frequency," #"Transmit Frequency,"
		output += f"Channel Type," #"Channel Type,"
		output += f"{self.tx_power.get_alias(radio_types.D878)}," #"Transmit Power,"
		output += f"Band Width," #"Band Width,"
		output += f"CTCSS/DCS Decode," #"CTCSS/DCS Decode,"
		output += f"CTCSS/DCS Encode," #"CTCSS/DCS Encode,"
		output += f"," #"Contact," #todo DMR contacts
		output += f"Contact Call Type," #"Contact Call Type,"
		output += f"," #"Contact TG/DMR ID," #todo DMR contacts
		output += f"Radio ID," #"Radio ID,"
		output += f"Busy Lock/TX Permit," #"Busy Lock/TX Permit,"
		output += f"Squelch Mode," #"Squelch Mode,"
		output += f"Optional Signal," #"Optional Signal,"
		output += f"DTMF ID," #"DTMF ID,"
		output += f"2Tone ID," #"2Tone ID,"
		output += f"5Tone ID," #"5Tone ID,"
		output += f"PTT ID," #"PTT ID,"
		output += f"{self.digital_color.get_alias(radio_types.D878)}," #"Color Code,"
		output += f"{self.digital_timeslot.get_alias(radio_types.D878)}," #"Slot,"
		output += f"Scan List," #"Scan List,"
		output += f"Receive Group List," #"Receive Group List,"
		output += f"PTT Prohibit," #"PTT Prohibit,"
		output += f"Reverse," #"Reverse,"
		output += f"Simplex TDMA," #"Simplex TDMA,"
		output += f"Slot Suit," #"Slot Suit,"
		output += f"AES Digital Encryption," #"AES Digital Encryption,"
		output += f"Digital Encryption," #"Digital Encryption,"
		output += f"Call Confirmation," #"Call Confirmation,"
		output += f"," #"Talk Around(Simplex)," #todo dmr talkaround
		output += f"Work Alone," #"Work Alone,"
		output += f"Custom CTCSS," #"Custom CTCSS,"
		output += f"2TONE Decode," #"2TONE Decode,"
		output += f"Ranging," #"Ranging,"
		output += f"Through Mode," #"Through Mode,"
		output += f"Digi APRS RX," #"Digi APRS RX,"
		output += f"Analog APRS PTT Mode," #"Analog APRS PTT Mode,"
		output += f"Digital APRS PTT Mode," #"Digital APRS PTT Mode,"
		output += f"APRS Report Type," #"APRS Report Type,"
		output += f"Digital APRS Report Channel," #"Digital APRS Report Channel,"
		output += f"Correct Frequency[Hz]," #"Correct Frequency[Hz],"
		output += f"SMS Confirmation," #"SMS Confirmation,"
		output += f"Exclude channel from roaming," #"Exclude channel from roaming,"
		output += f"DMR MODE," #"DMR MODE,"
		output += f"DataACK Disable," #"DataACK Disable,"
		output += f"R5toneBot," #"R5toneBot,"
		output += f"R5ToneEot," #"R5ToneEot,"
		return output

	def _output_d878(self):
		tx_frequency = self.rx_freq.fmt_val() + self.tx_offset.fmt_val(0)

		channel_type = 'A-Analog'
		busy_lock = 'Off'
		dmr_mode = 0
		if self.digital_timeslot.fmt_val() is not None:
			channel_type = 'D-Digital'
			busy_lock = 'Always'
			dmr_mode = 1

		ctcs_dcs_decode = 'Off'
		if self.rx_ctcss.fmt_val() is not None or self.rx_dcs.fmt_val() is not None:
			if self.rx_ctcss.fmt_val() is not None:
				ctcs_dcs_decode = f"{self.rx_ctcss.fmt_val():.1f}"
			if self.rx_dcs.fmt_val() is not None:
				polarity = 'N'
				if self.rx_dcs_invert.fmt_val(False):
					polarity = 'I'
				ctcs_dcs_decode = f"D{str(self.rx_dcs.fmt_val()).zfill(3)}{polarity}"

		ctcs_dcs_encode = 'Off'
		if self.tx_ctcss.fmt_val() is not None or self.tx_dcs.fmt_val() is not None:
			if self.tx_ctcss.fmt_val() is not None:
				ctcs_dcs_encode = f"{self.tx_ctcss.fmt_val():.1f}"
			if self.tx_dcs.fmt_val() is not None:
				polarity = 'N'
				if self.tx_dcs_invert.fmt_val(False):
					polarity = 'I'
				ctcs_dcs_encode = f"D{str(self.tx_dcs.fmt_val()).zfill(3)}{polarity}"

		output = ''
		output += f"{self.number.fmt_val()},"  # "No.,"
		output += f"{self.name.fmt_val():.16s},"  # "Channel Name,"
		output += f"{self.rx_freq.fmt_val():.5f},"  # "Receive Frequency,"
		output += f"{tx_frequency},"  # "Transmit Frequency,"
		output += f"{channel_type},"  # "Channel Type,"
		output += f"{self.tx_power.fmt_val()},"  # "Transmit Power,"
		output += f"12.5K,"  # "Band Width,"
		output += f"{ctcs_dcs_decode},"  # "CTCSS/DCS Decode,"
		output += f"{ctcs_dcs_encode},"  # "CTCSS/DCS Encode,"
		output += f","  # "Contact," #todo DMR contacts
		output += f","  # "Contact Call Type," #todo DMR contacts
		output += f","  # "Contact TG/DMR ID," #todo DMR contacts
		output += f"DMR,"  # "Radio ID,"
		output += f"{busy_lock},"  # "Busy Lock/TX Permit,"
		output += f"Carrier,"  # "Squelch Mode,"
		output += f"Off,"  # "Optional Signal,"
		output += f"1,"  # "DTMF ID,"
		output += f"1,"  # "2Tone ID,"
		output += f"1,"  # "5Tone ID,"
		output += f"Off,"  # "PTT ID,"
		output += f"{self.digital_color.fmt_val('')},"  # "Color Code,"
		output += f"{self.digital_timeslot.fmt_val('')},"  # "Slot,"
		output += f"None,"  # "Scan List,"
		output += f"None,"  # "Receive Group List,"
		output += f"{busy_lock},"  # "PTT Prohibit,"
		output += f"Off,"  # "Reverse,"
		output += f"Off,"  # "Simplex TDMA,"
		output += f"Off,"  # "Slot Suit,"
		output += f"Normal Encryption,"  # "AES Digital Encryption,"
		output += f"Off,"  # "Digital Encryption,"
		output += f"Off,"  # "Call Confirmation,"
		output += f","  # "Talk Around(Simplex)," #todo DMR talkaround
		output += f"Off,"  # "Work Alone,"
		output += f"251.1,"  # "Custom CTCSS,"
		output += f"0,"  # "2TONE Decode,"
		output += f"Off,"  # "Ranging,"
		output += f"Off,"  # "Through Mode,"
		output += f"Off,"  # "Digi APRS RX,"
		output += f"Off,"  # "Analog APRS PTT Mode,"
		output += f"Off,"  # "Digital APRS PTT Mode,"
		output += f"Off,"  # "APRS Report Type,"
		output += f"1,"  # "Digital APRS Report Channel,"
		output += f"0,"  # "Correct Frequency[Hz],"
		output += f"Off,"  # "SMS Confirmation,"
		output += f"0,"  # "Exclude channel from roaming,"
		output += f"{dmr_mode},"  # "DMR MODE,"
		output += f"0,"  # "DataACK Disable,"
		output += f"0,"  # "R5toneBot,"
		output += f"0,"  # "R5ToneEot,"
		return output
