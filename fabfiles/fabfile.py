#!/usr/bin/env python

from fabric.api import *
from fabric.contrib import *


def install_ubuntu():
    """
       Installs a base ubuntu system using fabric.

    .. warning::
       openssh-server running on the remote ubuntu host,
         this is not the default configuration.

    """
    sudo('apt-get update')
    sudo('apt-get dist-upgrade')
    sudo('apt-get install keychain emacs texlive-full git-core subversion \
        ubuntu-restricted-addons ubuntu-restricted-extras screen \
        ssh-askpass-gnome system-config-lvm auctex vim')
    post_install_linux()


def post_install_linux():
    """
        Prep the newly installed system for use

        First, create the initial projects directory
    """
    if not files.exists('/home/%s/Projects' % env.user):
        run('mkdir -P /home/%s/Projects' % env.user)

    """
        Now clone the dotfiles repo and run install_dotfiles
    """
    with cd('/home/%s/Projects' % env.user):
        run('git clone git@github.com:mosburn/dotfiles.git')
    with cd('/home/%s/Projects/dotfiles' % env.user):
        run('sh install_dotfiles')
