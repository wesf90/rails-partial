# Sublime Text 2 plugin: Rails Partial

Makes creating Rails Partials a breeze. Quickly create a blank Partial, or select text and create the partial instantly!


## Shortcut Keys

There are two shortcuts, "Create Partial", and "Create Partial and Open". The latter option simply loads the partial into Sublime Text after creating it.

**Windows / OSX / Linux:**

 * `ALT+P` - Create Partial
 * `SHIFT+ALT+P` - Create Partial and Open


## How to Use

The following instructions are all done inside your Rails Apps's view (.erb, .html, .haml, .slim) or stylesheet (.css, .scss, .sass) files.


#### Creating a Partial from Code
1. Select the block of code you wish to put into a partial and hit the Shortcut Key
2. Name the Partial (the preceding underscore and the file extension is not required)
3. Hit `Enter`. Done! Your partial is located in the same directory as your original file.


#### Creating a Blank Partial
If you do not select any code before hitting the shortcut key, this plugin will simply create a blank partial file and insert the render/import code in your view/stylesheet as appropriate.


#### Creating Partials in other directories
If you wish to create your partial in a different directory, simply type the directory name followed by a slash and the partial name. For example:

To create a partial inside of app/views/shared/_partial_name.html.erb (a common directory belonging for your views), you would type: `shared/partial_name`. You could also enter `common/partial_name` as well as `somedir/subdir/partial_name`.


#### Importing Stylesheets
The same methods above can be applied to your .css, .scss/.sass files. Try it out!


## Limitations

This plugin has support for the following file types:
 - **Markup:** .erb, .html, .haml, .slim
 - **Stylesheet:** .css, .scss, .sass.

This list will possibly be expanded in the future. If you would like support for other files, please submit an issue or an pull request.


## Installation

You have two options, we'll start with the preferred installation method, Package Control.


### Package Control

The easiest and preferred way to of installing this plugin is with [Package Control](http://wbond.net/sublime\_packages/package\_control).

 * Ensure Package Control is installed and Sublime Text 3 has been restarted.
 * Open the Command Palette (Command+Shift+P on OS X, Control+Shift+P on Linux/Windows).
 * Select "Package Control: Add Repository"
 * Enter https://github.com/wesf90/rails-partial/tree/st3
 * Select "Package Control: Install Package"
 * Enter rails-partial

Even though Package Control makes it look like it's installing the ST2 version, you should find that in fact the ST3 branch has been installed.

Package Control will automatically keep Rails Partial up to date with the latest version.


### Git

This method required a little more work, but simply clone this repo into your Sublime Text 2 Package directory.

``` bash
$ git clone git://github.com/wesf90/rails-partial.git Rails Partial
```

Further instructions below.

#### Windows XP, 7 and 8
Execute the commands below one by one in your Command prompt.

``` bash
$ cd "%APPDATA%\Sublime Text 2\Packages"
$ git clone git://github.com/wesf90/rails-partial.git "Rails Partial"
```

#### Linux
Execute the commands below one by one in your terminal.

``` bash
$ cd ~/.config/sublime-text-2/Packages/
$ git clone git://github.com/wesf90/rails-partial.git Rails\ Partial
```
