# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### 待完成
- 下载并加载数据集
- 完成数据探索与质量检查
- 完成统计推断分析
- 完成分层分析
- 填写实验结论卡

## [0.1.0] - 2025-03-XX

### Added
- 初始化项目结构
- 创建 README 文档
- 创建数据字典（data_dictionary.md）
- 创建 A/B 测试工具函数库（ab_utils.py）
- 创建分析 Notebook 模板
- 创建实验结论卡模板（experiment_summary.md）
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
