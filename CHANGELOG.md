# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Notes
- （暂无）

## [1.0.0] - 2026-03-06

### Added
- 完整分析 Notebook（含 Z-test、置信区间、Bootstrap、功效分析、分层分析）
- 实验结论卡（experiment_summary.md）与核心发现/行动建议/风险说明
- 核心图表导出至 docs/figures/ 并在 README 中直接展示
- GitHub 仓库交付与可复现运行命令

## [0.1.0] - 2025-03-XX

### Added
- 初始化项目结构
- 创建 README 文档
- 创建数据字典（data_dictionary.md）
- 创建 A/B 测试工具函数库（ab_utils.py）
- 创建分析 Notebook 初版
- 创建实验结论卡（experiment_summary.md）
- 创建项目路线图（PROJECT_ROADMAP.md）
- 创建快速启动脚本（quick_start.sh）
- 添加 .gitignore 文件
- 添加 requirements.txt

### Project Structure
```
marketing_ab_testing/
├── README.md
├── CHANGELOG.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_marketing_ab_test.ipynb
├── src/
│   └── ab_utils.py
├── docs/
│   ├── data_dictionary.md
│   ├── experiment_summary.md
│   ├── PROJECT_ROADMAP.md
│   └── figures/
├── scripts/
│   └── quick_start.sh
└── results/
```

---

## 版本说明

- **[Unreleased]**: 正在开发中的功能
- **[0.1.0]**: 项目初始化，基础结构搭建完成
