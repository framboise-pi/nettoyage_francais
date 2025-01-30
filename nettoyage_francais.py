#!/usr/bin/env python3
######################
#	nettoyage à la française d'une string XD
#	par LAFONTAINE Cédric Camille
#
#           _        _ _ _             ___     
#  ___ ___ _| |___   | |_| |_ ___ ___  |  _|___ 
# |  _| . | . | -_|  | | | . |  _| -_|_|  _|  _|
# |___|___|___|___|  |_|_|___|_| |___|_|_| |_|  
#
# ASCII art generator: http://patorjk.com/software/taag/
#
import os
import json

class NettoyageFrancais:
		def __init__(self, input_string):
				self.input_string = input_string
				self.grand_remplacement = {
					'e': ['é', 'è', 'ê'],
					'u': ['û', 'ù'],
					'c': ['ç'],
					'-at-': ['@'],
					'': ['©'],#copyright ctrl+shift+u 00a9 entrée
					'-': ["'"],
					'-': ['"'],
					'': [':'],
					'o': ['ô'],
					'': [','],
					'et': ['&'],
					'a': ['à','â'],
					'_': [' ']
				}
				self.grande_suppression = ['(', ')', '[', ']', '/']
				
				# Log file name
				self.log_file = 'nettoyage_francais_log.json'
				
				# Load existing log messages
				self.load_existing_logs()

		def load_existing_logs(self):
				"""Load existing log messages from the JSON file."""
				if os.path.exists(self.log_file):
						with open(self.log_file, 'r', encoding='utf-8') as json_file:
								try:
										self.log_messages = json.load(json_file)
								except json.JSONDecodeError:
										# If JSON is invalid, start with an empty list
										self.log_messages = []
				else:
						self.log_messages = []

		def append_log(self, message):
				"""Append a message to the log file and the in-memory log messages."""
				self.log_messages.append(message)
				with open(self.log_file, 'w', encoding='utf-8') as json_file:
						json.dump(self.log_messages, json_file, ensure_ascii=False, indent=4)

		def nettoyer(self):
				"""Clean and modify the input string according to the defined rules."""
				original_string = self.input_string
				modified_string = original_string.lower()

				# I. le grand remplacement
				for nouvelle_valeur, original_values in self.grand_remplacement.items():
						for original in original_values:
								modified_string = modified_string.replace(original, nouvelle_valeur)
								self.append_log(f"Replacing '{original}' with '{nouvelle_valeur}' in string '{original_string}'")

				# II. la grande suppression
				for char in self.grande_suppression:
						if char in modified_string:
								self.append_log(f"Removing character '{char}' from string '{modified_string}'")
								modified_string = modified_string.replace(char, '')

				# Log the final modified string
				self.append_log(f'Modified string: "{original_string}" to "{modified_string}"')
				return modified_string  # Return the modified string
