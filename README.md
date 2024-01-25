## Python-based short URL generator, deployed as a static site

The `build.py` script will open the `urls.json` file and generate a "public" folder into which it will create a static file for each URL to redirect the browser.

The main benefit here is that you're not using a full framework, most static site deployment providers will deploy a static site for free and attach your own domain name, and you can add whatever analytics tracking etc into the build script template that you like.

Each short URL will also support the `+` suffix to preview what the URL redirect is going to be, e.g. `https://example.com/shorturl+` will show you the redirect URL before you're redirected.


## Deploy to Render

1. Fork this repo
2. Alter the `urls.json` file to your liking
3. Push your changes to your own repo
4. Click this button to deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)


## Future plans

1. Make the template HTML external to the Python script.
2. Add cmd-line scripts to add/edit/delete URLs from the JSON file.


## Contributions welcome

Please feel free to submit a PR to improve this project or suggest improvements through the Issues tab.
