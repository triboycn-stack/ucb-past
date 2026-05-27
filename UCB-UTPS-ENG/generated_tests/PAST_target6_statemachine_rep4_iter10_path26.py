# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: counter == 9
# 重复次数: 4, 迭代: 10
# 生成时间: 2026-04-18 16:59:01

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试条件: counter == 9
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试边界条件: counter == 10
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试类型错误
    (123, "test", "START", 123, "test", "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    ("IDLE", 5, 123, "IDLE", 5, "NO_CHANGE"),
    # 测试无效动作
    ("IDLE", 0, "STOP", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 0, "RESET", "RUNNING", 0, "NO_CHANGE"),
    ("STOPPED", 0, "INCREMENT", "STOPPED", 0, "NO_CHANGE"),
    # 测试状态转换逻辑
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    ("RUNNING", 0, "STOP", "STOPPED", 0, "STOPPED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("STOPPED", 0, "RESUME", "RUNNING", 0, "RESUMED"),
    ("STOPPED", 0, "RESET", "IDLE", 0, "RESET"),
    ("COMPLETED", 0, "RESET", "IDLE", 0, "RESET"),
    # 测试 RESET 在 RUNNING 状态下不生效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # 测试 INCREMENT 在 counter >= 10 时不生效
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试空动作
    ("IDLE", 0, "", "IDLE", 0, "NO_CHANGE"),
    # 测试非法动作
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result