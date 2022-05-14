# genREADME

# Generated code snippets
## Main
```c
#include <stdio.h>

int main() {
    printf("pokemon\n");
}
```
## Main
```ts
console.log("another");
```


## Usage

To Generate a README.md with code snippets. In your MAIN.md or any other file, use
`gen => [alt-name](link)`
for creating a code snippet.
1. alt-name will be the title if with_title = true and it is not empty
2. other wise if with_title = true, the the filename with first letter capitalized will be the title
3. link refers to the relative path to the file

### Example workflow

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Generate README.md
      uses: tezz-io/genREADME@main
      with:
        file: "MAIN.md"
        with_title: "true"
        n_hashes: "2"
    - name: Setup Username and email
    run: |
        git config user.name github-actions
        git config user.email github-actions@github.com
    - name: Push generated README.md  
    run: |
        git add .
        git commit -m "Generated README.md"
        git push
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `file`  | Path to MAIN.md or other .md file    |
| `with_title`  | Whether the title of the snippet should be present    |
| `n_hashes`  | The number of hashes before the title    |
