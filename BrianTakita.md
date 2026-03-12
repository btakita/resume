# Brian Takita

Shipping production AI systems and building agent tooling — real-time multimodal pipelines, spec-driven development infrastructure, context engineering. 20+ years full-stack experience.

<div style="text-align:center" class="contact-line">
**LinkedIn:** [linkedin.com/in/briantakita](https://www.linkedin.com/in/briantakita/) |
**Email:** [btak.dev@gmail.com](mailto:btak.dev@gmail.com) |
**GitHub:** [btakita](https://github.com/btakita)
</div>

<div style="text-align:center" class="contact-line">
Greater Boston, MA |
**Website:** [briantakita.me](https://briantakita.me) |
**Phone:** [+1 (424) 249-2350](tel:+14242492350)
</div>

## Summary

Architected a production real-time multimodal AI avatar pipeline at Presence AI — text, audio, and video lip-sync on NVIDIA H100 GPUs via WebRTC. Now building agent tooling in Rust: git-native correspondence (corky), document-as-interface for persistent AI sessions (agent-doc), and cross-language naming analysis (tagpath). A decade of context engineering — from a domain ontology system (2014) through reactive frameworks to modern agentic systems. Deep expertise in event-driven architecture, reactive programming, and collaborative intelligence workflows where agents and humans work in parallel.

## Skills

Context Engineering, Spec-Driven Development, Agents, Rust, Python, TypeScript, Zig, React, SvelteJS, Docker, WebRTC, REST, GraphQL, Node.js, Next.js, Django, FastAPI, Flask, Graphene, SQLAlchemy, Angular, Vue.js, Zod, Flutter, Go, Ruby on Rails, C#, PostgreSQL, Supabase, Firebase, AWS, Terraform, Google Cloud, Azure, CI/CD, Plesk, Heroku, Agentic Systems, Claude, Squarespace, WordPress, Wix

## Career Highlights

- **Presence AI** — Architected real-time multimodal AI avatar pipeline — text, audio, and video lip-sync on NVIDIA H100 GPUs via WebRTC
- **Open Source** — corky: git-native correspondence in Rust | agent-doc: document-as-interface for AI agents | RSpec: BDD core contributor | rr: pioneered proxy test doubles
- **Pivotal Labs** — Mentored developers across 20+ startups. Speaker at RailsConf 2008. Early contributor to Behavior Driven Development
- **TrueCar / honk.com** — Led vehicle review platform development at honk.com (acquired by TrueCar); senior product team at TrueCar
- **Milyoni** — Social Entertainment Platform for Warner Brothers, Lions Gate, Paramount Studios, Universal Music Group
- **Censible** — 8-year ESG analytics platform — Martin Investments analyst portal, ESG Portfolio Rebalancing system
- **Context Engineering** — Domain ontology system (152 nodes) since 2014 — structuring agent reasoning across domains
- **Reactive Frameworks** — 15-year lineage: backbone-signal → ctx-core → rmemo → relysjs — applied to modern agentic systems

## AI Products Shipped

- **Presence AI Avatar Pipeline** — Architected and shipped a production real-time multimodal AI pipeline: facial landmark detection, lip-sync inference, and frame sequencing on NVIDIA H100 GPUs via WebRTC. Defined the agentic development methodology used by the engineering team.
- **corky** — Built and shipped a git-native correspondence system in Rust that syncs email, Telegram, and Slack into scoped markdown mailboxes with per-contact agent context and topic-based routing. Includes Whisper-powered diarized transcription for voice messages, social media posting with scheduled delivery, and bidirectional sync across providers. Prototyped in Python, then spec-driven rewrite to Rust in under 1 day. Used daily for professional correspondence.
- **agent-doc** — Created and shipped a document-as-interface tool for persistent AI conversations: offline markdown editing, diff-based submissions, write-safe concurrent editing via 3-way merge. Evolved from a document-as-interface pattern first built for Tenfore Holdings (2015). Used as primary development interface.
- **agent-kit** — Built a Rust SDK for CLI tools integrating with AI agent loops: session management, tmux pane routing, instruction file discovery (AGENTS.md/CLAUDE.md), and snapshot-based state tracking. Powers agent-doc and corky's agent integrations.
- **tmux-router** — Declarative tmux pane routing in Rust: sync editor layouts to tmux sessions, multiplexed agent orchestration across concurrent development contexts.
- **tagpath** — Built and shipped a cross-language identifier analysis tool in Rust: convention detection, semantic search, alias generation, and tag co-occurrence graphs across 14 tree-sitter grammars. Published to crates.io.

## Experience

### Presence AI — _Lead Backend Engineer, AI Pipeline_

<small>April 2024 – February 2026 (1 year 10 months)</small>

- Full-stack feature development: Next.js + React frontend ↔ GraphQL (urql) ↔ API Services ↔ Multimodal Avatar Agents + PostgreSQL. TypeScript monorepo with 8 internal packages (@presence-ai/api, design-system, livekit, analytics, credits, monitoring, error, web)
- Architected and shipped the entire real-time video pipeline: facial landmark detection, LatentSync lip-sync inference (VAE decode, denoising, restoration), idle video generation, and frame sequencing on NVIDIA H100 GPUs via WebRTC using LiveKit
- Architected a multi-service AI monorepo with closed-loop agentic workflows and self-auditing development infrastructure (Claude Code / Codex)
- Developed an iterative agentic development methodology: lightweight living specs refined through closed-loop agent auditing and continuous human-in-the-loop feedback, accelerating design velocity while staying in flow with the emerging design
- Built reusable async primitives for high-quality agent-authored code and human comprehension: task lifecycle management, scoped cancellation, lazily resolved dependencies that decouple initialization order and cascade invalidation through the context, runtime profile logging, and stable cross-stack naming to maintain conceptual coherence for both human and agent reasoning
- Improved lip-sync quality through landmark temporal smoothing, LatentSync model upgrades, and optimized Whisper audio feature extraction via improved audio stream batching

### Open Source — _Creator / Solo Developer_

<small>2006 – Present | Early contributor to Behavior Driven Development (BDD)</small>

#### **corky** — Git-Based Correspondence Toolkit (Rust) [github.com/btakita/corky](https://github.com/btakita/corky) | [Docs](https://btakita.github.io/corky)

- Built a git-native correspondence system that syncs topics, contacts, and threads from email (IMAP), Telegram, and Slack into scoped markdown mailboxes, with per-topic and per-contact agent context that propagates across collaborators via 3-way merge
- Designed multi-scope mailbox architecture where each collaborator receives only relevant threads and context, with bidirectional sync using content hashing (FNV-1a) and git-based conflict resolution for offline-first collaboration
- Implemented crash-safe incremental IMAP sync with streaming merge, bulk import for Slack and Telegram archives, and label-based routing rules that fan out threads to multiple mailboxes
- Dog-fooding daily for personal and professional correspondence across Gmail and Protonmail accounts

#### **agent-doc** — Document-as-Interface for Interactive Sessions with AI Agents (Rust) [github.com/btakita/agent-doc](https://github.com/btakita/agent-doc)

- Created a document-as-interface model for persistent AI conversations: edit a markdown file offline, submit diffs, agent responds inline — all tracked through git commits for full session history and branch-based workflows
- Engineered write-safe concurrent editing via 3-way merge (snapshot + user edits + agent response), preventing data loss when human and agent edit simultaneously
- Built agent-agnostic core with pluggable LLM backends, automatic pre-commit of user changes, and snapshot-based diffing so only changed content is sent to the agent
- Dog-fooding as the primary interface for planning and iterating on both corky and agent-doc development

#### **agent-kit** — SDK for AI Agent CLI Tools (Rust) [crates.io/crates/agent-kit](https://crates.io/crates/agent-kit)

- Built a Rust SDK for CLI tools that integrate with AI agent loops: session management, tmux pane routing, instruction file discovery, and snapshot-based state tracking
- Powers agent-doc and corky's agent integrations — shared foundation for session lifecycle, config resolution, and concurrent write safety

#### **tmux-router** — Declarative Tmux Pane Routing (Rust) [crates.io/crates/tmux-router](https://crates.io/crates/tmux-router)

- Declarative layout engine syncing editor state to tmux sessions — multiplexed agent orchestration across concurrent development contexts
- Auto-claims panes for agent sessions, routes documents to the correct editor, and maintains layout consistency across window resizes

#### _Other contributions:_

- _[lazily-py](https://github.com/btakita/lazily-py)_ — Creator. Lazy evaluation with context caching in Python
- _[lazily-zig](https://github.com/btakita/lazily-zig)_ — Creator. Cross-platform & thread-safe lazy evaluation with context caching in Zig
- _[ctx-core](https://github.com/ctx-core/ctx-core)_ — Creator. Explicit, scalable cross-platform, reactive contexts written in JavaScript
- _[rmemo (Reactive Memo)](https://github.com/ctx-core/rmemo)/[RelementJS](https://github.com/relementjs/relementjs)_ — Creator. Smallest & most composable reactive isomorphic UI library in JavaScript
- _[rappstack](https://github.com/rappstack)_ — Creator. Full-stack framework using BunJS & Elysia for extensible web app modules
- _[rebuildjs](https://github.com/rebuildjs/rebuildjs)_ — Creator. Simple hackable alternative to Vite for Multi-Page Apps
- _[relysjs](https://github.com/relysjs/relysjs)_ — Creator. Reactive web app server for MPAs with middleware and build APIs
- _[hyopjs](https://github.com/hyopjs/hyop)_ — Creator. Tiny hydration library (starting at 61 B)
- _[Generic Query Analyzer](https://sourceforge.net/projects/gqa.berlios/)_ — Creator. .NET WinForms query analyzer for OleDB data sources including MS Access
- _[SvelteJS](https://svelte.dev/)_ — Contributor (breadth-first queueing algorithm)
- _[Nano Stores](https://github.com/nanostores/nanostores)_ — Contributor (breadth-first queueing algorithm)
- _[rr (double Ruby)](https://github.com/rr/rr)_ — Creator. Test double framework for Ruby. Pioneered proxy-based test doubles (mock.proxy, stub.proxy) — pattern now standard as `patch` in Python's pytest/unittest
- _[RSpec](https://rspec.info/)_ — Core contributor to the Ruby Behavior Driven Development (BDD) testing framework
- _[backbone-signal](https://github.com/btakita/backbone-signal)_ — Creator. Signal & Slots reactive API for Backbone Models
- _[Screw Unit](https://github.com/nkallen/screw-unit)_ — Co-creator. BDD testing framework for JavaScript
- _[philosophy](https://github.com/btakita/philosophy)_ — Creator. Domain ontology system (152 nodes) defining scope, context, resolution, and abstraction — structuring agent reasoning across domains (since 2014)
- _[Desert](https://github.com/pivotal/desert)_ — Co-creator. Rails plugin framework with model/view/controller sharing

### Brian Takita — _Full-Stack Engineer_

<small>January 2019 – Feb 2026 (7 years 1 month)</small>

Manage, develop, & ensure success of short-term freelance software projects. Uses subcontractors for development. Web and mobile Flutter apps across all industries.

- **BestInform** — European information platform for structured data, reports, and analytics. Pixel-perfect Figma implementation; real-time support messaging. Angular 14, PrimeNG, Angular Material, Firebase. [bestinform.eu](https://bestinform.eu)
- **Guard App** — Security service platform connecting guards, companies, and customers. Admin portal and mobile apps for patrol management, incident reporting, NFC verification. Flutter, Angular, Firebase, Java Spring Boot.
- **Drivemond** — Taxi and ride-hailing platform for Chicago. Passenger and driver mobile apps with real-time matching and GPS tracking. Flutter, AWS.
- **Galler AI** — AI-powered image generation and editing platform in the browser. React frontend with Figma design system; cropping, clipping, drawing tools. React, TypeScript.
- **SafeSchoolz (Aegis Platform)** — AI safety platform detecting firearms and alerting authorities. Built gun detection model (~85% mAP). Android, .NET, Python/Jupyter, Twilio.
- **IIPM** — Membership and certification platform for Irish pension specialists. Member and admin portals. WordPress, PHP, JavaScript/jQuery, Stripe. [iipm.ie](https://iipm.ie)

### Censible — _Lead Product Developer_

<small>January 2016 – April 2024 (8 years 4 months) | Greater New York City Area</small>

Developed web solutions for Financial Services, centered around an Environment, Social, Governance (ESG) lens. These tools helped investors align their investments with their values & manage exposure to ESG topics.

- Built Martin Investments analyst portal with ESG rating algorithms, XLSX export handling 10,000+ rows, and SVG/PDF report generation
- Built [ESG Portfolio Rebalancing system](https://esg.censible.co/rebalance) and [ESG analytics platform](https://esg.censible.co) — [censible.co](https://censible.co/)

### SocialChorus — _Senior Software Engineer_

<small>February 2018 – August 2018 (7 months) | Remote</small>

- Product development on the Studio team
- Converted legacy Backbone frontend to Svelte & React
- ES5 to ES6/ES2017 migration
- Created best practices for front-end component development

### Neo Innovation, Inc. — _Software Development Consultant_

<small>September 2015 – December 2015 (4 months) | Greater New York City Area</small>

Built a document-as-interface application for Tenfore Holdings — a research pipeline where executives email contacts and contextual notes, which are semantically matched to companies and contacts in Salesforce, then routed to the analyst team for refinement. Early exploration of the document-as-interface pattern later evolved into agent-doc (2024).

### CrystalCommerce — _Senior Software Developer_

<small>January 2015 – September 2015 (9 months)</small>

Migrated production Rails app. Re-architected the front end using Node.js, Browserify, Gulp, and Backbone.

### Rundavoo — _Platform Architect / Lead Front End Developer_

<small>March 2013 – December 2014 (1 year 10 months) | Greater Los Angeles Area</small>

Led front-end development for Rundavoo, a Google top 75 app in 2014. Created a responsive, multi-platform (desktop, tablet, mobile, server) application that integrated with several APIs via CORS and a proxy server.

Technologies: HTML5, CSS3, Node.js, Browserify, Jasmine, reactive programming, Cloudflare, PhoneGap

### Milyoni, Inc. — _Architect / Lead Developer_

<small>March 2012 – March 2013 (1 year 1 month) | Pleasanton, CA</small>

Lead developer for Social Entertainment Platform including video, social marketing, gamification, real-time social interaction, and interactive engagements synced with video. Platform used by Warner Brothers, Lions Gate, Paramount Studios, Universal Music Group, Hearst Media, Starz, Ovation TV, Astro, Focus Features, Funimation, Sundance Now.

Mentored junior & mid-level developers. Proponent of flattening communication across the organization.

Technologies: Node.js, Backbone.js, Rails, Postgres, Redis, Heroku

### TrueCar / honk.com — _Lead Developer → Senior Software Engineer_

<small>August 2009 – February 2012 (2 years 7 months) | Santa Monica, CA</small>

Led development of honk.com, a vehicle review and white-label platform used by USAA and Wall Street Journal Autos. Honk had News Corp as an investor and was acquired by TrueCar. Partnered on product vision for social car shopping that was key to the acquisition.

At TrueCar, senior member of advanced product team — introduced new products, partner integrations (WSJ.com, USAA.com), and devops automation (Chef for EC2, workstations, datacenter servers). Rails 3 upgrade. Led initiatives to share agile knowledge across the organization.

- Full-stack Ruby on Rails + Sinatra development with Lucene search
- High Availability deployment on EC2 and Engine Yard
- JavaScript client/server event framework ([jelly](https://github.com/honkster/jelly))
- Chef scripts for server and workstation automation

### Pivotal Labs — _Agile Engineer_

<small>January 2006 – August 2009 (3 years 7 months)</small>

Agile Development in the XP tradition. TDD, Pair Programming, Daily Standups, Retrospectives. Mentored developers across 20+ startups, bootstrapping their engineering process, team, and initial product. Speaker at RailsConf 2008. Leadership role in common code, practices, and open source.

Projects: Honk, Maven Link, KGB.com, Grockit, KDA Research, Real Girls Media, heavy.com, Bringo, CommunityWalk

Open source contributions:

- [Erector](https://github.com/pivotal/erector) — Ruby Builder and Widget framework for generating HTML
- [JS Test Server](https://github.com/pivotal/js-test-server) — organized JavaScript TDD
- [Unison](https://github.com/grockit/unison) — event-driven relational algebra library for Ruby

### Peer to Patent Project — _Consultant_

<small>2007</small>

Key contributor to launching the Peer to Patent pilot application, led by New York Law School. A tool to allow the crowd to review and submit prior art for pending patents.

### NASPP — _IT Analyst_

<small>February 2004 – January 2006 (1 year 11 months)</small>

- SQL Server DB Admin
- Developed internal CRM with Rails, .NET & MS Access
- Website ASP development
- Reports for Sales Trends and forecasting

### Flextronics — _Web Application Developer Intern_

<small>May 2001 – February 2002 (9 months)</small>

Developed corporate intranet using Microsoft technologies (ASP, SQL Server).

## Education

**University of the Pacific**
BS, Engineering Physics (1997 – 2002)

## Certifications

- Advanced Permaculture Course in Teaching
- Permaculture Design Certificate

## Languages

English: Native
