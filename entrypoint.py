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
    force_push = local.env.get('INPUT_FORCE-PUSH')
    branch = local.env.get('INPUT_PUSH-BRANCH') or "/".join(local.env.get('GITHUB_REF').split('/')[2:])
    rebase = local.env.get('INPUT_REBASE', 'false')
    files = local.env.get('INPUT_FILES', '')
    email = local.env.get('INPUT_EMAIL', f'{github_actor}@users.noreply.github.com')
    name = local.env.get('INPUT_NAME', github_actor)
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
    debug(git(['config', '--global', 'user.email', email]))
    debug(git(['config', '--global', 'user.name', name]))
    debug(git(['config', '--global', '--add', 'safe.directory', '/github/workspace']))
    debug(f'username:{github_actor}, branch:{branch}, commit message:{commit_message}')
    with open(netrc_path) as f:
        debug(f.read())
    add_args = ['add']
    if force_add == 'true':
        add_args.append('-f')
    add_args.append('-A')
    if files:
        debug(f"Files: {files}")
        add_args.extend(files.strip("'").split())
    if rebase == 'true':
        debug(git(['pull', '--rebase', '--autostash', 'origin', branch]))
    push_args = ['push', '--follow-tags', '--set-upstream', 'origin', branch]
    if force_push == 'true':
        push_args.append('--force')
    debug(git(['checkout', '-B', branch]))
    debug(git(add_args))
    debug(git(['commit', '-m', commit_message], retcode=None))
    debug(git(push_args))

if __name__ == '__main__':
    run()
