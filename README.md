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
      uses: github-actions-x/commit@v2.0
      with:
        github-token: ${{ secrets.GITHUB_TOKEN }}
        push-branch: 'master'
        commit-message: 'publish'
        force-add: 'true'
```
