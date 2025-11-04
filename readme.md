# BGI/Ethornell .arc rebuild
A python script made to fix the annoying amount of files when making a translation patch for a BGI/Ethornell Visual Novel.
### What is this?/What does it do?
This is a python script that takes all the BGI/Ethornell files in a directory to repack a .arc file.

(It also works if you create sub-folders with the name of the .arc file to create and put the files inside!)

## How do I use it?
Simply run `python rebuild.py` in a terminal/cmd, a folder called "extracted" should be created along with some indications.

Now, you can take two routes (because you can do both at the same time):

### 1. Bulk .arc rebuilding
You can create sub-folders with the name of the .arc file you want to create (example: 'data01510') and drop all the extension-less files there.

When you run the script, a new .arc.new file with the name of the sub-folder will be created with the files inside it.

### 2. One-by-one .arc rebuilding
Just drop the extension-less files inside the 'extracted' folder. You only can make one .arc at a time.

__Make sure you have the original .arc file, for naming purposes.__ (little life hack: create a new text file, call it whatever and make the extension .arc, the script just wants the name.)

## Useful information
- Delete the .new extension in order to make BGI understand it. (And delete/backup the original .arc file, don't be a dummy)

- Most dialog scripts are almost always stored in `data015x0.arc`. (`data01500.arc`, `data01510.arc`, `data01520.arc` and so on)

- Sometimes, menu images and CGs you might want to edit are stored in `data025x0.arc`.

- I strongly recommend you use [crskycode's (now nanami5270's) fork of GARbro](https://github.com/nanami5270/GARbro-Mod) to unpack the .arc files as well as [marcussacana's SacanaWrapper](https://github.com/marcussacana/SacanaWrapper) with the plugin for BGI files to work with the scenario scripts and make translation easier.

## TODO
- ~~*Compression.*~~ Yeah, no. The thing is, GARbro already decompresses the DSC files (the extensionless files you get), so trying to compress the files here would be dumb. I noticed this after almost a year of having created this tool (AKA right now, at the time of this commit, when reviewing the file). I'll work on DSC recompression using the decompression GARbro uses as a base, but I might or might not get it working. Expect this readme to change if I get it working or leave it as-is.

## Found a problem?/Have a suggestion?
Create an Issue! I'll be happy to try and fix your problem or listen to your feedback.
