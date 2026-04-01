# Job Application Answers

---

# Why are you interested in working at Hightouch? - Hightouch, Backend Engineer (Control Plane)

Hightouch sits at an intersection I've been building toward for over a decade: agentic AI systems that operate on real data at enterprise scale. At Presence AI I architected a multi-service backend where AI agents, async pipelines, and human workflows had to coordinate reliably under real-time constraints - and the hardest problems weren't the models, they were the control plane: permissions, lifecycle management, scoped cancellation, and making the system legible to both humans and agents as it scaled. That's exactly what this role is about, and I find that deeply compelling.

Three things specifically stand out to me:

First, the Control Plane problems are the kind I gravitate toward. I built access-scoped context systems in corky (per-contact and per-topic agent context with role-based propagation), designed lazily-resolved dependency graphs with cascading invalidation at Presence AI, and spent 8 years at Censible building analyst portals where the right user saw the right data at the right granularity. Roles, permissions, and change management at data-warehouse scale is a natural extension of that work.

Second, I'm drawn to Hightouch's position at the intersection of agentic AI and cloud data infrastructure. My recent open source work - agent-doc, agent-kit, corky - is all about building reliable tooling where AI agents and humans collaborate on shared state. The challenge of helping enterprise admins manage downstream impact when data models change, or optimize warehouse costs as agent-driven marketing workflows scale, is exactly the kind of problem where my background in event-driven architecture and spec-driven development applies directly.

Third, the product-minded engineering culture resonates with how I work. At Pivotal Labs I mentored developers across 20+ startups by deeply engaging with product specs before writing code. At TrueCar, I partnered on the product vision that drove the honk.com acquisition. I'm most effective when I'm thinking holistically about architecture, customer impact, and maintainability together - not just shipping features.

I want to build the infrastructure layer that lets enterprise teams trust and scale their AI-powered marketing - and Hightouch is the company doing that.

---

# Which companies did you use Node.js/Express (or similar frameworks)? - Hightouch, Backend Engineer (Control Plane)

Presence AI (React, Node.js backend services), Censible (Node.js, SvelteJS), SocialChorus (Node.js, migrated Backbone to Svelte/React), CrystalCommerce (Node.js, Browserify), Rundavoo (Node.js, Browserify), Milyoni (Node.js, Backbone.js), TrueCar/honk.com (Node.js, Sinatra), and Pivotal Labs (Node.js across multiple client projects). I've also built extensively with similar server frameworks including FastAPI, Django, Flask (Python), and Ruby on Rails.

---

# How many years of professional experience do you have using Node.js? - Steno, Full-Stack Engineer

14 years. I've used Node.js professionally since 2012, starting at Milyoni and continuing through TrueCar, Rundavoo, CrystalCommerce, SocialChorus, Censible, and most recently at Presence AI.

---

# Why Steno, why now? - Steno, Full-Stack Engineer

I'm coming off Presence AI, where our investors wound down the project despite strong technical execution. That experience sharpened something for me: I want to build at a company where the product has real staying power - where customers depend on it for years, not months.

Steno fits that exactly. Legal cases take over a year to settle, which means the software has to be reliable, the relationships are long-term, and the work compounds. That's the kind of engineering I find most rewarding.

The timing is also right because Steno is at an inflection point I recognize. Transcript Genius signals you're bringing gen-AI into a domain where accuracy is non-negotiable - court reporting, legal transcripts, evidence. I've spent the last two years building production AI pipelines (real-time multimodal at Presence AI) and agent tooling in Rust (corky, agent-doc), so I know firsthand both the potential and the discipline required to ship AI that professionals actually trust. I want to bring that experience to a team that's scaling AI in a domain where getting it right genuinely matters.

---

# Why are you driven to work at Cleerly? - Cleerly, Engineer

At Presence AI I built real-time AI pipelines where the output had to be precise - facial landmark detection, lip-sync inference frame-by-frame, sub-100ms latency. But at the end of the day, a dropped frame in an avatar video is just a visual glitch. At Cleerly, that same class of problem - getting an AI model's output right on medical imaging - directly affects whether someone gets an invasive catheter procedure or a safe CT scan. That difference in stakes is what draws me.

