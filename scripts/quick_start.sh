#!/bin/bash

# Marketing A/B Testing 项目快速启动脚本

echo "=================================="
echo "Marketing A/B Testing 项目设置"
echo "=================================="

# 检查 Python 版本
echo ""
echo "检查 Python 版本..."
python --version

# 创建虚拟环境
echo ""
echo "创建虚拟环境..."
python -m venv venv

# 激活虚拟环境
echo ""
echo "激活虚拟环境..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# 安装依赖
echo ""
echo "安装 Python 依赖包..."
pip install --upgrade pip
pip install -r requirements.txt

# 创建必要的目录
echo ""
echo "确保所有目录存在..."
mkdir -p data/raw data/processed docs/figures docs/screenshots results

echo ""
echo "=================================="
echo "设置完成！"
echo "=================================="
echo ""
echo "下一步："
echo "1. 从 Kaggle 下载数据集："
echo "   https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing"
echo ""
echo "2. 将 marketing_AB.csv 放到 data/raw/ 目录"
echo ""
echo "3. 启动 Jupyter Notebook："
echo "   jupyter notebook notebooks/01_marketing_ab_test.ipynb"
echo ""
