import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_git_installed(host):
    git = host.package("git")
    assert git.is_installed


def test_git_config(host):
    sys_config = host.file("/etc/gitconfig")
    sys_content = ['[alias]', '	co = checkout', '	st = status']
    assert sys_config.content_string == '\n'.join(sys_content) + "\n"
    global_content = ['[user]', '	name = User1', '	email = user1@mail.com']
    assert host.file(
        "/root/.gitconfig").content_string == '\n'.join(global_content) + "\n"
