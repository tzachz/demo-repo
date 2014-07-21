import glob
import re
import ntpath
import os
from fabric.api import task, put, run, env, hosts, cd


def get_destination_file_folder(file_name):
    folder_name = re.match("(^.+)_[\w\.\-]+_amd64\.deb$", ntpath.basename(file_name)).groups()[0]
    folder = '/home/debian/%s' % folder_name
    return folder, folder_name


def get_build_debain_file(build_dir):
    files = glob.glob("%s/linux-package/*.deb" % build_dir)
    assert len(files) == 1, "found %s debians, expecting 1" % len(files)
    return files[0]


def copy(file_name):
    folder, folder_name = get_debian_destination_file_folder(file_name)
    run("mkdir -p %s" % folder)
    put(file_name, folder)
    return folder, folder_name