I've spent two years building production multimodal pipelines on GPU infrastructure, and I understand the engineering discipline required when the model's accuracy isn't academic - it's the product. Cleerly is doing exactly that: replacing an invasive, risky procedure with AI-powered imaging that has to earn the trust of cardiologists and insurers alike. Building software where precision genuinely protects people is the most meaningful application of the skills I've developed, and I want to be part of scaling that.

---

# Cover Letter - HqO, Senior Software Engineer

Dear Hiring Team,

I'm writing to express my interest in the Senior Software Engineer position at HqO. Building a global platform that integrates thousands of service providers across 1800+ properties in 32 countries is precisely the kind of architectural challenge I've spent 20 years preparing for - and the opportunity to do it from the Greater Boston area, where I'm based, makes this an ideal fit.

**Platform scale and integration experience.** At Presence AI, I architected a multi-service TypeScript monorepo with 8 internal packages, real-time data pipelines, and GraphQL APIs connecting frontend, backend, and AI services. At Milyoni, I built a Social Entertainment Platform that integrated with Warner Brothers, Lions Gate, Paramount, Universal Music Group, and half a dozen other media companies - each with their own requirements and workflows. HqO's challenge of integrating thousands of service providers into a unified REX Platform is a natural extension of this work: designing flexible, multi-tenant systems where each integration has unique constraints but the platform experience stays consistent.

**Consumer + enterprise product development.** HqO serves both end-users and enterprise operators from the same platform - a dual-audience problem I know well. At TrueCar/honk.com, I built a consumer vehicle review platform and enterprise white-label product used by USAA and Wall Street Journal Autos simultaneously. At Censible, I built both a public-facing ESG analytics platform and a private Martin Investments analyst portal, each with distinct UX and data access requirements. I'm comfortable holding both audiences in mind while shipping.

**Mentorship and technical leadership.** At Pivotal Labs, I mentored developers across 20+ startups, bootstrapping their engineering process, team, and initial product. At Milyoni, I mentored junior and mid-level developers while serving as lead architect. At Presence AI, I defined the agentic development methodology adopted by the engineering team. The possibility of light leadership responsibilities alongside IC work is how I do my best - leading through code, specs, and pair collaboration rather than from a distance.

**Execution speed in early-stage environments.** I've spent most of my career at fast-moving startups where direct impact is the norm. I recently prototyped a full correspondence system in Python and rewrote it to production Rust in under a day using spec-driven development. I move quickly without sacrificing architectural thinking.

I'd welcome the chance to discuss how my experience building multi-tenant platforms, real-time systems, and cross-provider integrations can help HqO scale the REX Platform globally.

Best regards,
Brian Takita
Greater Boston, MA
btak.dev@gmail.com | linkedin.com/in/briantakita | github.com/btakita

---

# How will you contribute to our Core Purpose and BHAG? - HqO, Senior Software Engineer

HqO's core purpose is connecting real estate to people - making physical spaces work better through digital experience. My contribution would be architectural: I build the backend systems and integration layers that let platforms scale without breaking. At Presence AI I designed a multi-service monorepo where eight internal packages had to coordinate in real-time. At Milyoni I built a platform that served a dozen major entertainment studios, each with unique integration requirements. Scaling HqO's REX Platform across 32 countries and thousands of service providers is the same class of problem - and I'd bring both the technical depth and the product thinking to help HqO get there faster.

---

# How could you add value to HqO's customers? - HqO, Senior Software Engineer

HqO's customers are property operators who need their tenants to have a seamless experience across services, buildings, and providers. I'd add value by building reliable, performant integrations that just work - because that's what I've done repeatedly. At Censible, I built an analyst portal handling 10,000+ row exports and real-time ESG analytics that investment professionals depended on daily for 8 years. At TrueCar, I built the white-label platform that USAA and Wall Street Journal trusted with their auto customers. When operators and end-users both rely on the same system, the engineering has to be invisible - fast, correct, and available. That's what I focus on.

