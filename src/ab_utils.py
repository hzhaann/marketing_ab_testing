"""
A/B Testing Utility Functions
用于 A/B 测试分析的工具函数集合
"""

import numpy as np
import pandas as pd
from scipy import stats
from typing import Tuple, Dict, Optional


def calculate_conversion_rate(data: pd.DataFrame, 
                              group_col: str = 'test group',
                              conversion_col: str = 'converted') -> pd.DataFrame:
    """
    计算各组的转化率
    
    Parameters:
    -----------
    data : pd.DataFrame
        包含实验数据的DataFrame
    group_col : str
        分组列名
    conversion_col : str
        转化列名
        
    Returns:
    --------
    pd.DataFrame
        包含各组转化率统计的DataFrame
    """
    result = data.groupby(group_col).agg({
        conversion_col: ['count', 'sum', 'mean']
    }).round(4)
    
    result.columns = ['total_users', 'converted_users', 'conversion_rate']
    result['non_converted_users'] = result['total_users'] - result['converted_users']
    
    return result


def proportion_z_test(conversions_a: int, n_a: int, 
                     conversions_b: int, n_b: int,
                     alternative: str = 'two-sided') -> Dict:
    """
    两样本比例Z检验
    
    Parameters:
    -----------
    conversions_a : int
        组A的转化数
    n_a : int
        组A的总样本数
    conversions_b : int
        组B的转化数
    n_b : int
        组B的总样本数
    alternative : str
        检验类型：'two-sided', 'larger', 'smaller'
        
    Returns:
    --------
    dict
        包含检验结果的字典
    """
    # 计算转化率
    p_a = conversions_a / n_a
    p_b = conversions_b / n_b
    
    # 合并比例
    p_pool = (conversions_a + conversions_b) / (n_a + n_b)
    
    # 标准误
    se = np.sqrt(p_pool * (1 - p_pool) * (1/n_a + 1/n_b))
    
    # Z统计量
    z_stat = (p_a - p_b) / se
    
    # P值
    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    elif alternative == 'larger':
        p_value = 1 - stats.norm.cdf(z_stat)
    else:  # smaller
        p_value = stats.norm.cdf(z_stat)
    
    return {
        'conversion_rate_a': p_a,
        'conversion_rate_b': p_b,
        'difference': p_a - p_b,
        'relative_lift': (p_a - p_b) / p_b if p_b > 0 else np.nan,
        'z_statistic': z_stat,
        'p_value': p_value,
        'significant_at_0.05': p_value < 0.05
    }


def confidence_interval_proportion(conversions: int, n: int, 
                                  confidence: float = 0.95) -> Tuple[float, float]:
    """
    计算比例的置信区间（正态近似）
    
    Parameters:
    -----------
    conversions : int
        转化数
    n : int
        总样本数
    confidence : float
        置信水平
        
    Returns:
    --------
    tuple
        (下界, 上界)
    """
    p = conversions / n
    z = stats.norm.ppf((1 + confidence) / 2)
    se = np.sqrt(p * (1 - p) / n)
    
    lower = p - z * se
    upper = p + z * se
    
    return (max(0, lower), min(1, upper))


def bootstrap_confidence_interval(data_a: np.ndarray, data_b: np.ndarray,
                                 n_bootstrap: int = 10000,
                                 confidence: float = 0.95,
                                 random_state: Optional[int] = None) -> Dict:
    """
    Bootstrap方法计算转化率差异的置信区间
    
    Parameters:
    -----------
    data_a : np.ndarray
        组A的转化数据（0/1数组）
    data_b : np.ndarray
        组B的转化数据（0/1数组）
    n_bootstrap : int
        Bootstrap重采样次数
    confidence : float
        置信水平
    random_state : int, optional
        随机种子
        
    Returns:
    --------
    dict
        包含Bootstrap结果的字典
    """
    if random_state is not None:
        np.random.seed(random_state)
    
    n_a = len(data_a)
    n_b = len(data_b)
    
    # Bootstrap重采样
    differences = []
    for _ in range(n_bootstrap):
        sample_a = np.random.choice(data_a, size=n_a, replace=True)
        sample_b = np.random.choice(data_b, size=n_b, replace=True)
        
        diff = sample_a.mean() - sample_b.mean()
        differences.append(diff)
    
    differences = np.array(differences)
    
    # 计算置信区间
    alpha = 1 - confidence
    lower = np.percentile(differences, alpha/2 * 100)
    upper = np.percentile(differences, (1 - alpha/2) * 100)
    
    return {
        'mean_difference': differences.mean(),
        'std_difference': differences.std(),
        'ci_lower': lower,
        'ci_upper': upper,
        'confidence_level': confidence
    }


def calculate_effect_size(conversions_a: int, n_a: int,
                         conversions_b: int, n_b: int) -> Dict:
    """
    计算效应量（Cohen's h）
    
    Parameters:
    -----------
    conversions_a : int
        组A的转化数
    n_a : int
        组A的总样本数
    conversions_b : int
        组B的转化数
    n_b : int
        组B的总样本数
        
    Returns:
    --------
    dict
        包含效应量的字典
    """
    p_a = conversions_a / n_a
    p_b = conversions_b / n_b
    
    # Cohen's h
    h = 2 * (np.arcsin(np.sqrt(p_a)) - np.arcsin(np.sqrt(p_b)))
    
    # 效应量解释
    if abs(h) < 0.2:
        interpretation = 'small'
    elif abs(h) < 0.5:
        interpretation = 'medium'
    else:
        interpretation = 'large'
    
    return {
        'cohens_h': h,
        'interpretation': interpretation,
        'absolute_difference': p_a - p_b,
        'relative_lift': (p_a - p_b) / p_b if p_b > 0 else np.nan
    }


