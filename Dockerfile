FROM python:3.7-alpine

LABEL version="1.0.0"
LABEL repository="https://github.com/github-actions-x/commit"
LABEL homepage="https://github.com/github-actions-x/commit"
LABEL maintainer="Ruslan Nasonov <rus.nasonov@gmail.com>"

LABEL com.github.actions.name="Git commit and push"
LABEL com.github.actions.description="Commits any changed files and pushes the result back to origin."
LABEL com.github.actions.icon="git-commit"
LABEL com.github.actions.color="green"
COPY LICENSE README.md /

RUN apk --update --no-cache add git && pip install plumbum

COPY "entrypoint.sh" "/entrypoint.sh"

ENTRYPOINT ["/entrypoint.sh"]