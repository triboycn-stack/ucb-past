# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: new_counter == 10
# 重复次数: 1, 迭代: 0
# 生成时间: 2026-04-18 16:51:13

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试 RUNNING 状态下 RESET 不生效
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    
    # 测试 counter 达到 10 后 INCREMENT 返回 NO_CHANGE
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    
    # 测试 new_counter == 10 的情况（从 9 增加到 10）
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    
    # 测试类型错误时返回 NO_CHANGE
    ("RUNNING", "test", "INCREMENT", "RUNNING", "test", "NO_CHANGE"),
    (123, 5, "INCREMENT", 123, 5, "NO_CHANGE"),
    ("RUNNING", 5, 123, "RUNNING", 5, "NO_CHANGE"),
    
    # 测试 IDLE 状态下 START 动作
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    
    # 测试 IDLE 状态下 RESET 动作
    ("IDLE", 5, "RESET", "IDLE", 5, "RESET"),
    
    # 测试 RUNNING 状态下 STOP 动作
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    
    # 测试 RUNNING 状态下 INCREMENT 动作（未达到 10）
    ("RUNNING", 5, "INCREMENT", "RUNNING", 6, "INCREMENTED"),
    
    # 测试 STOPPED 状态下 RESUME 动作
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    
    # 测试 STOPPED 状态下 RESET 动作
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    
    # 测试 COMPLETED 状态下 RESET 动作
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    
    # 测试无效动作
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 5, "INVALID", "RUNNING", 5, "NO_CHANGE"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result