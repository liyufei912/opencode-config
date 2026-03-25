# OpenCode 本地免费模型多模型协同

## OpenCode 免费模型列表

| 模型 | 模型ID | 特点 |
|------|--------|------|
| **MiniMax M2.5 Free** | `minimax-m2.5-free` | 最强免费模型，SWE-bench 80%+ |
| **MiMo V2 Pro Free** | `mimo-v2-pro-free` | 中文优化，多模态 |
| **MiMo V2 Omni Free** | `mimo-v2-omni-free` | 全能型，免费期收集反馈 |
| **Nemotron 3 Super Free** | `nemotron-3-super-free` | NVIDIA模型，稳定 |
| **Big Pickle** | `big-pickle` | 神秘模型，完全免费 |
| **GPT 5 Nano** | `gpt-5-nano` | OpenAI官方免费 |

## 已配置的多模型协同

### Primary Agents (主智能体)

| Agent | 模型 | 用途 | 权限 |
|-------|------|------|------|
| **build** | minimax-m2.5-free | 主要编码任务 | 全部开启 |
| **plan** | mimo-v2-pro-free | 分析和规划 | edit/bash 需确认 |

### Subagents (子智能体)

| Agent | 模型 | 用途 | 调用方式 |
|-------|------|------|----------|
| **researcher** | big-pickle | 网络搜索和研究 | @researcher |
| **reviewer** | gpt-5-nano | 代码审查 | @reviewer |
| **debugger** | minimax-m2.5-free | 调试和问题排查 | @debugger |

### 配置文件位置

- **JSON配置**: `~/.opencode/opencode.json`
- **Markdown Agents**: `~/.config/opencode/agents/*.md`

### JSON配置示例

```json
{
  "model": "opencode/minimax-m2.5-free",
  "agent": {
    "build": {
      "mode": "primary",
      "model": "opencode/minimax-m2.5-free",
      "temperature": 0.3
    },
    "plan": {
      "mode": "primary",
      "model": "opencode/mimo-v2-pro-free",
      "temperature": 0.2
    },
    "researcher": {
      "mode": "subagent",
      "model": "opencode/big-pickle",
      "temperature": 0.5
    },
    "reviewer": {
      "mode": "subagent",
      "model": "opencode/gpt-5-nano",
      "temperature": 0.2
    },
    "debugger": {
      "mode": "subagent",
      "model": "opencode/minimax-m2.5-free",
      "temperature": 0.1
    }
  }
}
```

## 模型使用策略

| 任务类型 | 推荐Agent | 模型 | 原因 |
|----------|-----------|------|------|
| 日常编码 | build | minimax-m2.5-free | 最强免费编码模型 |
| 分析规划 | plan | mimo-v2-pro-free | 中文优化 |
| 网络搜索 | researcher | big-pickle | 完全免费 |
| 代码审查 | reviewer | gpt-5-nano | OpenAI官方，快速 |
| 调试排查 | debugger | minimax-m2.5-free | 详细分析 |

## OpenCode Zen 免费模型定价

| 模型 | 输入 | 输出 | 缓存读 | 缓存写 |
|------|------|------|--------|--------|
| Big Pickle | Free | Free | Free | - |
| MiMo V2 Pro Free | Free | Free | Free | - |
| MiMo V2 Omni Free | Free | Free | Free | - |
| Nemotron 3 Super Free | Free | Free | Free | - |
| MiniMax M2.5 Free | Free | Free | Free | - |
| GPT 5 Nano | Free | Free | Free | - |

## 使用方法

### 1. 查看可用模型
```bash
opencode /models
```

### 2. 切换模型
```bash
opencode /model opencode/minimax-m2.5-free
```

### 3. 多模型协同
```bash
opencode /agent coder    # 使用 coder agent
opencode /agent researcher  # 使用 researcher agent
opencode /agent reviewer  # 使用 reviewer agent
```

### 4. 查看配置
```bash
opencode /config
```

## 注意事项

1. **免费期限制**: 免费模型是限时提供的，团队用这段时间收集反馈来改进模型
2. **数据使用**: 部分免费模型（Big Pickle, MiniMax M2.5 Free, MiMo V2等）在免费期内可能会收集数据用于模型改进
3. **隐私**: 所有付费模型都遵循零保留政策，不会用于模型训练
4. **自动切换**: 当主模型不可用时，会自动切换到 fallback 列表中的模型

## 获取更多信息

- [OpenCode Zen 文档](https://opencode.ai/docs/zen/)
- [模型列表 API](https://opencode.ai/zen/v1/models)
