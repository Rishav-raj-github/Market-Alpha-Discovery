# Contributing to Market-Alpha-Discovery

Thank you for considering contributing to Market-Alpha-Discovery! We welcome contributions from the community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How Can I Contribute?

### Reporting Bugs

- Check if the bug has already been reported in [Issues](https://github.com/Rishav-raj-github/Market-Alpha-Discovery/issues)
- If not, create a new issue with:
  - Clear, descriptive title
  - Detailed description of the issue
  - Steps to reproduce
  - Expected vs actual behavior
  - Screenshots if applicable

### Suggesting Enhancements

- Open an issue describing:
  - The enhancement you'd like to see
  - Why it would be useful
  - Possible implementation approaches

### Contributing Code

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Write or update tests as needed
5. Ensure all tests pass
6. Commit your changes (see commit guidelines below)
7. Push to your fork
8. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/Market-Alpha-Discovery.git
cd Market-Alpha-Discovery

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
```

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Update the CHANGELOG.md with your changes
3. Ensure your code follows the style guidelines
4. Make sure all tests pass
5. Link any related issues in your PR description
6. Request review from maintainers
7. Address any feedback from reviewers

## Style Guidelines

### Python Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use meaningful variable and function names
- Write docstrings for all functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Code Formatting

- Use `black` for code formatting: `black .`
- Use `flake8` for linting: `flake8 .`
- Maximum line length: 88 characters (black default)

### Testing

- Write unit tests for new features
- Maintain or improve code coverage
- Use pytest for testing
- Test files should be in the `tests/` directory

## Commit Message Guidelines

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>: <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```
feat: Add sentiment analysis feature

Implements sentiment analysis using VADER for news articles
to enhance alpha discovery signals.

Closes #123
```

```
fix: Resolve data normalization issue

Fixes incorrect normalization in preprocessing step that was
causing skewed results.
```

## Questions?

Feel free to open an issue for any questions or join discussions in existing issues.

Thank you for contributing! 🎉
