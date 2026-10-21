import main

def SAMPLES():
    # 実際に関数を呼び出して落ちないことを確認するテスト
    try:
        main.sample()
    except Exception as e:
        assert False, f"Unexpected error: {e}"
