# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: state == 'RUNNING'
# 重复次数: 2, 迭代: 12
# 生成时间: 2026-04-26 06:38:42

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 RUNNING 状态下 RESET 不生效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    
    # 测试 RUNNING 状态下 INCREMENT 有效
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    
    # 测试 RUNNING 状态下 INCREMENT 达到 10 后不生效
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    
    # 测试 RUNNING 状态下 STOP 有效
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    
    # 测试类型错误时返回 NO_CHANGE
    (123, "test", "START", 123, "test", "NO_CHANGE"),
    ("IDLE", "test", "START", "IDLE", "test", "NO_CHANGE"),
    ("IDLE", 5, 123, "IDLE", 5, "NO_CHANGE"),
    
    # 测试无效动作
    ("RUNNING", 5, "INVALID", "RUNNING", 5, "NO_CHANGE"),
    
    # 测试边界条件：counter = 9 时 INCREMENT
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    
    # 测试边界条件：counter = 10 时 INCREMENT
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
])
def test_transition_running_state(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_message = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_message == expected_result