# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: action == 'INCREMENT'
# 重复次数: 2, 迭代: 2
# 生成时间: 2026-04-26 06:37:14

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 RUNNING 状态下 INCREMENT
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试 IDLE 状态下 INCREMENT（无效）
    ("IDLE", 5, "INCREMENT", "IDLE", 5, "NO_CHANGE"),
    # 测试 STOPPED 状态下 INCREMENT（无效）
    ("STOPPED", 5, "INCREMENT", "STOPPED", 5, "NO_CHANGE"),
    # 测试 COMPLETED 状态下 INCREMENT（无效）
    ("COMPLETED", 5, "INCREMENT", "COMPLETED", 5, "NO_CHANGE"),
    # 测试类型错误
    ("RUNNING", "test", "INCREMENT", "RUNNING", "test", "NO_CHANGE"),
    (123, 5, "INCREMENT", 123, 5, "NO_CHANGE"),
    ("RUNNING", 5, 123, "RUNNING", 5, "NO_CHANGE"),
    # 测试 RESET 在 RUNNING 状态下不生效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # 测试边界条件：counter=9 时 INCREMENT
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试 counter=10 时 INCREMENT 不生效
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试空动作
    ("RUNNING", 5, "", "RUNNING", 5, "NO_CHANGE"),
    # 测试无效动作
    ("RUNNING", 5, "INVALID", "RUNNING", 5, "NO_CHANGE"),
])
def test_transition_with_increment(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_message = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_message == expected_result