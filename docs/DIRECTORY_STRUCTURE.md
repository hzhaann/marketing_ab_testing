# 目录结构说明

## 完整目录树

```
marketing_ab_testing/
├── README.md                          # 项目主文档
├── CHANGELOG.md                       # 版本更新日志
├── requirements.txt                   # Python 依赖包列表
├── .gitignore                         # Git 忽略文件配置
│
├── data/                              # 数据目录
│   ├── raw/                          # 原始数据（不提交到 Git）
│   │   └── .gitkeep                  # 占位文件 + 数据下载说明
│   └── processed/                    # 处理后的数据
│       └── .gitkeep                  # 占位文件
│
├── notebooks/                         # Jupyter Notebooks
│   └── 01_marketing_ab_test.ipynb   # 完整分析流程
│
├── src/                              # 源代码
│   └── ab_utils.py                  # A/B 测试工具函数库
│
├── docs/                             # 文档目录
│   ├── data_dictionary.md           # 数据字典
│   ├── experiment_summary.md        # 实验结论卡
│   ├── PROJECT_ROADMAP.md           # 项目路线图
│   ├── RESUME_TEMPLATE.md           # 简历写法参考
│   ├── DIRECTORY_STRUCTURE.md       # 本文件
│   ├── figures/                     # 图表输出
│   │   └── .gitkeep
│   └── screenshots/                 # 截图（可选）
│
├── scripts/                          # 脚本目录
│   └── quick_start.sh               # 快速启动脚本
│
└── results/                          # 分析结果
    └── .gitkeep                      # 占位文件
```

## 目录说明

### 根目录文件

#### README.md
- **用途**: 项目主文档，GitHub 首页展示
- **内容**: 项目概述、技术栈、快速开始、核心发现
- **受众**: GitHub 访问者、招聘方

#### CHANGELOG.md
- **用途**: 记录项目版本更新历史
- **内容**: 每个版本的新增功能、修改、修复
- **更新频率**: 每次重要更新后

#### requirements.txt
- **用途**: Python 依赖包列表
- **使用**: `pip install -r requirements.txt`
- **维护**: 添加新依赖时及时更新

#### .gitignore
- **用途**: 指定 Git 不跟踪的文件
- **内容**: 数据文件、缓存、IDE 配置等

### data/ - 数据目录

#### data/raw/
- **用途**: 存放原始数据文件
- **文件**: `marketing_AB.csv`（从 Kaggle 下载）
- **注意**: 
  - 不提交到 Git（已在 .gitignore 中排除）
  - 在 .gitkeep 中提供下载说明

#### data/processed/
- **用途**: 存放清洗和处理后的数据
- **可能包含**:
  - `cleaned_data.csv`: 清洗后的完整数据
  - `stratified_data.csv`: 分层分析数据
  - `summary_stats.csv`: 汇总统计数据

### notebooks/ - 分析 Notebook

#### 01_marketing_ab_test.ipynb
- **用途**: 完整的 A/B 测试分析流程
- **内容**:
  1. 数据加载与探索
  2. 数据质量检查
  3. 指标定义与计算
  4. 统计推断
  5. Practical Significance 评估
  6. 分层分析
  7. 结论与建议
- **运行**: `jupyter notebook notebooks/01_marketing_ab_test.ipynb`

### src/ - 源代码

#### ab_utils.py
- **用途**: A/B 测试工具函数库
- **包含函数**:
  - `calculate_conversion_rate()`: 计算转化率
  - `proportion_z_test()`: 两样本比例 Z 检验
  - `confidence_interval_proportion()`: 置信区间计算
  - `bootstrap_confidence_interval()`: Bootstrap 置信区间
  - `calculate_effect_size()`: 效应量计算
  - `sample_size_calculation()`: 样本量计算
  - `check_sample_ratio_mismatch()`: SRM 检查
  - `practical_significance_check()`: 业务意义检查
  - `stratified_analysis()`: 分层分析
- **使用**: 在 Notebook 中 `from ab_utils import *`

### docs/ - 文档目录

#### data_dictionary.md
- **用途**: 数据字典，说明每个字段的含义
- **内容**:
  - 字段说明
  - 数据类型
  - 取值范围
  - 业务含义
  - 核心指标定义

