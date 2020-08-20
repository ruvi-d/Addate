# Addate

Have you ever noticed that you various capture devices (your phone, camera, GoPro, etc) have their own file naming schemes?  

Usually this isn't a big deal, but it quickly starts to suck when you realize that every piece of software (file manager to editor) defaults to alphabetically sorting. Sometimes the gods are extra cruel and you can have the same filenames from multiple sources.

Addate solves this annoyance by providing a script to prepend (append to front) the file creation date to the filename so that your files, from all your devices are chronologically sorted; even when the view is alphabetically sorted. There is even multi-threaded support to speed things up.

Many thanks to [difference-engine/thumbnail-generator-ubuntu](https://github.com/difference-engine/thumbnail-generator-ubuntu) from where I picked up many of the tricks. 

## Basic Usage
```
# Rename files in side a directory and it's subdirectories
addate -r -d directory1

# Rename files from two directories
addate -d directory1/directory1_1 directory2

# Pulling up the help
addate --help
```

## Command Line Options
| short | long          | Description                                                                                         |
|-------|---------------|-----------------------------------------------------------------------------------------------------|
| -d    | --img_dirs    | Directories to scan for files and rename; separated by space, eg: "dir1/dir2 dir3"  [required] |
| -w    | --workers     | No of processing threads to spawn                                                                    |
| -i    | --only_images | Whether to only rename images                                                   |
| -r    | --recursive   | Whether to recursively look in to sub folders for files                                                               |
|       | --help        | CLI help                                                                                            |

## Installation
Clone repo, navigate to folder and install using:
```
pip3 install .
```

To uninstall run:
```
pip3 uninstall addate
```
