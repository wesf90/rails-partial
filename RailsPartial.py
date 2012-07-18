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
		target_path     = os.path.dirname(source)
		rails_view_path = os.path.dirname(target_path)


		# Dummy-proof partial_name -- Remove the prepended underscore and any file extensions
		partial_name = re.sub(r"^_{1}([^\.]+)\..*?$", '\\1', partial_name)

		
		# Are we wanting the partial in a separate directory?
		if ( re.search(r"\/|\\", partial_name) ):
			if is_rails_view(source):
				# If we're a rails view file, change the target path to the base views path
				target_path = rails_view_path

			# Check if the partial's path exists, if not, create
			partial_path = os.path.dirname(target_path + '/' + partial_name)
			if not os.path.exists(partial_path):
				os.makedirs(partial_path)

			# Prepend the underscore after the manually-entered dir
			partial_name = re.sub(r"^(.*)(\\|\/){1}(.*?)$", '\\1\\2_\\3', partial_name)
		else:
			# Prepend the underscore
			partial_name = '_' + partial_name


		# Set the partial's name
		partial_file_with_path = target_path + '/' + partial_name + source_ext

		# Create the file and paste the data
		if partial_file_with_path:
			with open(partial_file_with_path, 'w') as f:
				f.write(textwrap.dedent(partial_code))

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