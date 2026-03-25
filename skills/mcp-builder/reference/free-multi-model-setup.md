# Free Multi-Model Collaboration Setup

## 免费模型推荐 (2026)

### 1. Google Gemini (推荐 - 无需信用卡)
| 模型 | 限制 | 特点 |
|------|------|------|
| gemini-2.0-flash-exp | 10 RPM, 250 RPD | 最新最快 |
| gemini-2.5-flash | 15 RPM, 1000 RPD | 稳定版 |
| gemini-2.5-flash-lite | 15 RPM, 1000 RPD | 最便宜 |

**获取API Key**: https://aistudio.google.com/app/apikey

### 2. Groq (免费高速)
| 模型 | 限制 | 特点 |
|------|------|------|
| llama-3.3-70b-versatile | 30 RPM | 最强免费模型 |
| llama-3.1-8b-instant | 30 RPM | 快速响应 |
| mixtral-8x7b-32768 | 30 RPM | MoE架构 |

**获取API Key**: https://console.groq.com/keys

### 3. Ollama (本地完全免费)
| 模型 | 内存要求 | 特点 |
|------|----------|------|
| qwen2.5:14b | ~10GB | 中文优化 |
| llama3.1:8b | ~6GB | 通用 |
| codellama:7b | ~6GB | 代码专用 |
| deepseek-r1:14b | ~10GB | 推理能力强 |

**安装**: https://ollama.com/download

### 4. OpenRouter (聚合多个免费模型)
| 模型 | 限制 | 特点 |
|------|------|------|
| google/gemini-2.0-flash | 多种免费模型 | 聚合平台 |

**获取API Key**: https://openrouter.ai/keys

## 环境变量配置

```bash
# 创建环境变量文件
cat >> ~/.zshrc << 'EOF'

# Free AI API Keys
export GEMINI_API_KEY="your-gemini-api-key"
export GROQ_API_KEY="gsk_xxxxx"
export OPENROUTER_API_KEY="sk-or-xxxxx"
EOF

# 重新加载
source ~/.zshrc
```

## 配置文件

已创建 `~/.opencode/opencode.json`:

```json
{
  "providers": {
    "google": { "apiKey": "${GEMINI_API_KEY}" },
    "groq": {
      "baseURL": "https://api.groq.com/openai/v1",
      "apiKey": "${GROQ_API_KEY}"
    },
    "ollama": {
      "baseURL": "http://localhost:11434/v1",
      "apiKey": "ollama"
    }
  },
  "model": "google/gemini-2.0-flash-exp",
  "agents": {
    "coder": {
      "model": "google/gemini-2.0-flash-exp",
      "temperature": 0.3
    },
    "researcher": {
      "model": "groq/llama-3.3-70b-versatile",
      "temperature": 0.5
    },
    "reviewer": {
      "model": "google/gemini-2.0-flash-exp",
      "temperature": 0.2
    }
  },
  "fallback": [
    "groq/llama-3.3-70b-versatile",
    "google/gemini-2.0-flash-exp",
    "ollama/qwen2.5:14b"
  ]
}
```

## 快速开始

### 1. 获取免费API Key

```bash
# Google Gemini (最简单，无需信用卡)
open https://aistudio.google.com/app/apikey

# Groq (30 RPM高速)
open https://console.groq.com/keys
```

### 2. 安装 Ollama (可选，本地模型)

```bash
# macOS
brew install ollama

# 启动服务
ollama serve

# 下载模型
ollama pull qwen2.5:14b
ollama pull codellama:7b
```

### 3. 验证配置

```bash
# 检查配置
opencode doctor

# 测试模型
opencode models list
```

## 模型使用策略

| 任务类型 | 推荐模型 | 原因 |
|----------|----------|------|
| 日常编码 | Gemini 2.0 Flash | 免费、快速 |
| 复杂推理 | Groq Llama 3.3 70B | 高速、大上下文 |
| 代码审查 | Gemini Flash | 免费、快速 |
| 本地隐私 | Ollama Qwen | 完全离线 |
| 研究搜索 | Groq Llama | 免费高速 |

## Rate Limit 应对策略

1. **多Provider轮换**: 配置多个免费Provider
2. **本地Ollama备份**: 完全不受限
3. **错峰使用**: 避开高峰时段
4. **缓存常用响应**: 减少重复调用

## 完整免费方案推荐

```
主模型: Google Gemini 2.0 Flash (免费)
备选1: Groq Llama 3.3 70B (高速免费)
备选2: Ollama Qwen 2.5 (本地完全免费)
```

## 帮助命令

```bash
# 查看所有可用命令
opencode --help

# 诊断配置问题
opencode doctor

# 列出模型
opencode models

# 切换模型
opencode model set groq/llama-3.3-70b-versatile
```
