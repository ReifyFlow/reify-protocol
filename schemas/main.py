import json
import sys

class PhysicsEngine:
    def __init__(self):
        self.logs = []

    def log(self, msg, level="INFO"):
        icon = {"INFO": "ℹ️", "ERROR": "❌", "SUCCESS": "✅"}.get(level, "")
        print(f"{icon} [{level}] {msg}")
        if level == "ERROR":
            self.logs.append(msg)

    def verify(self, req_file, chip_file):
        print(f"\n--- 开始验证: {req_file} vs {chip_file} ---")
        
        # 1. 加载数据
        try:
            with open(req_file, 'r', encoding='utf-8') as f:
                req = json.load(f)
            with open(chip_file, 'r', encoding='utf-8') as f:
                chip = json.load(f)
        except FileNotFoundError as e:
            self.log(f"文件丢失: {e.filename}", "ERROR")
            return False

        user_intent = req['physics_type']
        target_pin = req.get('target_pin', 'Unknown')
        chip_pin = chip['pin_name']

        # 2. 检查引脚匹配 (Pin Matching)
        if target_pin != chip_pin:
            self.log(f"引脚不匹配！用户想连 {target_pin}，但硬件模型是 {chip_pin}", "ERROR")
            return False

        # 3. 检查能力匹配 (Affordance Check) - 核心逻辑！
        # 获取硬件支持的所有功能列表
        supported_funcs = [a['function'] for a in chip['affordances']]
        
        self.log(f"用户意图: {user_intent}")
        self.log(f"硬件能力: {supported_funcs}")

        if user_intent not in supported_funcs:
            self.log(f"物理定律冲突！引脚 {chip_pin} 不具备 '{user_intent}' 能力。", "ERROR")
            self.log(f"建议：请更换支持 {user_intent} 的引脚 (如 PA0, PB1...)", "INFO")
            return False

        # 4. 检查参数约束 (Constraint Check) - 进阶逻辑
        # 找到对应的能力对象
        capability = next(a for a in chip['affordances'] if a['function'] == user_intent)
        perf_limits = capability.get('performance', {})
        user_params = req['requirements'].get('parameters', {})

        # 例子：检查波特率是否超限
        if user_intent == "serial_stream":
            max_baud = perf_limits.get('max_baud', 0)
            user_baud = user_params.get('baud_rate', 0)
            if user_baud > max_baud:
                self.log(f"参数超限！用户请求 {user_baud} bps，硬件最大支持 {max_baud} bps。", "ERROR")
                return False

        self.log("验证通过！物理连接合法。", "SUCCESS")
        return True

if __name__ == "__main__":
    engine = PhysicsEngine()
    
    # 测试 1: 错误的请求 (PA9 做 ADC)
    engine.verify("user_req_bad.json", "chip_atom_pa9.json")
    
    # 测试 2: 正确的请求 (PA9 做 串口)
    engine.verify("user_req_good.json", "chip_atom_pa9.json")