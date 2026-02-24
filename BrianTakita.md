# Brian Takita

First principles emphasize powerful primitives, bottom-up development discipline, & systems with an observable domain ontology. Full stack developer with over 20 years experience. Productivity without the bloat.

**Location:** Greater Boston
**Email:** brian.takita@gmail.com
**Phone:** +1 (424) 249-2350
**LinkedIn:** [linkedin.com/in/briantakita](https://www.linkedin.com/in/briantakita)
**Website:** [briantakita.me](https://briantakita.me)

## Summary

Over 20 years of software development experience developing full-stack applications. Currently focused on the full pipeline of Realtime AI Avatars using Generative models.

Utilizes philosophy, logic, language, & qualitative/quantitative approaches to create software models to explore & accurately represent the domain.

**Top Skills:** Spec-Driven Development, Agents, Rust

---

## Experience

### Presence AI — Lead Backend Engineer, AI Pipeline
**April 2024 – Present**

- Architected and shipped the entire real-time video pipeline: facial landmark detection, LatentSync lip-sync inference (VAE decode, denoising, restoration), idle video generation, and frame sequencing on NVIDIA H100 GPUs via LiveKit
- Architected a multi-service AI monorepo with closed-loop agentic workflows and self-auditing development infrastructure (Claude Code / Codex)
- Developed an iterative agentic development methodology: lightweight living specs refined through closed-loop agent auditing and continuous human-in-the-loop feedback, accelerating design velocity while staying in flow with the emerging design
- Built reusable async primitives for high-quality agent-authored code and human comprehension: task lifecycle management, scoped cancellation, lazily resolved dependencies that decouple initialization order and cascade invalidation through the context, runtime profile logging, and stable cross-stack naming to maintain conceptual coherence for both human and agent reasoning
- Improved lip-sync quality through landmark temporal smoothing, LatentSync model upgrades, and optimized Whisper audio feature extraction via improved audio stream batching

### Open Source — Creator / Solo Developer
**2024 – Present**

**corky** — Git-Based Correspondence Toolkit (Rust, ~9,200 LOC)
[github.com/btakita/corky](https://github.com/btakita/corky) | [Docs](https://btakita.github.io/corky)

- Built a git-native correspondence system that syncs topics, contacts, and threads from email (IMAP), Telegram, and Slack into scoped markdown mailboxes, with per-topic and per-contact agent context that syncs across collaborators via 3-way merge
- Designed multi-scope mailbox architecture where each collaborator receives only relevant threads and context, with bidirectional sync using content hashing (FNV-1a) and git-based conflict resolution for offline-first collaboration
- Implemented crash-safe incremental IMAP sync with streaming merge, bulk import for Slack and Telegram archives, and label-based routing rules that fan out threads to multiple mailboxes
- Dog-fooding daily for personal and professional correspondence across Gmail and Protonmail accounts

**agent-doc** — Git-Native Document Sessions with AI Agents (Rust)
[github.com/btakita/agent-doc](https://github.com/btakita/agent-doc)

- Created a document-as-interface model for persistent AI conversations: edit a markdown file offline, submit diffs, agent responds inline — all tracked through git commits for full session history and branch-based workflows
- Engineered write-safe concurrent editing via 3-way merge (snapshot + user edits + agent response), preventing data loss when human and agent edit simultaneously
- Built agent-agnostic core with pluggable LLM backends, automatic pre-commit of user changes, and snapshot-based diffing so only changed content is sent to the agent
- Dog-fooding as the primary interface for planning and iterating on both corky and agent-doc development

### Brian Takita — Full Stack Web Engineer
**January 2019 – Present**

Manage, develop, & ensure success of short-term freelance software projects. Uses subcontractors for development. Web and mobile Flutter apps across all industries.

### Censible — Lead Product Developer
**January 2016 – Present** | Greater New York City Area

Develop web solutions for Financial Services, centered around an Environment, Social, Governance (ESG) lens. These tools help investors align their investments with their values & to manage exposure to ESG topics.

- [censible.co](https://censible.co/)
- [esg.censible.co](https://esg.censible.co)
- [esg.censible.co/rebalance](https://esg.censible.co/rebalance)

### SocialChorus — Senior Software Engineer
**February 2018 – August 2018** | Remote

- Product Development on the Studio team
- Convert legacy Backbone FrontEnd to Svelte & React
- ES5 to ES6/ES2017 migration
- Create best-practices for Front End component development

### Neo Innovation, Inc. — Software Development Consultant
**September 2015 – December 2015** | Greater New York City Area

Developed email-based research pipeline app for Financial Holdings company. Workflow involves actor (i.e. CEO or sales) emailing contacts & contextual notes, to be researched and processed by the analyst team. The app semantically matches the text to companies & contacts in Salesforce to assist the analyst team with further refinements & analysis.

### CrystalCommerce — Senior Software Developer
**January 2015 – September 2015**

Migrate production Rails App. Front end rearchitecturing using Node.js, Browserify, Gulp, Backbone.

### Rundavoo — Platform Architect / Lead Front End Developer
**March 2013 – December 2014** | Greater Los Angeles Area

Lead front end development for Rundavoo, a Google top 75 app in 2014. Created a responsive, multi-platform (desktop, tablet, mobile, server) application that integrated with several APIs via CORS and a proxy server.

Technologies: HTML5, CSS3, Node.js, Browserify, Jasmine, reactive programming, Cloudflare, PhoneGap

### Milyoni, Inc. — Architect / Lead Developer
**March 2012 – March 2013** | Pleasanton, CA

Lead developer for Social Entertainment Platform including video, social marketing, gamification, real time social interaction, and interactive engagements synced with video. Platform used by Warner Brothers, Lions Gate, Paramount Studios, Universal Music Group, Hearst Media, Starz, Ovation TV, Astro, Focus Features, Funimation, Sundance Now.

Mentor junior & mid-level developers. Proponent of flattening communication across the organization.

Technologies: Node.js, Backbone.js, Rails, Postgres, Redis, Heroku

### TrueCar, Inc. — Senior Software Engineer
**August 2010 – February 2012** | Santa Monica, CA

Senior member of advanced product team, which introduced new products, integration with major partners (WSJ.com, USAA.com car reviews), and devops (Chef to automate EC2 architecture, workstations, and new datacenter servers). Rails 3 Upgrade. YUM packaging for deployment.

Led initiatives to share agile knowledge across the organization and integrate services.

### honk.com — Lead Developer
**August 2009 – August 2010**

Vehicle review site and embeddable white-label platform used by USAA and Wall Street Journal Autos (invested by Fox News Corp, acquired by TrueCar). Lead development and partnered in product vision for social car shopping that was key to the acquisition.

- Full-stack Ruby on Rails development
- High Availability deployment on EC2
- Javascript client/server event framework ([jelly](https://github.com/honkster/jelly))
- Chef scripts for server and workstation automation

### Pivotal Labs — Agile Engineer
**January 2006 – August 2009**

Agile Development in the XP tradition. TDD, Pair Programming, Daily Standups, Retrospectives. Worked with early startups to bootstrap their engineering process, team, and initial product. Leadership role in common code, practices, and open source.

Projects: Honk, Maven Link, KGB.com, Grockit, KDA Research, Real Girls Media, heavy.com, Bringo, CommunityWalk

Open source contributions:
- [Erector](https://github.com/pivotal/erector) — Ruby Builder and Widget framework for generating HTML
- [JS Test Server](https://github.com/pivotal/js-test-server) — organized Javascript TDD
- [Unison](https://github.com/grockit/unison) — relational algebra Ruby library with events

### Peer to Patent Project — Consultant
**2007**

Heavy lifter in launching the Peer to Patent pilot application, led by New York Law School. A tool to allow the crowd to review and submit prior art for pending patents.

### NASPP — IT Analyst
**February 2004 – January 2006**

- SQL Server DB Admin
- Developed internal CRM with Rails, .NET & MS Access
- Website ASP development
- Reports for Sales Trends and forecasting

### Flextronics — Web Application Developer Intern
**May 2001 – February 2002**

Develop corporate intranet using Microsoft technologies (ASP, SQL Server).

---

## Education

**University of the Pacific**
BS, Engineering Physics (1997 – 2002)

---

## Certifications

- Advanced Permaculture Course in Teaching
- Permaculture Design Certificate