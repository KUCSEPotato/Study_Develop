# chatgpt에 의해 생성된 코드입니다.
# internal_sha256_debug.py
# 순수 파이썬 SHA-256 (학습/디버깅용) - FIPS 180-4 기반
# verbose/log 포인트와 선택적 breakpoint가 포함되어 있습니다.

def _rotr(x, n): return ((x >> n) | (x << (32 - n))) & 0xffffffff
def _shr(x, n):  return x >> n
def _Ch(x, y, z):   return (x & y) ^ (~x & z)
def _Maj(x, y, z):  return (x & y) ^ (x & z) ^ (y & z)
def _Σ0(x):         return _rotr(x, 2) ^ _rotr(x, 13) ^ _rotr(x, 22)
def _Σ1(x):         return _rotr(x, 6) ^ _rotr(x, 11) ^ _rotr(x, 25)
def _σ0(x):         return _rotr(x, 7) ^ _rotr(x, 18) ^ _shr(x, 3)
def _σ1(x):         return _rotr(x, 17) ^ _rotr(x, 19) ^ _shr(x, 10)

_K = [
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]

def sha256_py(msg: bytes,
              verbose: bool = False,
              round_trace = (0, 1, 63),  # 어떤 라운드를 로그로 볼지
              use_breakpoint: bool = False) -> bytes:
    """학습용 SHA-256. verbose를 켜면 내부 상태를 출력합니다."""
    # 초기 해시 값
    H = [
        0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
        0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
    ]

    # 패딩
    ml = len(msg) * 8
    msg = msg + b'\x80'
    while (len(msg) * 8) % 512 != 448:
        msg += b'\x00'
    msg += ml.to_bytes(8, 'big')

    if verbose:
        print(f"[padding done] total={len(msg)} bytes, original_bits={ml}")

    # 512비트(64바이트) 블록 처리
    for i in range(0, len(msg), 64):
        block_idx = i // 64
        block = msg[i:i+64]

        if verbose:
            print(f"\n[block {block_idx}] raw={block.hex()}")

        # 메시지 스케줄
        W = [int.from_bytes(block[j:j+4], 'big') for j in range(0, 64, 4)]
        for t in range(16, 64):
            W.append((_σ1(W[t-2]) + W[t-7] + _σ0(W[t-15]) + W[t-16]) & 0xffffffff)

        if verbose:
            print(f"W[0..7]   = {[hex(x) for x in W[:8]]}")
            print(f"W[56..63] = {[hex(x) for x in W[56:]]}")

        a, b, c, d, e, f, g, h = H

        # 선택적 breakpoint: 블록 시작 직후
        if use_breakpoint:
            print(f"[block {block_idx}] breakpoint before rounds")
            breakpoint()

        for t in range(64):
            T1 = (h + _Σ1(e) + _Ch(e, f, g) + _K[t] + W[t]) & 0xffffffff
            T2 = (_Σ0(a) + _Maj(a, b, c)) & 0xffffffff

            if verbose and (t in round_trace):
                print(f"round {t:02d}: "
                      f"a={a:08x} b={b:08x} c={c:08x} d={d:08x} "
                      f"e={e:08x} f={f:08x} g={g:08x} h={h:08x} "
                      f"T1={T1:08x} T2={T2:08x}")

                # 라운드 진입 시점 브레이크
                if use_breakpoint:
                    print(f"[block {block_idx}] breakpoint at round {t}")
                    breakpoint()

            h, g, f, e, d, c, b, a = (
                g, f, e, (d + T1) & 0xffffffff, c, b, a, (T1 + T2) & 0xffffffff
            )

        H = [(x + y) & 0xffffffff for x, y in zip(H, [a, b, c, d, e, f, g, h])]
        if verbose:
            print(f"[block {block_idx}] H={list(map(lambda v: f'{v:08x}', H))}")

    digest = b''.join(hv.to_bytes(4, 'big') for hv in H)
    return digest


# 표준 테스트 벡터(학습용 보증)
assert sha256_py(b"abc").hex() == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"

def main():
    print(">>> main entered")
    # 디버깅/학습용 실행 예시
    data = b"abc"
    print(f"input={data!r}")

    # verbose=True 로 내부 상태를 확인 (round 0,1,63만 출력)
    dg = sha256_py(data, verbose=True, round_trace=(0, 1, 63), use_breakpoint=False).hex()
    print(f"final digest={dg}")

    # 필요 시 다른 입력도 테스트
    # dg2 = sha256_py(b"hello", verbose=False).hex()
    # print(f"sha256('hello')={dg2}")

if __name__ == "__main__":
    main()
