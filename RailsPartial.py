# Rails Partial - Sublime Text 2 Plugin
# Created by Wes Foster (wesf90)

import os, re
import sublime, sublime_plugin

class RailsPartialCommand(sublime_plugin.TextCommand):
	edit         = None
	open_partial = False

	def run(self, edit, open_partial = False):
		self.edit         = edit
		self.open_partial = open_partial

		self.view.window().show_input_panel("Partial Name (underscore and extension not needed):","",self.get_selected_text,None,None)

	def is_enabled(self):
 		return True

	# Get the selected text
	def get_selected_text(self, partial_name):
		for region in self.view.sel():
			if not region.empty():
				partial_code = self.view.substr(region)
			else:
				partial_code = ''

			self.create_partial_file(partial_name, partial_code)



	# Create the file
	def create_partial_file(self, partial_name, partial_code):
		# The source file's path
		source = self.view.file_name()

		# Get the file path and extension
		source_ext	= re.sub(r"^[^\.]+", '', os.path.basename(source))
		target_path = os.path.dirname(source)

		# Dummy-proof partial_name -- Remove the prepended underscore and any file extensions
		partial_name = re.sub(r"^_{1}([^\.]+)\..*?$", '\\1', partial_name)

		# Set the partial's name
		partial_file_with_path = target_path + '/_' + partial_name + source_ext

		# Create the file and paste the data
		if partial_file_with_path:
			with open(partial_file_with_path, 'w') as f:
				f.write(partial_code)

			#Open the file?
			if (self.open_partial == True):
				self.view.window().open_file(partial_file_with_path)

			# Insert the render code into the source file and replace the selected text
			self.insert_render_code(partial_name, source)


	# Insert the render code
	def insert_render_code(self, partial_name, source):
		# Handle different file types
		if source.endswith(".haml"):
			code_replace = "= render '{0}'"
		elif source.endswith( (".erb", ".html") ):
			code_replace = "<%= render '{0}' %>"
		elif source.endswith( (".css", ".scss", ".sass") ):
			code_replace = "@import '{0}'"
		else:
			self.display_message("You're using an unknown file type, so I'm not sure how to write the code to include!")

		# Replace the selected partial text with the appropriate inclusion code
		for region in self.view.sel():
			if region.empty():
				point = region.begin()
				self.view.insert(self.edit, point, code_replace.format(partial_name) )
			else:
				self.view.replace(self.edit, region, code_replace.format(partial_name) )

		self.display_message(partial_name + ' Created Successfully!')


	def display_message(self, value):
	    sublime.active_window().active_view().set_status("rails_partial_msg", value)