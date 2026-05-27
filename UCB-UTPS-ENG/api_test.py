# quick_test.py
"""快速测试脚本 - 验证环境配置"""

import os
import sys

def check_environment():
    """检查环境配置"""
    print("="*60)
    print("环境检查")
    print("="*60)
    
    # 检查目标文件
    target_files = ["target4_dedent.py", "target5_scanstring.py", 
                    "target6_statemachine.py", "target7_closure.py"]
    
    print("\n1. 检查目标文件:")
    for tf in target_files:
        if os.path.exists(tf):
            print(f"   ✅ {tf}")
        else:
            print(f"   ❌ {tf} (不存在)")
    
    # 检查API连接
    print("\n2. 检查API连接:")
    try:
        from openai import OpenAI
        client = OpenAI(
            api_key="sk-f0df09ba45bf458dacd7dbe1367c16db",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        print("   ✅ OpenAI客户端创建成功")
    except Exception as e:
        print(f"   ❌ OpenAI客户端创建失败: {e}")
    
    # 检查依赖
    print("\n3. 检查依赖包:")
    packages = ['pytest', 'coverage', 'hypothesis', 'numpy', 'scipy', 'matplotlib']
    for pkg in packages:
        try:
            __import__(pkg)
            print(f"   ✅ {pkg}")
        except ImportError:
            print(f"   ❌ {pkg} (未安装)")
    
    print("\n" + "="*60)


def run_minimal_test():
    """运行最小测试"""
    print("\n运行最小测试...")
    
    # 创建目标文件
    if not os.path.exists("target4_dedent.py"):
        from create_target_files import TARGET_FILES
        for filename, content in TARGET_FILES.items():
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content.strip())
            print(f"   创建: {filename}")
    
    # 导入并测试
    try:
        from target4_dedent import dedent
        result = dedent("  hello")
        print(f"   ✅ dedent函数测试通过: {result}")
    except Exception as e:
        print(f"   ❌ dedent函数测试失败: {e}")


if __name__ == "__main__":
    check_environment()
    run_minimal_test()