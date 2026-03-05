function fixall
  gd --name-only --cached | xargs yarn eslint --fix
  gd --name-only --cached | xargs yarn prettier --write

  gd --name-only | xargs yarn eslint --fix
  gd --name-only | xargs yarn prettier --write

  gd origin/main... --name-only | xargs yarn eslint --fix
  gd origin/main... --name-only | xargs yarn prettier --write
end
