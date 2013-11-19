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


def install_osx():
    """
        Installs base OSX settings to speed up development.
        This logic of this is to install python related components,
        sets up git, and installs some base configurations

        :requires xcode: Requires XCode to compile the python modules

    """

    """Python bashrc configuration"""
    if not files.contains('~/.bashrc',
                          '#pip should only run if there is a virtualenv \
                            currently activated'):
        files.append('~/.bashrc',
                     'export PIP_REQUIRE_VIRTUALENV=true')
    if not files.contains('~/.bashrc',
                          'export PIP_REQUIRE_VIRTUALENV=true'):
        files.append('~/.bashrc',
                     '#pip should only run if there is a virtualenv currently \
                     activated')
    if not files.contains('~/.bashrc',
                          '# cache pip-installed packages to avoid \
                          re-downloading'):
        files.append('~/.bashrc',
                     '# cache pip-installed packages to avoid re-downloading')
    if not files.contains('~/.bashrc',
                          'export PIP_DOWNLOAD_CACHE=$HOME/.pip/cache'):
        files.append('~/.bashrc',
                     'export PIP_DOWNLOAD_CACHE=$HOME/.pip/cache')
    if not files.contains('~/.bashrc',
                          'export WORKON_HOME=$HOME/.virtualenvs'):
        files.append('~/.bashrc',
                     'export WORKON_HOME=$HOME/.virtualenvs')
    if not files.contains('~/.bashrc',
                          'export PROJECT_HOME=$HOME/Projects'):
        files.append('~/.bashrc',
                     'export PROJECT_HOME=$HOME/Projects')
    if not files.contains('~/.bashrc',
                          'source /usr/local/bin/virtualenvwrapper.sh'):
        files.append('~/.bashrc',
                     'source /usr/local/bin/virtualenvwrapper.sh')

    """Check for existance of a ssh key, if not it creates it"""
    if not files.exists("~/.ssh/id_rsa.pub"):
        """Generate the new key"""
        run('ssh-keygen -t rsa -b 4096 ')
