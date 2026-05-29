# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: action == 'INCREMENT'
# 重复次数: 3, 迭代: 2
# 生成时间: 2026-04-26 06:39:23

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 RUNNING 状态下 INCREMENT 的正常情况
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    # 测试 RUNNING 状态下 INCREMENT 达到最大值 10
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试 RUNNING 状态下 INCREMENT 已经达到 10
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试 IDLE 状态下 INCREMENT 不合法
    ("IDLE", 5, "INCREMENT", "IDLE", 5, "NO_CHANGE"),
    # 测试 STOPPED 状态下 INCREMENT 不合法
    ("STOPPED", 5, "INCREMENT", "STOPPED", 5, "NO_CHANGE"),
    # 测试 COMPLETED 状态下 INCREMENT 不合法
    ("COMPLETED", 5, "INCREMENT", "COMPLETED", 5, "NO_CHANGE"),
    # 测试类型错误
    ("RUNNING", "invalid", "INCREMENT", "RUNNING", "invalid", "NO_CHANGE"),
    ("RUNNING", 5, 123, "RUNNING", 5, "NO_CHANGE"),
    # 测试无效动作
    ("RUNNING", 5, "INVALID", "RUNNING", 5, "NO_CHANGE"),
    # 测试边界条件：counter = 9
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试边界条件：counter = 10
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
])
def test_transition_increment(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result