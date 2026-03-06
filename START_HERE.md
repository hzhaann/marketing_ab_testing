# 🚀 从这里开始 - Marketing A/B Testing 项目

欢迎！这是你的第二个数据分析作品集项目。

---

## 📋 项目概述

**项目名称**: Marketing A/B Testing - 投放效果评估  
**项目类型**: 个人作品集项目  
**技术栈**: Python, Jupyter Notebook, 统计推断, A/B Testing  
**预计时间**: 3-5 天  
**当前状态**: 🟡 初始化完成，待开始分析

---

## 🎯 项目目标

通过这个项目，你将：
1. ✅ 补齐简历中 A/B 测试能力的缺口
2. ✅ 展示完整的实验分析流程（假设检验、统计推断、业务评估）
3. ✅ 产出可投递的 GitHub 项目
4. ✅ 准备好面试所需的代码、图表、结论

---

## 🏃 快速开始（3 步）

### Step 1: 下载数据集

访问 Kaggle 下载数据：
```
https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing
```

将 `marketing_AB.csv` 放到 `data/raw/` 目录。

### Step 2: 配置环境

运行快速启动脚本：
```bash
bash scripts/quick_start.sh
```

或手动配置：
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: 开始分析

可复现执行（会生成 `docs/figures/` 下的图表）：
```bash
./venv/bin/python -m jupyter nbconvert --execute --to notebook --inplace notebooks/01_marketing_ab_test.ipynb
```

交互式打开（可选）：
```bash
./venv/bin/python -m jupyter notebook notebooks/01_marketing_ab_test.ipynb
```

---

## 📁 项目结构一览

```
marketing_ab_testing/
├── 📄 README.md                    # 项目主文档（GitHub 首页）
├── 📄 START_HERE.md                # 本文件（快速开始指南）
├── 📄 PROJECT_STATUS.md            # 项目进度追踪
├── 📄 CHANGELOG.md                 # 版本更新日志
│
├── 📂 data/                        # 数据目录
│   ├── raw/                       # 原始数据（从 Kaggle 下载）
│   └── processed/                 # 处理后的数据
│
├── 📂 notebooks/                   # 分析 Notebook
│   └── 01_marketing_ab_test.ipynb # 核心分析文件 ⭐
│
├── 📂 src/                         # 源代码
│   └── ab_utils.py                # A/B 测试工具函数库 ⭐
│
├── 📂 docs/                        # 文档
│   ├── data_dictionary.md         # 数据字典
│   ├── experiment_summary.md      # 实验结论卡 ⭐
│   ├── PROJECT_ROADMAP.md         # 项目路线图
│   ├── RESUME_TEMPLATE.md         # 简历写法参考 ⭐
│   └── DIRECTORY_STRUCTURE.md     # 目录结构说明
│
└── 📂 scripts/                     # 脚本
    └── quick_start.sh             # 快速启动脚本
```

**⭐ 标记的是核心文件，优先关注！**

---

## 📚 核心文档导航

### 1️⃣ 开始分析前必读

- **[PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md)**: 项目路线图（Day 1-5 推进计划）
- **[data_dictionary.md](docs/data_dictionary.md)**: 数据字典（字段说明、指标定义）

### 2️⃣ 分析过程中参考

- **[ab_utils.py](src/ab_utils.py)**: 工具函数库（Z 检验、Bootstrap、效应量等）
- **[01_marketing_ab_test.ipynb](notebooks/01_marketing_ab_test.ipynb)**: 分析 Notebook

### 3️⃣ 完成分析后填写

- **[experiment_summary.md](docs/experiment_summary.md)**: 实验结论卡（填写发现和建议）
- **[RESUME_TEMPLATE.md](docs/RESUME_TEMPLATE.md)**: 简历写法参考（准备面试材料）

### 4️⃣ 项目管理

- **[PROJECT_STATUS.md](PROJECT_STATUS.md)**: 项目进度追踪
- **[CHANGELOG.md](CHANGELOG.md)**: 版本更新日志

---

## 🗓️ 推荐推进计划

### Day 1: 数据探索（2-3 小时）
- [ ] 下载数据集
- [ ] 数据加载与初步探索
- [ ] 完善数据字典

### Day 2: 数据质量检查（2-3 小时）
- [ ] 缺失值、重复值检查
- [ ] SRM 检查
- [ ] 计算转化率

### Day 3: 统计推断（2-3 小时）
- [ ] Z 检验
- [ ] 置信区间
- [ ] Bootstrap

### Day 4: 分层分析（2-3 小时）
- [ ] Practical Significance
- [ ] 按曝光频次分层
- [ ] 按时段分层

### Day 5: 结论总结（1-2 小时）
- [ ] 填写实验结论卡
- [ ] 完善文档
- [ ] 准备简历

---

## 🎓 学习资源

### 统计方法
- [A/B Testing Best Practices](https://www.exp-platform.com/)
- [Statistical Inference for A/B Testing](https://www.evanmiller.org/ab-testing/)

### Python 工具
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [scipy.stats Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)

---

## ✅ 完成标准（MVP）

要达到"可投递"状态，必须完成：

1. ✅ 完整的分析 Notebook（代码 + 图表 + 结论）
2. ✅ 实验结论卡（填写完整）
3. ✅ 至少 3 个核心发现
4. ✅ 至少 2 条行动建议
5. ✅ 简历描述（基于写法参考整理）

---

## 🤔 常见问题

### Q1: 数据集在哪里下载？
A: 访问 [Kaggle](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing)，下载 `marketing_AB.csv`。

### Q2: 如何运行 Notebook？
A: 
```bash
# 1. 激活虚拟环境
source venv/bin/activate

# 2. 启动 Jupyter
jupyter notebook notebooks/01_marketing_ab_test.ipynb
```

### Q3: 如何使用 ab_utils.py 中的函数？
A: 在 Notebook 中：
```python
import sys
sys.path.append('../src')
from ab_utils import *
```

### Q4: 如何设定 MDE？
A: 参考 [data_dictionary.md](docs/data_dictionary.md) 中的建议：
- 保守：≥ 1% 绝对提升
- 中等：≥ 0.5% 绝对提升
- 激进：≥ 0.2% 绝对提升

### Q5: 完成后如何准备简历？
A: 参考 [RESUME_TEMPLATE.md](docs/RESUME_TEMPLATE.md)，填写具体数据和发现。

---

## 📞 需要帮助？

### 项目相关
- 查看 [PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md) 了解详细计划
- 查看 [DIRECTORY_STRUCTURE.md](docs/DIRECTORY_STRUCTURE.md) 了解目录结构

### 技术问题
- 查看 [ab_utils.py](src/ab_utils.py) 中的函数文档
- 参考 [data_dictionary.md](docs/data_dictionary.md) 了解数据

### 面试准备
- 查看 [RESUME_TEMPLATE.md](docs/RESUME_TEMPLATE.md) 中的面试问题清单
- 查看 [experiment_summary.md](docs/experiment_summary.md) 准备结论

---

## 🎉 准备好了吗？

现在就开始吧！

1. ✅ 下载数据集
2. ✅ 运行 `bash scripts/quick_start.sh`
3. ✅ 打开 Notebook 开始分析

 

---

**创建日期**: 2025-03  
**项目负责人**: hzhaan  
**项目状态**: 🟡 待开始分析
