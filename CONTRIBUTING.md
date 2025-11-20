# Contributing to Promptizer

Thank you for your interest in contributing to Promptizer! We welcome contributions from the community to make this tool better for everyone.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create a new issue on GitHub and include:
1. A clear title and description
2. Steps to reproduce the issue
3. Your environment details (OS, Python version, Ollama version)
4. Any error messages or logs

### Suggesting Enhancements

Have an idea? We'd love to hear it! Open an issue to discuss your suggestion before you start working on it.

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature or fix (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes manually (see Testing section below)
5. Commit your changes with clear messages
6. Push to your branch
7. Open a Pull Request targeting the `main` branch

## 🧪 Testing

Before submitting a PR, please verify that the tool works correctly:

1. **Basic Test**:
   ```bash
   python promptizer.py "Test prompt"
   ```

2. **File Output Test**:
   ```bash
   python promptizer.py "Test prompt" -o test_output.xml
   ```

3. **Different Model Test** (if you have others installed):
   ```bash
   python promptizer.py "Test prompt" -m mistral
   ```

## 📝 Code Style

- Follow PEP 8 guidelines for Python code
- Keep the code clean and readable
- Add comments where necessary to explain complex logic

## ⚖️ License

By contributing, you agree that your contributions will be licensed under the MIT License.