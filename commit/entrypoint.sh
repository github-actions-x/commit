#!/bin/sh -l

git_setup ( ) {
  cat <<- EOF > $HOME/.netrc
		machine github.com
		login $GITHUB_ACTOR
		password $GITHUB_TOKEN
		machine api.github.com
		login $GITHUB_ACTOR
		password $GITHUB_TOKEN
EOF
  chmod 600 $HOME/.netrc

  git config user.email "$GITHUB_ACTOR@users.noreply.github.com"
  git config user.name "$GITHUB_ACTOR"
  
  : ${INPUT_PUSH_BRANCH:=`echo "$GITHUB_REF" | awk -F / '{ print $3 }' `}
}

git_setup
git checkout $INPUT_PUSH_BRANCH
git add .
git commit -m $INPUT_COMMIT_MESSAGE
git push --follow-tags --set-upstream origin $INPUT_PUSH_BRANCH