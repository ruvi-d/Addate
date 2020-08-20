import os
import platform
import sys
import time
from multiprocessing import Pool
from pathlib import Path
from typing import List, Union

import click
from tqdm import tqdm


def get_file_date(path_to_file: str):
    stat = os.stat(path_to_file)
    secs = stat.st_mtime
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(secs))

def rename_file(path_to_file: str):
    file_creation_label = get_file_date(path_to_file)
    full_label = os.path.dirname(path_to_file)+ "/" + file_creation_label + " "+ os.path.basename(path_to_file)
    os.rename(path_to_file,full_label)

def process_folder(*, dir_path: Path, workers: int, only_images: bool, recursive: bool) -> None:
    all_files = get_all_files(dir_path=dir_path, recursive=recursive)
    if only_images:
        all_files = get_all_images(all_files=all_files)
    all_files = [str(fpath) for fpath in all_files]
    with Pool(processes=workers) as p:
        list(tqdm(p.imap(rename_file, all_files), total=len(all_files)))

def get_all_images(*, all_files: List[Path]) -> List[Path]:
    img_suffixes = [".jpg", ".jpeg", ".png", ".gif",".JPG"]
    all_images = [fpath for fpath in all_files if fpath.suffix in img_suffixes]
    print("Found {} images".format(len(all_images)))
    return all_images

def get_all_files(*, dir_path: Path, recursive: bool) -> List[Path]:
    if not (dir_path.exists() and dir_path.is_dir()):
        raise ValueError("{} doesn't exist or isn't a valid directory!".format(dir_path.resolve()))
    if recursive:
        all_files = dir_path.rglob("*")
    else:
        all_files = dir_path.glob("*")
    all_files = [fpath for fpath in all_files if fpath.is_file()]
    print("Found {} files in the directory: {}".format(len(all_files), dir_path.resolve()))
    return all_files

@click.command()
@click.option(
    "-d", "--img_dirs", required=True, help='Directories to scan for files and rename; separated by space, eg: "dir1/dir2 dir3" [required]'
)
@click.option("-w", "--workers", default=1, help="No of processing threads to spawn")
@click.option(
    "-i", "--only_images", is_flag=True, default=False, help="Whether to only rename images"
)
@click.option("-r", "--recursive", is_flag=True, default=False, help="Whether to recursively look in to sub folders for files")
def main(img_dirs: str, workers: str, only_images: bool, recursive: bool) -> None:
    img_dirs = [Path(img_dir) for img_dir in img_dirs.split()]
    for img_dir in img_dirs:
        process_folder(dir_path=img_dir, workers=workers, only_images=only_images, recursive=recursive)
    print("File prepending with date completed!")

if __name__ == "__main__":
    main()
