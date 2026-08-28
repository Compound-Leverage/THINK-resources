# Privacy Policy — THINK School

Canonical version: [compoundleverage.com/privacy](https://www.compoundleverage.com/privacy/).

**TODO (Marvin):** confirm that page covers THINK School's plugin-distribution
model specifically (bring-your-own-data, third-party MCP connectors, no
server-side collection) -- it may currently be written for the consulting/services
side of the business only. The notes below describe how THINK School itself
handles data; update the canonical page to match if it doesn't already.

_Draft pending legal review. Last updated: 2026-08-28._

THINK School plugins are **bring-your-own-data**: each plugin runs inside your own
Claude Code, Codex, or ChatGPT session and connects only to services and accounts
you configure yourself (for example, your own Notion workspace, your own Hunter.io
key, your own email send-from account).

## What Compound Leverage collects

**Nothing server-side.** THINK School has no backend, no hosted database, and no
analytics pipeline of its own. The plugins are Markdown instructions and manifest
files distributed through this repository; they do not phone home, log your data,
or transmit anything to Compound Leverage.

## What the plugins can access

When you run a THINK School plugin, it acts through the AI assistant session you're
already using (Claude Code, Codex, or ChatGPT) and any MCP connectors you have
authorized in that session (e.g. Notion, Google Drive, Hunter.io, GitHub). Those
connectors are governed by **your** agreement with **their** providers, not by
Compound Leverage. Review each connector's own privacy terms before authorizing it.

## Your data stays yours

- No proprietary Compound Leverage data, client data, or methodology ships in
  these public plugins.
- Nothing you enter into `customization/` config files, or any data your
  connected accounts return, is collected or retained by Compound Leverage.

## Contact

Questions about this policy: [partners@compoundleverage.com](mailto:partners@compoundleverage.com).
