# common/test_executor.py

import os
import sys
import subprocess
import time
import json


class TestExecutor:
    def __init__(self, target_file: str, prefix: str = ""):
        self.target_file = target_file
        self.module = os.path.splitext(os.path.basename(target_file))[0]
        self.test_file = f"test_{prefix}{self.module}.py"
        self.last_covered_lines = set()
        self.last_line_coverage = 0.0

    def run(self, test_code: str, iteration: int = -1) -> tuple:
        try:
            # 写入测试文件
            with open(self.test_file, "w", encoding="utf-8") as f:
                f.write("import sys, os\n")
                f.write("sys.path.insert(0, os.getcwd())\n")
                f.write(f"from {self.module} import *\n\n")
                f.write(test_code + "\n")

            # 清理旧覆盖率文件
            for path in [".coverage", "coverage.json"]:
                try:
                    if os.path.exists(path):
                        os.remove(path)
                except:
                    pass

            # 使用 pytest-cov 运行测试
            cmd = [
                sys.executable, "-m", "pytest", self.test_file,
                f"--cov={self.module}", "--cov-report=json",
                "-q", "--tb=short", "--disable-warnings"
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            # 等待文件生成
            time.sleep(0.5)

            if not os.path.exists("coverage.json"):
                print(f"        [WARN] coverage.json 未生成")
                return False, 0.0, 0.0, set()

            # 解析覆盖率
            with open("coverage.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            # 获取目标文件的覆盖率
            line_cov = 0.0
            covered_lines = set()
            total_lines = 0
            covered_count = 0

            for file_path, file_data in data.get("files", {}).items():
                if self.module in file_path or file_path.endswith(f"{self.module}.py"):
                    # 从 executed_lines 计算覆盖率
                    executed_lines = file_data.get("executed_lines", [])
                    missing_lines = file_data.get("missing_lines", [])

                    covered_lines.update(executed_lines)
                    total_lines = len(executed_lines) + len(missing_lines)
                    covered_count = len(executed_lines)

                    if total_lines > 0:
                        line_cov = (covered_count / total_lines) * 100

                    print(f"        [DEBUG] 文件: {file_path}")
                    print(f"        [DEBUG] 执行行数: {covered_count}, 总行数: {total_lines}")
                    print(f"        [DEBUG] 计算覆盖率: {line_cov:.1f}%")

            self.last_covered_lines = covered_lines
            self.last_line_coverage = line_cov

            success = result.returncode == 0
            print(f"        [DEBUG] pytest 返回码: {result.returncode}, success={success}")

            return success, line_cov, 0.0, covered_lines

        except subprocess.TimeoutExpired:
            print(f"        [TIMEOUT] 测试超时")
            return False, 0.0, 0.0, set()
        except Exception as e:
            print(f"        [ERROR] 执行错误: {e}")
            return False, 0.0, 0.0, set()

    def get_covered_lines(self):
        return self.last_covered_lines

    def cleanup(self):
        try:
            if os.path.exists(self.test_file):
                os.remove(self.test_file)
        except:
            pass