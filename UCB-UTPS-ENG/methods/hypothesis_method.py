# methods/hypothesis_method.py
"""Hypothesis Method - Property-Based Testing"""

import os
from common.test_executor import TestExecutor
from common.coverage_analyzer import CoverageAnalyzer


class HypothesisMethod:
    """Hypothesis Method Class"""

    def __init__(self, target_file: str):
        """Initialize Hypothesis method

        Args:
            target_file: Path to the target Python file
        """
        self.target_file = target_file
        self.source = open(target_file, encoding='utf-8').read()
        self.module_name = os.path.splitext(os.path.basename(target_file))[0]
        self.function_name = self._extract_function_name()
        self.coverage_analyzer = CoverageAnalyzer(target_file)

    def _extract_function_name(self) -> str:
        """Extract the target function name from source code"""
        try:
            import ast
            tree = ast.parse(self.source)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    return node.name
            return os.path.splitext(os.path.basename(self.target_file))[0]
        except:
            return "target_function"

    def _generate_test_code(self, iteration: int) -> str:
        """Generate Hypothesis test code

        Args:
            iteration: Current iteration number

        Returns:
            Generated test code as string
        """
        num_examples = 50 + iteration * 10

        if "dedent" in self.function_name:
            return f"""
import pytest
from hypothesis import given, strategies as st, settings
from hypothesis import HealthCheck

settings.register_profile("ci", max_examples={num_examples}, deadline=None,
                         suppress_health_check=[HealthCheck.too_slow])
settings.load_profile("ci")

@given(st.text())
def test_dedent_iter{iteration}(text_input):
    \"\"\"Test dedent function\"\"\"
    from {self.module_name} import dedent
    result = dedent(text_input)
    assert isinstance(result, str)
"""
        elif "scanstring" in self.function_name:
            return f"""
import pytest
from hypothesis import given, strategies as st, settings

settings.register_profile("ci", max_examples={num_examples}, deadline=None)
settings.load_profile("ci")

@given(st.text())
def test_scanstring_iter{iteration}(s):
    \"\"\"Test scanstring function\"\"\"
    from {self.module_name} import scanstring
    test_str = f'"{{s}}"'
    try:
        result, next_idx = scanstring(test_str, 1)
        assert isinstance(result, str)
        assert next_idx > 1
    except ValueError:
        pass
"""
        else:
            return f"""
import pytest
from hypothesis import given, strategies as st, settings

settings.register_profile("ci", max_examples={num_examples}, deadline=None)
settings.load_profile("ci")

@given(st.integers(), st.integers())
def test_generic_iter{iteration}(a, b):
    \"\"\"Test generic function\"\"\"
    from {self.module_name} import {self.function_name}
    try:
        result = {self.function_name}(a, b)
    except Exception:
        pass
"""

    def run(self, max_iter: int = 15, rep_idx: int = 0) -> dict:
        """Run Hypothesis method

        Args:
            max_iter: Maximum number of iterations
            rep_idx: Replication index

        Returns:
            Dictionary containing coverage histories
        """

        effective_history = []
        line_history = []
        branch_history = []

        executor = TestExecutor(self.target_file, prefix=f"hypothesis_rep{rep_idx}_")

        for i in range(max_iter):
            test_code = self._generate_test_code(i)

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

            print(f"      Iteration {i + 1}/{max_iter}: Effective Coverage = {effective_cov:.1f}%")

        executor.cleanup()

        return {
            'effective_history': effective_history,
            'line_history': line_history,
            'branch_history': branch_history
        }