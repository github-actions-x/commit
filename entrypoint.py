#!/usr/bin/env python3

from plumbum import local
import os

def debug(message: str):
    print(f'##[debug]{message}')


def run():
    netrc_path = os.path.join(local.env.get('HOME', ''), '.netrc')
    github_actor = local.env.get('GITHUB_ACTOR')
    github_token = local.env.get('INPUT_GITHUB-TOKEN')
    commit_message = local.env.get('INPUT_COMMIT-MESSAGE')
    force_add = local.env.get('INPUT_FORCE-ADD')
    branch = local.env.get('INPUT_PUSH-BRANCH') or local.env.get('GITHUB_REF').split('/')[2]
    with open(netrc_path, 'w') as f:
        f.write(
            f'machine github.com\n'
            f'login {github_actor}\n'
            f'password {github_token}\n'
            f'machine api.github.com\n'
            f'login {github_actor}\n'
            f'password {github_token}\n'
        )
    chmod = local['chmod']
    git = local['git']
    debug(chmod(['600', netrc_path]))
    debug(git(['config', '--global', 'user.email', f'{github_actor}@users.noreply.github.com']))
    debug(git(['config', '--global', 'user.name', f'{github_actor}']))
    debug(f'username:{github_actor}, branch:{branch}, commit message:{commit_message}')
    with open(netrc_path) as f:
        debug(f.read())
    add_args = ['add']
    if force_add == 'true':
        add_args.append('-f')
    add_args.append('-A')
    debug(git(['checkout', '-b', branch]))
    debug(git(add_args))
    debug(git(['commit', '-m', commit_message], retcode=None))
    debug(git(['push', '--follow-tags', '--set-upstream', 'origin', branch]))

if __name__ == '__main__':
    run()