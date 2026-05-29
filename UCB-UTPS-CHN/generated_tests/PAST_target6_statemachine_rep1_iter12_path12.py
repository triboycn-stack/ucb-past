# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: state == 'RUNNING'
# 重复次数: 1, 迭代: 12
# 生成时间: 2026-04-26 06:36:31

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 RUNNING 状态下 RESET 不生效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # 测试 RUNNING 状态下 STOP 转换
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    # 测试 RUNNING 状态下 INCREMENT 且 counter < 10
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    # 测试 RUNNING 状态下 INCREMENT 且 counter == 9
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    # 测试 RUNNING 状态下 INCREMENT 且 counter >= 10
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试类型错误（state 非字符串）
    (123, 5, "START", 123, 5, "NO_CHANGE"),
    # 测试类型错误（counter 非整数）
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    # 测试类型错误（action 非字符串）
    ("IDLE", 5, 123, "IDLE", 5, "NO_CHANGE"),
    # 测试无效动作
    ("IDLE", 5, "INVALID", "IDLE", 5, "NO_CHANGE"),
    # 测试 RUNNING 状态下无效动作
    ("RUNNING", 5, "RESUME", "RUNNING", 5, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result