---

# Describe your A-player mindset and an example of how you have performed at an A-player level at some point in your life. - HqO, Senior Software Engineer

My A-player mindset is ownership end-to-end: I don't stop at "my code works" - I care whether the product ships, the team learns, and the architecture serves us six months from now.

The clearest example is Presence AI. I joined as the first backend engineer and within months had architected the entire real-time video avatar pipeline from scratch - facial landmark detection, lip-sync inference, frame sequencing on H100 GPUs via WebRTC. But the A-player part wasn't just the technical execution. I simultaneously defined the agentic development methodology the team adopted, built reusable async primitives that made the codebase comprehensible to both humans and AI agents, set up Grafana monitoring for GPU infrastructure, and mentored the team on spec-driven development. When the project wound down due to investor decisions, every system I built was documented, tested, and transferable. That's what ownership looks like to me - building as if the work has to outlast you.

---

# Describe in detail why HqO should consider hiring you. - HqO, Senior Software Engineer

Three reasons:

First, I've built exactly the kind of multi-tenant, cross-provider platform HqO is scaling. At Milyoni, I integrated a Social Entertainment Platform with Warner Brothers, Lions Gate, Paramount, Universal Music Group, and six other studios - each with different APIs, data formats, and requirements. At TrueCar, I built partner integrations for USAA and WSJ that had to pass enterprise security review. HqO's challenge of connecting thousands of service providers into a unified experience across 1800+ properties is architecturally familiar to me.

Second, I bring 20+ years of full-stack depth with a backend focus. TypeScript, Node.js, React, GraphQL, PostgreSQL, Docker, AWS, CI/CD - these are tools I use daily, not resume keywords. I've shipped production systems at every layer from GPU pipelines to frontend design systems.

Third, I combine IC execution with natural mentorship. At Pivotal Labs I mentored developers across 20+ startups. I was a speaker at RailsConf 2008. I've led through code, specs, and pairing my entire career. The role's mention of light leadership responsibilities alongside IC work is exactly how I operate best.

---

# What has been your favourite project or proudest accomplishment? Why? - HqO, Senior Software Engineer

My proudest accomplishment is corky, the git-native correspondence system I built in Rust. It syncs email, Telegram, and Slack into scoped markdown mailboxes with per-contact agent context, topic-based routing, Whisper-powered voice transcription, and bidirectional sync across providers.

What makes me proudest isn't the technical complexity - it's the process. I prototyped it in Python, validated the design, then rewrote it to production Rust in under a day using spec-driven development with AI agents. It's the culmination of a decade of work: my reactive programming frameworks (backbone-signal through ctx-core through rmemo), my context engineering system (existence-lang, 2014), and my agent tooling (agent-doc, agent-kit) all converge in this one project. I use it daily for all my professional correspondence.

It represents my belief that the best software comes from deep architectural thinking combined with rapid, disciplined execution - which is exactly what I'd bring to HqO.

---

# Name Pronunciation - General

Brian Takita (BRAH-ee-un tah-KEE-tah)

---

# How did you hear about Fleetio and what compelled you to apply? - Fleetio, Senior Software Engineer (Growth)

I found the role on LinkedIn. Two things compelled me to apply.

First, Fleetio is a founding member of the Rails Foundation - and Rails shaped my career. I spent 3.5 years at Pivotal Labs doing XP/TDD in Rails, was a speaker at RailsConf 2008, and contributed to core open source in the Rails ecosystem (RSpec, Erector, rr). Seeing a company at Fleetio's scale actively investing in the Rails community tells me something about the engineering culture.

Second, the Growth Engineering role specifically. I've spent years building onboarding and engagement experiences across different products - at Pivotal Labs I bootstrapped engineering processes for 20+ startups, which is fundamentally an onboarding problem. At Censible I built the ESG analytics platform where trial-to-retention was everything for a small team. The combination of experimentation, data-driven UX, and cross-functional collaboration is how I like to work.

---

# What project are you most proud of from your recent role? Why? - Fleetio, Senior Software Engineer (Growth)

