public:: true
type:: [[Project]]
description:: Yet Another SPARQL GUI
has-category:: WebApp
has-tagged-techniques::, #[[Web development]], #Javascript, #RDF, #Git, #[[Github actions]] 
has-tagged-roles:: #Developer 
has-linked-projects:: #[[Yasgui - SPARQL GUI]], #[[Yasgui Geo Plugin]] 
is-featured:: Yes
during-job:: #[[Job: Independent railway data freelancer]]
external-link:: https://github.com/Matdata-eu/Yasgui

## Overview

I forked the famous [Yasgui from Zazuko](https://github.com/zazuko/Yasgui) and have been actively developing it with several major features and improvements. The project has evolved significantly with 9 releases between December 2025 and January 2026, transforming it into a comprehensive SPARQL development environment.

- 🌐 [Production deployment](https://yasgui.matdata.eu/)
- 📖 [Documentation site](https://yasgui-doc.matdata.eu/)
- 🐳 [Docker Hub](https://hub.docker.com/r/mathiasvda/yasgui)
- 📦 [npm Package](https://www.npmjs.com/package/@matdata/yasgui)

## Major Features Developed

### 🗂️ Workspaces & Managed Queries (v5.11.0)
Revolutionary feature enabling query storage and management through SPARQL endpoints or Git repositories. This enables collaborative query development and version control for enterprise environments. [Documentation](https://yasgui-doc.matdata.eu/docs/user-guide#managed-queries-and-workspaces)

### 🔐 Comprehensive Authentication Suite (v5.7.0)
Implemented multiple authentication methods for secure enterprise integration:
- Bearer Token authentication
- API Key authentication with custom headers
- Full OAuth 2.0 with PKCE support
- Automatic token refresh
- Per-endpoint authentication management

### 📊 Table Plugin Rewrite (v5.7.0)
Complete rewrite of the results table plugin using Tabulator.js (replacing Datatables.js), providing better performance, modern UI, and improved space utilization.

### 🎨 Advanced Theme System (v5.12.0-v5.13.0)
- User-configurable CodeMirror themes within settings
- Rainbow bracket colorization for improved code readability
- GitHub Dark theme as default for dark mode
- Enhanced syntax highlighting with improved color schemes

### 📤 Enhanced Share & Export (v5.10.0)
- Multiple share formats: PowerShell, wget, cURL
- URL shortening capability
- Security warnings when sharing credentials
- Copy to clipboard functionality

### 📐 Layout & UX Improvements (v5.8.0-v5.9.0)
- Vertical resizer in horizontal layout mode
- Optimized screen space utilization (Yasgui fills parent element)
- Smart endpoint button overflow handling with dropdown
- Fixed tab renaming interactions (drag, arrow keys, text selection, Delete key)
- Improved snippet bar collapsing behavior

### 🛠️ Developer Experience
- Fixed arbitrary HTTP headers support (v5.14.0)
- Better CORS error handling with clear user feedback
- Persistent storage management with clear option
- Default `.rq` file extension for Git workspaces
- Improved keyboard shortcuts and code formatting integration