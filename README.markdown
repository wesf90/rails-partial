# Sublime Text 2 plugin: Rails Partial

Makes creating Rails Partials a breeze. Quickly create a blank Partial, or select text and create the partial instantly!


## How to Use

1. Inside a Rails view file, select the text you with to put into a partial.
2. Hit the corresponding shortcut key listed below under "Shortcut Keys"
3. Name the Partial (the preceding underscore is not required)
4. You're done! If using HAML, ensure that the partial is not indented on the first line or you will receive an error.

If you do not select any text before hitting the shortcut key, this plugin will simple create the partial file and insert the "render" code as appropriate.


## Shortcut Keys

There are two shortcuts, "Create Partial", and "Create Partial and Open". The latter option simply loads the partial into the view where as the "Create Partial" only creates the partial.

Windows/OSX/Linux:
ALT+P: Create Partial
SHIFT+ALT+P: Create Partial and Open


## Limitations

This plugin only works for ERB/HTML/HAML and CSS/SCSS/SASS files. Other files will not work with this plugin. This will possibly be expanded in the future.

## Installation

You have two options, we'll start with the preferred installation method.

Sublime Text's Package Installer!

or

    $ git clone git://github.com/wesf90/rails-partial.git RailsPartial

into your Package directory:

### Windows 7:

    Copy the directory to: "C:\Users\<username>\AppData\Roaming\Sublime Text 2\Packages"

### Windows XP:

    Copy the directory to: "C:\Documents and Settings\<username>\Application Data\Sublime Text 2\Packages"
