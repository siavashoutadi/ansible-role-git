Role Name
=========

A role to install and configure git.

Requirements
------------

None.

Role Variables
--------------

```yaml
# Git packages. By default only git is installed.
# But for example it can be changed to git-all.
git_packages:
  - git

# List of git configuration. Scope is system or global
# and the default value is global.
# Example:
# git_config:
#   - name: user.name
#     value: My name
#     scope: global
#   - name: user.email
#     value: myemail@mail.com
#     scope: global
git_config: []

# Global git configuration will be added to home directroy
# of this user: ~/.gitconfig
git_user: root

```

Dependencies
------------

None.

Example Playbook
----------------

playbook.yml
```yaml
- hosts: servers
  vars:
    git_config:
      - name: user.name
        value: User1
      - name: user.email
        value: user1@mail.com
      - name: alias.co
        value: "checkout"
        scope: "system"
      - name: alias.st
        value: "status"
        scope: "system"
  roles:
    - role: siavashoutadi.git
```

License
-------

Apache 2.0.

Author Information
------------------

Siavash Outadi.
