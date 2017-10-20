1. Install npm (npm install npm -g)
2. Create book.json in project's root  (Gitbook settings)
3. Create SUMMARY.md in /docs directory (table of content(ToC) - tree structure of book - chapters and articles)
4. Save all .md files linked from ToC in the /docs directory - e.g. getting-started.md, api-reference.md
5. Create README.md ( book's introduction)

# Previewing the book
1. Install gitbook-cli and add to development dependency( npm install gitbook-cli --save-dev )
2. create package.json in root and add following script:
`
"scripts": {
   "docs:prepare": "gitbook install",
   "docs:watch": "npm run docs:prepare && gitbook serve"
}
`
3. run the watch task (npm run docs:watch)
4. book will be hosted on localhost:4000

# Publishing the book on Github Pages

