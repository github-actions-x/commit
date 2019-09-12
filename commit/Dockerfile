FROM alpine:3.10

LABEL version="1.0.0"
LABEL repository="https://github.com/rusnasonov/actions"
LABEL homepage="https://github.com/rusnasonov/actions"
LABEL maintainer="Ruslan Nasonov <rus.nasonov@gmail.com>"

LABEL com.github.actions.name="GitHub Action for git commit"
LABEL com.github.actions.description="Commits any changed files and pushes the result back to origin."
LABEL com.github.actions.icon="git-commit"
LABEL com.github.actions.color="green"
COPY LICENSE README.md /

RUN apk --update --no-cache add git

COPY "entrypoint.sh" "/entrypoint.sh"

ENTRYPOINT ["/entrypoint.sh"]