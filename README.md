(This was build as part of a guided project to practice writing a simple static site generator in Python.)

# Tolkien Fan Club Static Site

A small static site I built while learning to code, generated with a custom Python static site generator.  
Content is written in Markdown and compiled to HTML, then deployed via GitHub Pages.

## Features

- Markdown ➜ HTML conversion (including headings, lists, links, images, code)
- Simple templating with a shared `template.html`
- Recursive content generation from the `content/` directory
- Static assets (CSS, images) copied from `static/`
- Configurable site base path for GitHub Pages deployments

## Project Structure

- `src/` – generator source code (Markdown parsing, HTML nodes, CLI entrypoint)
- `content/` – Markdown content (`index.md`, blog posts, contact page, etc.)
- `static/` – CSS and image assets
- `docs/` – generated production site (GitHub Pages serves from here)
- `template.html` – HTML template used for all pages
- `build.sh` – build script for production (GitHub Pages)
- `main.sh` – local development helper (build + local server)

## Running Locally

From the project root:

```bash
./main.sh
```
This builds the site with the default base path / and starts a local server so you can view it in the browser.

## Deployment

The site is deployed via GitHub Pages from the main branch, docs/ folder.

GitHub repo: https://github.com/GritandGo/static-site-generator
Live site: https://GritandGo.github.io/static-site-generator/
