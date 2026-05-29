# 方法: PAST
# 目标文件: target6_statemachine.py
# 条件路径: not (state != 'RUNNING')
# 重复次数: 4, 迭代: 6
# 生成时间: 2026-04-18 16:58:27

import pytest
from target6_statemachine import transition

@pytest.mark.parametrize("state, counter, action, expected_state, expected_counter, expected_result", [
    # 测试类型错误情况
    ("IDLE", "invalid", "START", "IDLE", "invalid", "NO_CHANGE"),
    (123, 0, "START", "IDLE", 0, "NO_CHANGE"),
    ("IDLE", 0, 123, "IDLE", 0, "NO_CHANGE"),
    
    # 测试 IDLE 状态下的有效动作
    ("IDLE", 0, "START", "RUNNING", 0, "STARTED"),
    ("IDLE", 0, "RESET", "IDLE", 0, "RESET"),
    
    # 测试 RUNNING 状态下的动作
    ("RUNNING", 5, "STOP", "STOPPED", 5, "STOPPED"),
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    ("RUNNING", 5, "RESET", "RUNNING", 5, "NO_CHANGE"),
    
    # 测试 STOPPED 状态下的动作
    ("STOPPED", 5, "RESUME", "RUNNING", 5, "RESUMED"),
    ("STOPPED", 5, "RESET", "IDLE", 0, "RESET"),
    
    # 测试 COMPLETED 状态下的动作
    ("COMPLETED", 10, "RESET", "IDLE", 0, "RESET"),
    
    # 测试无效动作
    ("IDLE", 0, "INVALID", "IDLE", 0, "NO_CHANGE"),
    ("RUNNING", 5, "INVALID", "RUNNING", 5, "NO_CHANGE"),
    ("STOPPED", 5, "INVALID", "STOPPED", 5, "NO_CHANGE"),
    ("COMPLETED", 10, "INVALID", "COMPLETED", 10, "NO_CHANGE"),
    
    # 测试边界条件：counter = 9
    ("RUNNING", 9, "INCREMENT", "COMPLETED", 10, "COMPLETED"),
    
    # 测试边界条件：counter = 10
    ("RUNNING", 10, "INCREMENT", "RUNNING", 10, "NO_CHANGE"),
    
    # 测试状态转换有效性（非核心逻辑，但辅助验证）
    ("IDLE", "START", "START", "RUNNING", 0, "STARTED"),
    ("RUNNING", "STOP", "STOP", "STOPPED", 0, "STOPPED"),
    ("STOPPED", "RESUME", "RESUME", "RUNNING", 0, "RESUMED"),
    ("COMPLETED", "RESET", "RESET", "IDLE", 0, "RESET"),
])
def test_transition(state, counter, action, expected_state, expected_counter, expected_result):
    result_state, result_counter, result_msg = transition(state, counter, action)
    assert result_state == expected_state
    assert result_counter == expected_counter
    assert result_msg == expected_result