# Setting up Gitbook for a project
Credits to [this](https://medium.com/@gpbl/how-to-use-gitbook-to-publish-docs-for-your-open-source-npm-packages-465dd8d5bfba) guide

> IMPORTANT I am using node LTS (node version 6.11.4 and npm version 3.10.10), you may run into erros using current version of node.


1. Install npm (npm install npm -g)
2. Create book.json in project's root  (Gitbook settings & structure)
```
{ 
    "gitbook": "2.5.2",
    "structure": { 
      "summary": "docs/SUMMARY.md" 
    } 
}
```
3. Create SUMMARY.md in /docs directory (table of content(ToC) - tree structure of book - chapters and articles)
```
# Table of content 
* [Getting Started](docs/getting-started.md)
```
4. Save all .md files linked from ToC in the /docs directory - e.g. getting-started.md
5. Create README.md in the root ( book's introduction)

## Previewing the book
1. Install gitbook-cli and add to development dependency
```
npm install gitbook-cli --save-dev
```
2. create package.json in root and add following script:
```
"scripts": {
   "docs:prepare": "gitbook install",
   "docs:watch": "npm run docs:prepare && gitbook serve"
}
```
3. run the watch task (npm run docs:watch)
4. book will be hosted on localhost:4000

## Publishing the book on Github Pages

Refer to [this](https://help.github.com/articles/user-organization-and-project-pages/#project-pages) for User/Organization vs Project GitHub Pages

To publish the book, you need to create an empty gh-pages branch and the content you push onto that branch will be published as http://[username].github.io/[repo]

1. [Manually create gh-pages branch](https://help.github.com/articles/creating-project-pages-using-the-command-line/) 
 + asdf
2. adsf



