## commit

Git commit and push

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
      uses: github-actions-x/commit@v2.3
      with:
        github-token: ${{ secrets.GITHUB_TOKEN }}
        push-branch: 'master'
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
        uses: github-actions-x/commit@v2.3
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          push-branch: master
          commit-message: '${{ matrix.node-version }} adds auto-generated benchmarks and bar graph'
          rebase: 'true' # pull abd rebase before commit
```
