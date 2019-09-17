#!/bin/sh -l

git_setup ( ) {
  cat <<- EOF > $HOME/.netrc
		machine github.com
		login $GITHUB_ACTOR
		password $INPUT_GITHUB_TOKEN
		machine api.github.com
		login $GITHUB_ACTOR
		password $INPUT_GITHUB_TOKEN
EOF
  chmod 600 $HOME/.netrc

  git config --global user.email "$GITHUB_ACTOR@users.noreply.github.com"
  git config --global user.name "$GITHUB_ACTOR"
  
  : ${INPUT_PUSH_BRANCH:=`echo "$GITHUB_REF" | awk -F / '{ print $3 }' `}
}

git_setup

echo ::debug:: username — $GITHUB_ACTOR, branch — $INPUT_PUSH_BRANCH, commit message — $INPUT_COMMIT_MESSAGE
echo ::debug:: $(cat $HOME/.netrc)

git checkout $INPUT_PUSH_BRANCH

ADD_ARGS = ''
if [[ $INPUT_FORCE_ADD = 'true' ]]
then
    ADD_ARGS = '-f'
fi
git add $ADD_ARGS .

git commit -m $INPUT_COMMIT_MESSAGE

git push --follow-tags --set-upstream origin $INPUT_PUSH_BRANCH