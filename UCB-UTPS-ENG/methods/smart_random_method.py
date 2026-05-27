# methods/smart_random_method.py
# SmartRandom Method - Parameter-aware random test generation

import os
import ast
import random
import string
from common.test_executor import TestExecutor
from common.coverage_analyzer import CoverageAnalyzer


class SmartRandomMethod:
    """SmartRandom Method - Parameter-aware random generation"""

    def __init__(self, target_file: str):
        self.target_file = target_file
        self.source = open(target_file, encoding='utf-8').read()
        self.module_name = os.path.splitext(os.path.basename(target_file))[0]
        self.function_name = self._extract_function_name()
        self.params = self._extract_params()
        self.param_types = self._infer_param_types()
        self.coverage_analyzer = CoverageAnalyzer(target_file)

    def _extract_function_name(self) -> str:
        try:
            tree = ast.parse(self.source)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    return node.name
            return os.path.splitext(os.path.basename(self.target_file))[0]
        except:
            return "target_function"

    def _extract_params(self) -> list:
        try:
            tree = ast.parse(self.source)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == self.function_name:
                    return [arg.arg for arg in node.args.args]
        except:
            pass
        return []

    def _infer_param_types(self) -> dict:
        param_types = {}
        for param in self.params:
            if 'id' in param.lower() or 'name' in param.lower():
                param_types[param] = 'identifier'
            elif 'value' in param.lower() or 'num' in param.lower():
                param_types[param] = 'numeric'
            else:
                param_types[param] = 'string'
        return param_types

    def _generate_value(self, param_name: str, param_type: str) -> str:
        if param_type == 'numeric':
            choices = [str(random.randint(-100, 100)), '0', '1', '-1']
            return random.choice(choices)
        elif param_type == 'identifier':
            prefix = random.choice(['test', 'user', 'item'])
            suffix = ''.join(random.choices(string.ascii_lowercase, k=5))
            return f'"{prefix}_{suffix}"'
        else:
            choices = ['""', '"normal"', '"a"', '"123"']
            return random.choice(choices)

    def _generate_test_case(self) -> tuple:
        test_case = []
        for param in self.params:
            param_type = self.param_types.get(param, 'string')
            test_case.append(self._generate_value(param, param_type))
        return tuple(test_case)

    def _generate_test_code(self, iteration: int, test_cases: list) -> str:
        cases_str = ',\n        '.join([str(c) for c in test_cases])

        return f'''
import pytest
from {self.module_name} import {self.function_name}

test_cases = [
        {cases_str}
]

@pytest.mark.parametrize("args", test_cases)
def test_smart_random_iter{iteration}(args):
    try:
        result = {self.function_name}(*args)
        assert True
    except Exception:
        pass
'''

    def run(self, max_iter: int = 15, rep_idx: int = 0) -> dict:
        effective_history = []
        line_history = []
        branch_history = []

        executor = TestExecutor(self.target_file, prefix=f"smartrandom_rep{rep_idx}_")

        for i in range(max_iter):
            num_cases = 10 + i * 2
            test_cases = set()
            for _ in range(num_cases * 2):
                test_cases.add(self._generate_test_case())
                if len(test_cases) >= num_cases:
                    break

            test_code = self._generate_test_code(i, list(test_cases))

            if test_code:
                success, line_cov, branch_cov, covered_lines = executor.run(test_code, i)
                effective_cov = self.coverage_analyzer.compute_effective_coverage(covered_lines)
            else:
                effective_cov = effective_history[-1] if effective_history else 0
                line_cov = line_history[-1] if line_history else 0
                branch_cov = branch_history[-1] if branch_history else 0

            effective_history.append(effective_cov)
            line_history.append(line_cov)
            branch_history.append(branch_cov)

            print(f"     Iteration {i + 1}/{max_iter}: Effective coverage={effective_cov:.1f}%")

        executor.cleanup()

        return {
            'effective_history': effective_history,
            'line_history': line_history,
            'branch_history': branch_history
        }