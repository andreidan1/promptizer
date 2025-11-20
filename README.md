# 🚀 Promptizer

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ollama](https://img.shields.io/badge/ollama-supported-green.svg)](https://ollama.ai)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Convert simple text prompts into well-structured XML-formatted prompts using any local LLM via Ollama**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Troubleshooting](#-troubleshooting)

</div>

---

## 📋 Overview

Promptizer transforms your simple text prompts into sophisticated, structured XML prompts optimized for LLM interactions. By leveraging any model available in your local Ollama installation, it automatically generates prompts with:

- **System Role**: Defines the AI's expertise and perspective
- **Context**: Provides relevant background information  
- **Task Instructions**: Breaks down the task into clear steps
- **Formatting Rules**: Specifies output format requirements
- **Dataset**: Includes relevant sample data

This ensures more consistent, effective, and production-ready prompts for your LLM workflows.

## ✨ Features

- 🤖 **Universal LLM Support**: Works with any model available in Ollama (llama2, mistral, codellama, etc.)
- 🎯 **Smart Prompt Generation**: Automatically creates domain-specific XML prompts
- ⚡ **Lightweight**: Minimal dependencies, fast execution
- 🔧 **Flexible**: Choose your LLM model with simple flags
- 💾 **File Output**: Save generated prompts to files for reuse
- 🛡️ **Focused Generation**: Generates only content relevant to your prompt—no unrelated suggestions

## 📦 Prerequisites

- **Python 3.7+**
- **Ollama** installed and running ([installation guide](https://github.com/ollama/ollama))
- **At least one LLM model** pulled in Ollama

### Setting up Ollama

```bash
# Check available models
ollama list

# Pull the recommended model (gemma3:4b)
ollama pull gemma3:4b

# Or pull other models
ollama pull llama2        # Great for creative prompts
ollama pull codellama     # Best for code-related tasks
ollama pull mistral       # Fast and efficient
ollama pull neural-chat   # Optimized for conversations
```

## 🔧 Installation

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/promptizer.git
cd promptizer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Make the script executable (optional)
chmod +x promptizer.py
```

### Verify Installation

```bash
python promptizer.py --help
```

## 🚀 Usage

### Basic CLI Usage

```bash
python promptizer.py "Your simple text prompt here"
```

### Save to File

```bash
python promptizer.py "Your prompt" -o output.xml
```

### Streamlit Web UI

A simple web-based interface is included via Streamlit. Make sure your Ollama instance is running, then start the app with:

```bash
streamlit run app.py
```

By default, the app assumes Ollama is available at `http://localhost:11434` and uses the `gemma3:4b` model (configurable in the sidebar).

```bash
python promptizer.py "Your prompt" -o output.xml
```

### Use Different Models

```bash
# Default model (gemma3:4b)
python promptizer.py "Analyze user reviews"

# Specify a different model
python promptizer.py "Extract meeting notes" -m llama2
python promptizer.py "Code analysis task" -m codellama
python promptizer.py "Quick summary" -m mistral

# List available models
ollama list
```

### Command Line Options

```
Usage: promptizer.py [-h] [-m MODEL] [-o OUTPUT] prompt

Positional Arguments:
  prompt              The simple text prompt to convert to XML format

Optional Arguments:
  -h, --help          Show help message and exit
  -m, --model MODEL   Ollama model to use (default: gemma3:4b)
  -o, --output PATH   Save output to file
```

## 💡 Examples

### 1️⃣ Customer Feedback Analysis

```bash
python promptizer.py "Analyze user feedback for a new feature and identify common pain points"
```

**Generated Output**: Automatically creates an XML prompt with system role as a product analyst, context about the feature, task instructions for sentiment analysis, and sample review data.

### 2️⃣ Security Log Analysis

```bash
python promptizer.py "Analyze security logs to identify potential intrusion patterns and threats"
```

**Generated Output**: Creates a cybersecurity-focused XML prompt with threat detection instructions and relevant log examples.

### 3️⃣ Meeting Notes Extraction

```bash
python promptizer.py "Extract key decisions and action items from meeting notes" -o meeting_prompt.xml
```

**Generated Output**: Saves a focused XML prompt for meeting analysis with sample data.

### 4️⃣ Using Different Models

```bash
# Fast processing with Mistral
python promptizer.py "Summarize technical documentation" -m mistral

# Code-specific with CodeLlama
python promptizer.py "Generate prompts for code review tasks" -m codellama

# Creative with Llama2
python promptizer.py "Create marketing campaign analysis prompts" -m llama2
```

## How It Works

1. The script sends your prompt to Ollama along with a system prompt that explains the conversion task
2. The LLM generates a structured XML prompt based on your input
3. The XML includes:
   - `<system_role>`: Defines the AI's expertise
   - `<context>`: Provides background information
   - `<task_instructions>`: Lists specific steps for the task
   - `<formatting_rules>`: Specifies output format requirements
   - `<dataset>`: Contains sample data relevant to the task

## 🧠 Model Recommendations

| Model | Best For | Speed | Size |
|-------|----------|-------|------|
| **gemma3:4b** ⭐ | General use (default) | ⚡⚡⚡ | 3.3GB |
| **llama2** | Creative & complex tasks | ⚡⚡ | 3.8GB |
| **mistral** | Fast processing | ⚡⚡⚡⚡ | 4.4GB |
| **codellama** | Code-related prompts | ⚡⚡ | 3.3GB |
| **neural-chat** | Conversational tasks | ⚡⚡⚡ | 3.8GB |

**Recommended**: Start with `gemma3:4b` for the best balance of speed and quality.

## 🐛 Troubleshooting

### ❌ "Could not connect to Ollama"

```bash
# Ensure Ollama is running
ollama serve

# Or check if it's running on the default port
curl http://localhost:11434/api/tags
```

### ❌ Model Not Found

```bash
# List available models
ollama list

# Pull the missing model
ollama pull gemma3:4b
```

### ❌ Out of Memory Errors

Try using a smaller or more efficient model:

```bash
# Use a smaller model
ollama pull gemma3:1b  # 815MB
python promptizer.py "Your prompt" -m gemma3:1b

# Or use a faster model
python promptizer.py "Your prompt" -m mistral
```

### ❌ Slow Performance

- Use a faster model like `mistral`
- Ensure Ollama has sufficient system resources
- Check your system's available memory and CPU

## 📚 How It Works

1. You provide a simple text prompt
2. Promptizer sends it to your local Ollama instance
3. The LLM processes it with special instructions to maintain focus
4. An XML-formatted prompt is generated with:
   - Domain-specific system role
   - Relevant context
   - Clear task instructions
   - Formatting guidelines
   - Sample data
5. Output is displayed or saved to a file

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This software is released into the public domain under the Unlicense. See `LICENSE` for details.

## 💬 Support

Have questions? Please open an issue on GitHub.

---

<div align="center">

Made with ❤️ for the open-source community

</div>
