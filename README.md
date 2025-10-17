# 🔐 Password Strength Checker

A Python-based tool to evaluate password strength using regex-based pattern detection and an entropy-based scoring system. It provides a strength score (0–100) and suggestions for improving weak passwords.

## 📘 Overview

The Password Strength Checker analyzes passwords for security by checking for common weak patterns (e.g., repetitive characters, predictable sequences) and calculating a strength score based on length, character variety, and entropy. It’s a great demonstration of regex, logical programming, and basic cybersecurity principles.

## ✨ Features

- **Weak Pattern Detection**: Identifies repetitive characters, sequential patterns, and common weak passwords using regex.
- **Strength Scoring**: Rates passwords on a 0–100 scale based on length, character diversity, and entropy.
- **Improvement Suggestions**: Provides actionable feedback for creating stronger passwords.
- **Secure Random Password Generation**: Uses `secrets` for generating strong password suggestions.

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **re**: For regular expression-based pattern matching.
- **string**: For character set management.
- **secrets**: For cryptographically secure random password generation.

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/bnsairam/password-strength-checker.git
   cd password-strength-checker
