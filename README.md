https://github.com/Ibrahim3laa93/e_websearch/releases

[![Releases](https://img.shields.io/badge/Releases-latest-blue.svg)](https://github.com/Ibrahim3laa93/e_websearch/releases)

# e_websearch — Lightweight CLI Web Search, Scraper, and API

![Search illustration](https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=1200&q=80)

A compact command-line web search tool that queries multiple sources, extracts structured results, and exposes a small HTTP API for automation. Use it for research, monitoring, and data extraction. It runs on Linux, macOS, and Windows. It supports JSON and CSV exports, result filtering, and headless scraping.

Badges
- License: MIT
- Platform: Linux / macOS / Windows
- Releases: [Download latest release](https://github.com/Ibrahim3laa93/e_websearch/releases)

Features
- Multi-source search: Combine results from Google-like engines, Bing, DuckDuckGo, and site-specific queries.
- Fast scraping: Headless browser scraping for JavaScript-heavy pages.
- Structured output: JSON, CSV, plain text.
- Local API: Start a small web server and query results programmatically.
- Filters: Domain allowlist/blocklist, date range, language.
- Caching: Local cache to speed repeated queries.
- Rate control: Built-in throttling to reduce server load.
- Extensible: Plugin hooks for custom parsers and result processors.

Why use e_websearch
- It gives direct CLI control over web searches.
- It exposes results as structured data for pipelines.
- It runs offline after a query completes.
- It uses standard formats so you can integrate with tools and scripts.

Get the binary
Download the release asset from the Releases page and execute it. Use the link below to fetch the file you need. Follow the platform section for command examples.

https://github.com/Ibrahim3laa93/e_websearch/releases

Install (binaries)
Linux / macOS (example)
1. Visit the Releases page and download the correct asset for your OS.
2. Give execute permission and run.

Example commands (replace asset name with the real file on the release page):
```bash
curl -L -o e_websearch.tar.gz "https://github.com/Ibrahim3laa93/e_websearch/releases/download/v1.0/e_websearch-linux-x64.tar.gz"
tar -xzf e_websearch.tar.gz
chmod +x e_websearch
./e_websearch --help
```

Windows (example)
- Download the .zip from the Releases page.
- Extract and run e_websearch.exe from PowerShell or Command Prompt.

Install (from source)
- Clone the repo
```bash
git clone https://github.com/Ibrahim3laa93/e_websearch.git
cd e_websearch
# build steps (example)
make build
./bin/e_websearch --help
```

Usage examples
- Basic search
```bash
./e_websearch "open source privacy tools"
```

- Limit to a site
```bash
./e_websearch "site:example.com authentication" --max 50
```

- Export JSON
```bash
./e_websearch "best CLI tools" --format json --output results.json
```

- CSV export
```bash
./e_websearch "security news" --format csv --output results.csv
```

- Headless scrape (fetch rendered content)
```bash
./e_websearch "dynamic article example" --render --max 10
```

- Start the local API
```bash
./e_websearch --server --port 8080
# Then query
curl "http://localhost:8080/search?q=privacy+tools&format=json"
```

Command line flags (core)
- --help: Show help.
- --max N: Max results per query (default 20).
- --format [json|csv|text]: Output format.
- --output PATH: Save output to file.
- --render: Use headless browser to render pages before extraction.
- --server: Start HTTP API server.
- --port N: API server port.
- --allow-domain DOMAIN: Allow only this domain.
- --block-domain DOMAIN: Block this domain.
- --cache-dir PATH: Use a directory for cache.
- --throttle MS: Milliseconds between requests.

Configuration
Create a YAML config file to set defaults and API keys for third-party services.

Example config (~/.e_websearch/config.yml)
```yaml
default_max: 30
format: json
cache_dir: ~/.e_websearch/cache
throttle_ms: 250
user_agent: "e_websearch/1.0 (+https://github.com/Ibrahim3laa93/e_websearch)"
engines:
  - duckduckgo
  - bing
  - google_serp_api
api_keys:
  google_serp_api: YOUR_KEY_HERE
```

Integration
- Pipes: Output JSON to jq or CSV to spreadsheet import.
```bash
./e_websearch "privacy updates" --format json | jq '.results[] | {title,link}'
```
- CI: Run searches in scheduled jobs and store artifacts.
- Alerts: Combine with a small script to send email when keywords appear.

Advanced scraping
- Set a selector to extract a specific piece of content:
```bash
./e_websearch "site:example.com guide" --selector ".article-body p" --format text
```
- Use custom parser plugin (drop a script in plugins/)
- Apply post-processing filters with a small Python or Node script.

API details
When you run with --server the tool exposes a small REST API.

Endpoints
- GET /search?q=QUERY&format=json&max=20
- GET /status
- POST /config (update runtime config)

Example:
```bash
curl "http://localhost:8080/search?q=cli+tools&format=json&max=10"
```

Response (JSON)
- results: list of result objects
- meta: query metadata (elapsed_ms, engine_breakdown)

Result object
- title: string
- link: string
- snippet: string
- source: engine name
- published: ISO date if available
- content: full extracted text when requested

Security and privacy
- The tool stores minimal metadata by default.
- You can enable or disable cache using --cache-dir or set it to /dev/null.
- You control which domains to query and which to block via command options.

Performance tips
- Use cache for repeated queries.
- Increase throttle when you hit remote rate limits.
- Use --max to limit the number of results.

Testing
- Unit tests live in tests/
- Run the test suite:
```bash
make test
```

Contributing
- Fork the repo.
- Create a branch with a short name and a clear purpose.
- Add tests for new features.
- Open a pull request with a description of changes and examples.
- Follow the code style in tools/format.

Changelog
- See releases for tagged changes and binaries: https://github.com/Ibrahim3laa93/e_websearch/releases
- Each release includes assets to download and run.

License
- MIT License. See LICENSE file.

Acknowledgments
- Thanks to open-source projects that inspired the design: headless browser drivers, HTTP clients, and JSON tooling.
- Images used in this README come from Unsplash.

Common questions (FAQ)
- How do I get the binary?
  - Download the asset from the Releases page and execute it.
- What platforms run this?
  - Linux, macOS, Windows.
- Can I add new search engines?
  - Yes. Add an engine module in engines/ and register it in config.

Releases and downloads
- Visit the Releases page to find prebuilt binaries and archives. Download the asset that matches your OS and architecture. After download, extract and run the executable. The Releases page contains signed assets for key versions and the full release notes.

Links
- Releases: https://github.com/Ibrahim3laa93/e_websearch/releases
- Repo: https://github.com/Ibrahim3laa93/e_websearch
- Issues: https://github.com/Ibrahim3laa93/e_websearch/issues