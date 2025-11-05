# BGI/Ethornell .arc rebuild
A python script made to fix the annoying amount of files when making a translation patch for a BGI/Ethornell Visual Novel.
### What is this?/What does it do?
~~This is a python script that takes all the BGI/Ethornell files in a directory to repack a .arc file.~~

This is now part of [BGI/Ethornell Tools](https://github.com/Jair4x/ethornell-tools), a collection of tools using Python for the BGI/Ethornell Engine.
That includes:

- Extraction and rebuilding of .arc files
- Decompression and compression of DSC (extensionless) files.

## Useful information
- Most dialog scripts are almost always stored in `data015x0.arc`. (`data01500.arc`, `data01510.arc`, `data01520.arc` and so on)

- Sometimes, menu images and CGs you might want to edit are stored in `data025x0.arc`.

- I strongly recommend you use [crskycode's (now nanami5270's) fork of GARbro](https://github.com/nanami5270/GARbro-Mod) to unpack the .arc files as well as [marcussacana's SacanaWrapper](https://github.com/marcussacana/SacanaWrapper) with the plugin for BGI files to work with the scenario scripts and make translation easier.