def sample_size_calculation(p1: float, p2: float, 
                           alpha: float = 0.05, 
                           power: float = 0.8) -> int:
    """
    计算所需样本量（每组）
    
    Parameters:
    -----------
    p1 : float
        组1的预期转化率
    p2 : float
        组2的预期转化率
    alpha : float
        显著性水平
    power : float
        统计功效
        
    Returns:
    --------
    int
        每组所需样本量
    """
    # 效应量
    h = 2 * (np.arcsin(np.sqrt(p1)) - np.arcsin(np.sqrt(p2)))
    
    # Z值
    z_alpha = stats.norm.ppf(1 - alpha/2)
    z_beta = stats.norm.ppf(power)
    
    # 样本量
    n = ((z_alpha + z_beta) / h) ** 2
    
    return int(np.ceil(n))


def check_sample_ratio_mismatch(n_a: int, n_b: int, 
                                expected_ratio: float = 0.5,
                                alpha: float = 0.05) -> Dict:
    """
    检查样本比例失配（Sample Ratio Mismatch, SRM）
    
    Parameters:
    -----------
    n_a : int
        组A的样本量
    n_b : int
        组B的样本量
    expected_ratio : float
        预期组A的比例
    alpha : float
        显著性水平
        
    Returns:
    --------
    dict
        SRM检查结果
    """
    total = n_a + n_b
    observed_ratio = n_a / total
    
    # 卡方检验
    expected_a = total * expected_ratio
    expected_b = total * (1 - expected_ratio)
    
    chi2_stat = ((n_a - expected_a)**2 / expected_a + 
                 (n_b - expected_b)**2 / expected_b)
    
    p_value = 1 - stats.chi2.cdf(chi2_stat, df=1)
    
    return {
        'observed_ratio': observed_ratio,
        'expected_ratio': expected_ratio,
        'chi2_statistic': chi2_stat,
        'p_value': p_value,
        'srm_detected': p_value < alpha,
        'warning': 'SRM detected! Check randomization.' if p_value < alpha else 'No SRM detected.'
    }


def practical_significance_check(difference: float, 
                                mde: float,
                                p_value: float,
                                alpha: float = 0.05) -> Dict:
    """
    检查实际业务意义（Practical Significance）
    
    Parameters:
    -----------
    difference : float
        观测到的差异
    mde : float
        最小可检测效应（Minimum Detectable Effect）
    p_value : float
        统计检验的p值
    alpha : float
        显著性水平
        
    Returns:
    --------
    dict
        业务意义检查结果
    """
    statistically_significant = p_value < alpha
    practically_significant = abs(difference) >= mde
    
    if statistically_significant and practically_significant:
        recommendation = 'Launch: Both statistically and practically significant'
    elif statistically_significant and not practically_significant:
        recommendation = 'Do not launch: Statistically significant but effect too small'
    elif not statistically_significant and practically_significant:
        recommendation = 'Inconclusive: Large effect but not statistically significant (may need more data)'
    else:
        recommendation = 'Do not launch: Neither statistically nor practically significant'
    
    return {
        'statistically_significant': statistically_significant,
        'practically_significant': practically_significant,
        'recommendation': recommendation,
        'observed_difference': difference,
        'mde_threshold': mde
    }


def stratified_analysis(data: pd.DataFrame,
                       group_col: str,
                       conversion_col: str,
                       strata_col: str) -> pd.DataFrame:
    """
    分层分析
    
    Parameters:
    -----------
    data : pd.DataFrame
        实验数据
    group_col : str
        分组列名
    conversion_col : str
        转化列名
    strata_col : str
        分层列名
        
    Returns:
    --------
    pd.DataFrame
        分层分析结果
    """
    results = []
    
    for stratum in data[strata_col].unique():
        stratum_data = data[data[strata_col] == stratum]
        
        for group in stratum_data[group_col].unique():
            group_data = stratum_data[stratum_data[group_col] == group]
            
            n = len(group_data)
            conversions = group_data[conversion_col].sum()
            cr = conversions / n if n > 0 else 0
            
            results.append({
                'stratum': stratum,
                'group': group,
                'n': n,
                'conversions': conversions,
                'conversion_rate': cr
            })
    
    return pd.DataFrame(results)


if __name__ == '__main__':
    # 示例用法
    print("A/B Testing Utility Functions")
    print("=" * 50)
    
    # 示例数据
    conversions_a = 1000
    n_a = 10000
    conversions_b = 950
    n_b = 10000
    
    # Z检验
    result = proportion_z_test(conversions_a, n_a, conversions_b, n_b)
    print("\nZ-Test Results:")
    for key, value in result.items():
        print(f"  {key}: {value}")
    
    # 效应量
    effect = calculate_effect_size(conversions_a, n_a, conversions_b, n_b)
    print("\nEffect Size:")
    for key, value in effect.items():
        print(f"  {key}: {value}")
