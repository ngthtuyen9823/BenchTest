TEMPLATE = """
  build-%d:
    runs-on: ubuntu-latest

    container:
      image: docker:stable
    steps:
      - name: Run
        run: docker run -e NUM=32 ngthvan1612/bench-test:v3
"""

WORKFLOW = """
name: CI

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]
  workflow_dispatch:

jobs:
"""

res = WORKFLOW
for i in range(0, 30):
  res += TEMPLATE.replace('%d', str(i + 1))

with open('.github/workflows/blank.yml', 'w') as f:
  f.write(res)
