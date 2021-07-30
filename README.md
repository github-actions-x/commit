## Github Commit & Push Action

Git commit and push

### Options

* **github-token**: *Required*. Github Token with commit access. If pushing to the same repo the action is running on, please use `${{ secrets.GITHUB_TOKEN }}`. If for another repo, create a personal private token, add it to secrets then use it here.
* **push-branch**: Override branch to push to, defaults to the same branch the action is currently running on.
* **push-remote**: Override remote to push to, defaults to the same repo the action is currently running on.  Must be in GIT URL format, example below.
* **commit-message**: Specify commit message, defaults to `autocommit`.
* **force-add**: Force add files, useful for adding ignored files. Defaults to `false`.
* **force-push**: Force git push, defaults to `false`.
* **rebase**: Pull and rebase before commiting. Useful when using commit inside matrix. Defaults to `false`
* **files**: Specific files to add. Uses the same format as `git add`. Defaults to all files.
* **email**: Committer email. Default is `${name}@users.noreply.github.com`
* **name**: Committer name. Default is name of the person or app that initiated the workflow.


### Example

```yaml
name: publish

on:
  push:
    branches:
    - master
    
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: checkout
      uses: actions/checkout@master
      with:
        ref: master
    - name: build
      uses: github-actions-x/hugo@master
    - name: push
      uses: github-actions-x/commit@v2.8
      with:
        github-token: ${{ secrets.GITHUB_TOKEN }}
        push-branch: 'master'
        push-remote: https://github.com/some-org/some-repo.git
        commit-message: 'publish'
        force-add: 'true'
        files: a.txt b.txt c.txt dirA/ dirB/ dirC/a.txt
        name: commiter name
        email: my.github@email.com 

```

If you use `commit` inside [matrix](https://help.github.com/en/articles/workflow-syntax-for-github-actions#jobsjob_idstrategymatrix), set variable `rebase='true'` for pulling and rebasing changes.

```yaml
name: Node CI

on:
  push:
    branches:
    - master

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version:
          - 10.x
          - 12.x
    steps:
      - uses: actions/checkout@v1
      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v1
        with:
          node-version: ${{ matrix.node-version }}
      - name: generate benchmarks
        run: |
          npm run generate-some-files-for-specific-node-version
      - name: push
        uses: github-actions-x/commit@v2.8
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          push-branch: master
          commit-message: '${{ matrix.node-version }} adds auto-generated benchmarks and bar graph'
          files: a.text build/
          rebase: 'true' # pull and rebase before commit
```
