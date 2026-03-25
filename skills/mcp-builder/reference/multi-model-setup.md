# Multi-Model Collaboration Setup Guide

## Overview

OpenCode supports multi-model collaboration, allowing you to configure multiple AI providers and specialized agents that work together.

## Configuration File Location

- **Global**: `~/.opencode/opencode.json`
- **Project-specific**: `./opencode.json` (in your project directory)

## Basic Configuration

```json
{
  "$schema": "https://opencode.ai/config.json",
  "providers": {
    "anthropic": {
      "apiKey": "${ANTHROPIC_API_KEY}"
    },
    "openai": {
      "apiKey": "${OPENAI_API_KEY}"
    },
    "google": {
      "apiKey": "${GOOGLE_API_KEY}"
    },
    "ollama": {
      "baseURL": "http://localhost:11434/v1",
      "apiKey": "ollama"
    }
  }
}
```

## Environment Variables

Set your API keys in environment variables:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
export GOOGLE_API_KEY="AIza..."
```

## Multi-Agent Setup

Configure specialized agents for different tasks:

```json
{
  "model": "anthropic/claude-3-5-sonnet-20241022",
  "agents": {
    "coder": {
      "description": "Primary coding agent",
      "model": "anthropic/claude-3-5-sonnet-20241022",
      "temperature": 0.3,
      "maxTokens": 8192
    },
    "researcher": {
      "description": "Research agent for web search",
      "model": "openai/gpt-4o-mini",
      "temperature": 0.5
    },
    "reviewer": {
      "description": "Code review agent",
      "model": "anthropic/claude-3-5-haiku-20241022",
      "temperature": 0.2
    }
  },
  "fallback": [
    "openai/gpt-4o",
    "google/gemini-1.5-flash"
  ]
}
```

## Model Priority & Fallback

Define fallback models when primary is unavailable:

```json
{
  "model": "anthropic/claude-3-5-sonnet-20241022",
  "fallback": [
    "openai/gpt-4o",
    "google/gemini-1.5-pro",
    "ollama/llama3.1:8b"
  ]
}
```

## Available Model Formats

### Anthropic
- `anthropic/claude-opus-4-20250514`
- `anthropic/claude-3-5-sonnet-20241022`
- `anthropic/claude-3-5-haiku-20241022`

### OpenAI
- `openai/gpt-4o`
- `openai/gpt-4o-mini`
- `openai/gpt-4-turbo`

### Google
- `google/gemini-1.5-pro`
- `google/gemini-1.5-flash`
- `google/gemini-2.0-flash-exp`

### Ollama (Local)
- `ollama/llama3.1:8b`
- `ollama/llama3.1:70b`
- `ollama/codellama:7b`
- `ollama/qwen2.5:14b`

## Quick Setup Commands

```bash
# Create config directory
mkdir -p ~/.opencode

# Edit configuration
vim ~/.opencode/opencode.json

# Check configuration
opencode doctor

# List available models
opencode models list
```

## Multi-Agent Collaboration Example

With the multi-agent setup, agents can collaborate:

1. **Coder**: Writes initial code implementation
2. **Researcher**: Looks up documentation and APIs
3. **Reviewer**: Analyzes code quality and suggests improvements

When one agent needs help, it can delegate to another specialized agent.

## Tips

- Use `temperature: 0.2-0.3` for coding tasks (more deterministic)
- Use `temperature: 0.5-0.7` for creative/research tasks
- Set `maxTokens` based on expected response length
- Configure fallback models to avoid interruptions during rate limits
