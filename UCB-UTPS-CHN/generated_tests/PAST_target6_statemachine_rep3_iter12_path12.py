# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: state == 'RUNNING'
# 重复次数: 3, 迭代: 12
# 生成时间: 2026-04-26 06:40:56

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 RUNNING 状态下 RESET 不生效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    # 测试 RUNNING 状态下 STOP 成功
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    # 测试 RUNNING 状态下 INCREMENT 成功（counter < 10）
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    # 测试 RUNNING 状态下 INCREMENT 达到 10 后不生效
    ("RUNNING", 9, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试 RUNNING 状态下 INCREMENT 达到 10 后再次 INCREMENT 不生效
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    # 测试类型错误时返回 NO_CHANGE
    ("RUNNING", "invalid", "INCREMENT", "RUNNING", "invalid", "NO_CHANGE"),
    ("RUNNING", 5, 123, "RUNNING", 5, "NO_CHANGE"),
    # 测试无效动作
    ("RUNNING", 5, "INVALID_ACTION", "RUNNING", 5, "NO_CHANGE"),
    # 测试 RUNNING 状态下其他动作
    ("RUNNING", 5, "RESUME", "RUNNING", 5, "NO_CHANGE"),
])
def test_transition_running_state(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result