#### experiment_summary.md
- **用途**: 实验结论卡，一页纸总结
- **内容**:
  - 实验概述
  - 核心指标
  - 统计推断结果
  - Practical Significance 评估
  - 分层分析
  - 核心发现（Top 3）
  - 行动建议（Top 2）
  - 风险与限制

#### PROJECT_ROADMAP.md
- **用途**: 项目路线图，指导项目推进
- **内容**:
  - 项目目标
  - 推进计划（Day 1-5）
  - 最低完成标准（MVP）
  - 面试准备清单
  - 常见问题与解决方案

#### RESUME_TEMPLATE.md
- **用途**: 简历写法参考
- **内容**:
  - 完整版简历描述
  - 精简版简历描述
  - 面试自证清单
  - 必须能回答的问题
  - 量化结果写法参考

#### DIRECTORY_STRUCTURE.md
- **用途**: 本文件，说明目录结构
- **内容**: 每个目录和文件的用途

#### figures/
- **用途**: 存放分析过程中生成的图表
- **可能包含**:
  - 转化率对比图
  - 置信区间可视化
  - 分层分析图表
  - Bootstrap 分布图

#### screenshots/
- **用途**: 存放项目截图（可选）
- **用途**: 用于 README 或报告

### scripts/ - 脚本目录

#### quick_start.sh
- **用途**: 快速启动脚本，自动化环境配置
- **功能**:
  - 检查 Python 版本
  - 创建虚拟环境
  - 安装依赖包
  - 创建必要目录
- **使用**: `bash scripts/quick_start.sh`

### results/ - 分析结果

- **用途**: 存放最终的分析结果文件
- **可能包含**:
  - 统计检验结果表格
  - 分层分析结果
  - 最终报告的数据支撑文件

## 文件命名规范

### Notebook 命名
- 格式: `{序号}_{描述}.ipynb`
- 示例: `01_marketing_ab_test.ipynb`
- 规则: 
  - 序号用两位数（01, 02, ...）
  - 描述用小写字母和下划线

### 数据文件命名
- 格式: `{描述}_{日期}.csv`
- 示例: `cleaned_data_20250315.csv`
- 规则:
  - 描述清晰
  - 包含日期（如果有版本）

### 图表文件命名
- 格式: `{类型}_{描述}.png`
- 示例: `bar_conversion_rate_comparison.png`
- 规则:
  - 类型：bar, line, scatter, heatmap 等
  - 描述清晰

## Git 提交规范

### 不提交的文件
- 原始数据文件（`data/raw/*.csv`）
- 处理后的数据文件（`data/processed/*.csv`）
- 虚拟环境（`venv/`）
- IDE 配置（`.vscode/`, `.idea/`）
- 系统文件（`.DS_Store`, `Thumbs.db`）

### 提交的文件
- 代码文件（`.py`, `.ipynb`）
- 文档文件（`.md`）
- 配置文件（`requirements.txt`, `.gitignore`）
- 脚本文件（`.sh`）
- 占位文件（`.gitkeep`）

## 项目扩展建议

### 如果要添加新功能

1. **新的分析维度**
   - 在 Notebook 中添加新的 Section
   - 更新 experiment_summary.md

2. **新的工具函数**
   - 在 `src/ab_utils.py` 中添加
   - 添加函数文档字符串
   - 添加单元测试（可选）

3. **新的可视化**
   - 在 Notebook 中创建
   - 保存到 `docs/figures/`
   - 在 README 中引用

4. **新的文档**
   - 在 `docs/` 中创建新的 .md 文件
   - 在 README 中添加链接

## 维护建议

### 定期更新
- [ ] 每次分析后更新 CHANGELOG.md
- [ ] 完成分析后填写 experiment_summary.md
- [ ] 添加新依赖后更新 requirements.txt
- [ ] 生成新图表后更新 README

### 代码质量
- [ ] 保持代码注释清晰
- [ ] 函数添加文档字符串
- [ ] Notebook 添加 Markdown 说明
- [ ] 定期清理无用代码

### 文档质量
- [ ] 保持文档与代码同步
- [ ] 及时更新发现和结论
- [ ] 检查链接是否有效
- [ ] 确保示例代码可运行

---

**创建日期**: 2025-03  
**最后更新**: 2025-03  
**维护者**: hzhaan
