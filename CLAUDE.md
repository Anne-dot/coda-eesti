# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## MANDATORY: Read Global Instructions First

**Before starting ANY work, you MUST:**

1. Read ALL files in `/home/d0021/Automation/ai-instructions/` directory
2. Read them WITHOUT optimization (read full files, not summaries)
3. Follow those instructions ALWAYS and CONTINUOUSLY throughout the session
4. Those instructions are NON-NEGOTIABLE and apply to ALL work in this repository

Global instruction files include:
- `instructions.md` - Core working principles, coding standards, documentation rules, response format requirements
- `eesti_keele_juhend.txt` - Estonian language usage rules

## Project Overview

Modern, accessible website for CODA Eesti (Co-Dependents Anonymous Estonia).

**Status:** Active development

## Tech Stack

See [docs/TECH_STACK_DECISION.md](docs/TECH_STACK_DECISION.md) for full details.

**Quick reference:** Astro + Sveltia CMS + Tailwind CSS + Shadcn/ui + Cloudflare Pages

## Commands

### Development
```bash
npm install          # Install dependencies
npm run dev          # Start dev server (localhost:4321)
npm run build        # Build for production (./dist/)
npm run preview      # Preview production build
npm run astro ...    # Run Astro CLI commands
```

### Common Operations
```bash
npm run astro add           # Add integrations
npm run astro check         # Type check
npm run astro -- --help     # Get help
```

## Project Structure

```
coda/
├── public/                 # Static assets (images, etc.)
├── src/
│   ├── pages/             # Routes (file-based routing)
│   └── components/        # Astro/React/Vue/Svelte components
├── docs/                  # Documentation
│   ├── TECH_STACK_DECISION.md
│   └── PROTOKOLLID/       # Meeting protocols
├── package.json
└── README.md
```

## Content

- Contact information & meeting details
- Recovery materials (promises, daily texts, stories)
- Estonian-language book recommendations
- Links to international CODA & 12-step organizations

## Key Features

- 🎨 CODA.org inspired design (clean, calm, welcoming)
- 📱 Mobile-first responsive
- ♿ Accessible (Lighthouse 90+)
- ⚡ Fast (static site, zero JS by default)
- 🔒 Git-based CMS (easy for non-technical users)
- 🌍 Multilingual ready (Estonian primary)

## Important Files

- **README.md** - Project overview and quick start
- **docs/TECH_STACK_DECISION.md** - Why this tech stack
- **docs/PROTOKOLLID/2025-10-29.md** - Initial planning meeting
- **CODA_uurimustöö_veebilehed.md** - Platform research

## Design Principles

- **CODA.org inspired** - Professional yet welcoming
- **ADHD-friendly** - Clear structure, readable
- **Mobile-first** - Most users on phones
- **Accessibility** - Following WCAG guidelines
- **Performance** - Fast load times

## Content Management

Multiple administrators can manage content through Sveltia CMS (git-based workflow).

User guide coming soon for content editors.

## Context

This is a community project for CODA Estonia recovery community. Human-first approach required (not corporate). Multiple people will manage content (non-technical users).

## Related Links

- [CODA.org](https://coda.org) - International CODA
- [CODA Germany](https://coda-deutschland.de)
- [CODA UK](https://codauk.org)
- [CODA Canada](https://codacanada.ca)
