# Rails Partial - Sublime Text 2 Plugin
# Created by Wes Foster (wesf90)
# https://github.com/wesf90/rails-partial

import os
from re import sub
from textwrap import dedent
import sublime, sublime_plugin

def is_rails_view(path):
	return True if ( re.search(r"(?:\\|\/)app(?:\\|\/)views", path) ) else False

class RailsPartialCommand(sublime_plugin.TextCommand):
	edit         = None
	open_partial = False

	def run(self, edit, open_partial = False):
		self.edit         = edit
		self.open_partial = open_partial

		self.view.window().show_input_panel("Partial Name (underscore and extension not needed):","",self.get_selected_text,None,None)


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
		source_ext      = re.sub(r"^[^\.]+", '', os.path.basename(source))
		source_path     = os.path.dirname(source)
		rails_view_path = os.path.dirname(source_path)

		# Default partial vars
		partial_path = None
		partial_sep  = '/'

		# Set the target directory, current, it is the source's path
		target_path = source_path

		# Dummy-proof partial_name -- Remove the prepended underscore and any file extensions
		partial_name = re.sub(r"^_{1}([^\.]+)\..*?$", '\\1', partial_name)

		# Are we wanting the partial in a separate directory?
		if ( re.search(r"\/|\\", partial_name) ):
			# Get the directory names from the partial_name
			m = re.search(r"^(.*)(\\|\/){1}(.*?)$", partial_name)
			partial_path = m.group(1)
			partial_sep  = m.group(2)
			partial_name = m.group(3)

			if is_rails_view(source):
				# If we're a rails view file, change the target path to the base views path
				target_path = rails_view_path + partial_sep + partial_path
			else:
				target_path += partial_sep + partial_path

			# Check if the partial's path exists, if not, create
			if not os.path.exists(target_path):
				os.makedirs(target_path)


		# Set the partial's name
		partial_file_with_path = target_path + partial_sep + '_' + partial_name + source_ext

		# Create the file and paste the data
		if not os.path.exists(partial_file_with_path):
			with open(partial_file_with_path, 'w') as f:
				f.write(textwrap.dedent(partial_code))

			#Open the file?
			if (self.open_partial == True):
				self.view.window().open_file(partial_file_with_path)

			# Insert the render code into the source file and replace the selected text
			if partial_path:
				partial_name = partial_path + '/' + partial_name

			self.insert_render_code(partial_name, source)
		else:
			self.display_message("The partial you were trying to create already exists. To help protect you, we won't let you overwrite that partial. Please delete the partial and everything will be fine!")


	# Insert the render code
	def insert_render_code(self, partial_name, source):
		# Handle different file types
		if source.endswith(".haml"):
			code_replace = "= render '{0}'"
		elif source.endswith( (".erb",".html") ):		# .html added just in case.
			code_replace = "<%= render '{0}' %>"
		elif source.endswith( (".php") ):				# Only basic support, php isn't the real goal as of now. Feel free to expand!
			code_replace = "<?php include('{0}'); ?>"	# :)
		elif source.endswith( (".css") ):
			code_replace = "@import url('{0}');"
 		elif source.endswith( (".scss", ".sass") ):
			code_replace = "@import '{0}';"
		else:
			self.display_message("You're using an unsupported file type! The partial was created, just not 'included' automatically.")

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