At Presence AI, I'm most proud of the agentic development methodology I created and got the team to adopt. It wasn't the flashiest deliverable - we also shipped a real-time AI avatar pipeline on H100 GPUs - but the methodology had the most compounding impact.

The idea was lightweight living specs refined through closed-loop agent auditing: AI agents would review specs, flag inconsistencies, and suggest improvements, while humans stayed in the loop for design decisions. This accelerated our design velocity dramatically because the team could iterate on architecture and product specs before writing code, catching issues early instead of discovering them in PR review.

I'm proud of it because it changed how the entire team shipped - not just what I personally built. That's the kind of multiplier effect I'd want to bring to Fleetio's Growth team, where running experiments quickly and learning from the data is the whole game.

---

# Describe a recent project and how you used AI coding tools to complete it - Fleetio, Senior Software Engineer (Growth)

At Presence AI, I used Claude extensively as part of my daily backend engineering workflow. The most concrete example is how we built the real-time multimodal avatar pipeline.

I developed what I called a "closed-loop agentic workflow" - I'd write a lightweight living spec for a feature (say, the audio stream batching pipeline for Whisper feature extraction), then have Claude Code review the spec, flag edge cases I'd missed, and generate an initial implementation. I'd refine, test, and iterate - Claude handling the boilerplate and mechanical transformations while I focused on architecture decisions and integration points.

This wasn't just autocomplete. I built reusable async primitives - task lifecycle management, scoped cancellation, lazily resolved dependencies - and used Claude to help ensure these patterns were applied consistently across the 8-package TypeScript monorepo. The AI was particularly effective at propagating naming conventions and structural patterns across packages, which kept the codebase coherent as it grew quickly.

The methodology worked well enough that I formalized it: lightweight specs refined through agent auditing with continuous human-in-the-loop feedback. The whole engineering team adopted it. We shipped a production video pipeline on H100 GPUs in months with a small team - a pace that wouldn't have been possible without AI-augmented development at every stage.

After Presence AI, I took this further by building agent-doc (a document-as-interface tool for persistent AI sessions) and corky (a full correspondence system) - prototyping corky in Python and rewriting it to production Rust in under a day, entirely through spec-driven development with Claude.

---

# Years of Experience - General

- **Hands-on coding experience:** 24 years (2001 - present)
- **C#:** 3 years (NASPP, SafeSchoolz, Menu.com, Generic Query Analyzer)
- **T-SQL / SQL Server:** 3 years (NASPP, Flextronics)
- **JavaScript:** 20 years (2006 - present, across nearly every role)
- **React:** 8 years (Presence AI, Galler AI, SocialChorus, and others since ~2018)
- **Redis:** 3 years (Milyoni, TrueCar)
- **Svelte:** 6 years (Censible, SocialChorus, open source contributions to SvelteJS)
- **Node.js:** 14 years (2012 - present, Milyoni through Presence AI)

---

# Message to the Hiring Team - Otter Waiver, Full-Stack Engineer

Hi Otter team,

I'm a full-stack engineer with 20+ years of experience and I'm drawn to what you're building - a focused product that solves a real problem for businesses that most software companies ignore.

Your requirements read like a summary of my career: pixel-perfect frontend (I've done Figma-to-code implementation across multiple projects), multi-tenant backend architecture (I built platforms serving Warner Brothers, USAA, and dozens of other orgs with different access and data scoping), relational database design (15 years with PostgreSQL and SQL Server), and rapid prototyping that transitions to stable production (I recently prototyped a full system in Python and rewrote it to production Rust in under a day).

I'm particularly interested because Otter combines frontend craft with backend depth - waiver compliance, e-signature, marketing automation, and multi-tenant user management all in one product. That's the kind of full-lifecycle ownership I thrive on. I've spent 8 years at Censible building a similar all-in-one platform (analytics + compliance + reporting) for a niche industry, so I understand what it takes to serve smaller businesses with enterprise-grade quality.

Would love to chat about how I can help Otter ship faster and scale.

Brian Takita

