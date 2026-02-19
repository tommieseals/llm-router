# 🚀 LLM Router

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/tommieseals/llm-router/actions/workflows/ci.yml/badge.svg)](https://github.com/tommieseals/llm-router/actions)

**Intelligent routing for LLM requests across multiple providers and local nodes.**

## The Problem

Running multiple LLMs (local Ollama, cloud APIs) means manually deciding:
- Which model for which task?
- What if my preferred provider is down?
- How do I stay within rate limits?
- How do I minimize costs?

## The Solution

LLM Router automatically routes your requests to the best available model based on:

- **Task type** (code → deepseek, fast → phi3, research → perplexity)
- **Node health** (auto-failover if a node is down)
- **Cost optimization** (prefer free tiers, local first)
- **Usage tracking** (respect daily limits)

## Architecture

\\
┌─────────────┐
│  Your App   │
└──────┬──────┘
       │
       ▼
┌──────────────────────────────────┐
│         LLM Router               │
│  ┌─────────────────────────┐     │
│  │  Task Classification    │     │
│  │  • code → deepseek      │     │
│  │  • fast → phi3          │     │
│  │  • research → perplexity│     │
│  └───────────┬─────────────┘     │
│              │                   │
│  ┌───────────▼─────────────┐     │
│  │   Health Checker        │     │
│  │   • Node availability   │     │
│  │   • Latency monitoring  │     │
│  └───────────┬─────────────┘     │
│              │                   │
│  ┌───────────▼─────────────┐     │
│  │   Usage Tracker         │     │
│  │   • Daily limits        │     │
│  │   • Cost tracking       │     │
│  └─────────────────────────┘     │
└──────────────┬───────────────────┘
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
┌───────┐ ┌────────┐ ┌─────────┐
│Ollama │ │ Cloud  │ │Fallback │
│Nodes  │ │ APIs   │ │ Node    │
└───────┘ └────────┘ └─────────┘
\\

## Quick Start

### One-Command Install

\\ash
pip install llm-router
\\

### From Source

\\ash
git clone https://github.com/tommieseals/llm-router.git
cd llm-router
pip install -e .
\\

### Usage

\\python
from llm_router import Router

router = Router()

# Auto-routes to best model
response = router.query(" Write a Python function to sort a list) # Force specific task type response = router.query(Explain recursion, task=reasoning) # Check node health health = router.check_health() print(health) \\\ ### CLI \\\ash # Simple query llm-router What is the capital of France?\ # Code task (routes to code-specialized model) llm-router --task code Write a binary search in Python\ # Check health of all nodes llm-router --health # View usage stats llm-router --usage \\\ ## Configuration Create a \.env\ file or set environment variables: \\\ash # Local Ollama nodes OLLAMA_PRIMARY_URL=http://localhost:11434 OLLAMA_FALLBACK_URL=http://192.168.1.100:11434 # Cloud providers (optional) NVIDIA_API_KEY=your-key OPENROUTER_API_KEY=your-key PERPLEXITY_API_KEY=your-key # Limits NVIDIA_DAILY_LIMIT=50 \\\ ## Supported Providers | Provider | Models | Cost | Use Case | |----------|--------|------|----------| | Ollama (local) | Any | Free | General, fast queries | | NVIDIA NIM | Kimi K2.5, Llama | Free tier | Multimodal, reasoning | | OpenRouter | 100+ models | Pay-per-use | Fallback, variety | | Perplexity | Sonar | Pay-per-use | Web search, research | ## Task Routing Rules | Task | Primary | Fallback | |------|---------|----------| | code, debug | deepseek-coder | qwen-coder | | fast, simple | phi3:mini | tinyllama | | reasoning | qwen2.5:7b | gpt-4o-mini | | research | perplexity | openrouter | | multimodal | kimi | llava | ## License MIT License - see [LICENSE](LICENSE) ## Contributing PRs welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. READMEEOF cat ~/llm-router/README.md | head -20