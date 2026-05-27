# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: action == 'RESUME'
# 重复次数: 4, 迭代: 6
# 生成时间: 2026-04-26 06:42:10

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 RESUME 动作在 STOPPED 状态下有效
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    # 测试 RESUME 动作在非 STOPPED 状态下无效
    ("IDLE", 0, "RESUME", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 5, "RESUME", "RUNNING", 5, "NO_CHANGE"),
    ("COMPLETED", 10, "RESUME", "COMPLETED", 10, "NO_CHANGE"),
    # 测试非法输入
    (123, "test", "RESUME", 123, "test", "NO_CHANGE"),
    ("RUNNING", "test", "RESUME", "RUNNING", "test", "NO_CHANGE"),
    ("RUNNING", 5, 123, "RUNNING", 5, "NO_CHANGE"),
    # 测试边界条件
    ("STOPPED", 9, "RESUME", "RUNNING", 9, "RESUMED"),
    ("STOPPED", 10, "RESUME", "STOPPED", 10, "NO_CHANGE"),
])
def test_transition_resume(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result