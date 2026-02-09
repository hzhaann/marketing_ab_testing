#!/usr/bin/env python
"""
环境检查脚本
检查所需的 Python 包是否已安装
"""

import sys

def check_package(package_name, import_name=None):
    """检查包是否已安装"""
    if import_name is None:
        import_name = package_name
    
    try:
        __import__(import_name)
        print(f"✅ {package_name} 已安装")
        return True
    except ImportError:
        print(f"❌ {package_name} 未安装")
        return False

def main():
    print("=" * 50)
    print("环境检查 - Marketing A/B Testing 项目")
    print("=" * 50)
    print()
    
    # 检查 Python 版本
    print(f"Python 版本: {sys.version}")
    print()
    
    # 必需的包
    required_packages = [
        ('pandas', 'pandas'),
        ('numpy', 'numpy'),
        ('scipy', 'scipy'),
        ('matplotlib', 'matplotlib'),
        ('seaborn', 'seaborn'),
        ('jupyter', 'jupyter'),
        ('statsmodels', 'statsmodels'),
    ]
    
    print("检查必需的包:")
    print("-" * 50)
    
    all_installed = True
    for package_name, import_name in required_packages:
        if not check_package(package_name, import_name):
            all_installed = False
    
    print()
    print("=" * 50)
    
    if all_installed:
        print("✅ 所有必需的包都已安装！")
        print("你可以开始分析了。")
    else:
        print("❌ 有些包未安装。")
        print("请运行: pip install -r requirements.txt")
    
    print("=" * 50)

if __name__ == '__main__':
    main()
