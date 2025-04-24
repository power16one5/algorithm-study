import itertools
import sys



# 0 또는 1이면 카운트, 2이면 확정
def is_count(a, b, c, d):
    # ccw 계산에 중복되는 값을 저장
    abx, aby = a[0] - b[0], a[1] - b[1]
    bdx, bdy = b[0] - d[0], b[1] - d[1]
    cdx, cdy = c[0] - d[0], c[1] - d[1]

    # ccw 값
    det1, det2 = abx * (b[1] - c[1]) - aby * (b[0] - c[0]), abx * bdy - aby * bdx
    det3, det4 = cdx * (d[1] - a[1]) - cdy * (d[0] - a[0]), cdx * -bdy - cdy * -bdx

    # 두 선분이 교차할 경우
    if det1 * det2 < 0 and det3 * det4 < 0: return 1
    # 두 선분이 교차하지 않을 경우
    elif det1 * det2 > 0 or det3 * det4 > 0: return 0
    # 두 선분이 일직선상에 있을 경우
    elif not any([det1, det2, det3, det4]): return 0
    # 대상이 선분 위에 있는 경우
    elif not det1: return 2
    # ab 선분이 cd 선분의 y좌표값 보다 큰 경우
    elif a[1] >= c[1] and b[1] >= c[1]: return 1
    else: return 0


def main():
    readline = sys.stdin.readline
    N = int(readline())
    
    vertexes = [tuple(map(int, readline().split())) for _ in range(N)]
    lines = [(a, b) for a, b in itertools.pairwise([vertexes[-1]] + vertexes)]
    del vertexes

    points = [tuple(map(int, readline().split())) for _ in range(3)]

    fixed_point = [-1, None]
    for point in points:
        count = 0
        fixed_point[1] = point[1]

        for a, b in lines:
            ret = is_count(a, b, point, fixed_point)

            if ret == 2:
                count = 1
                break
        
            else:
                count += ret
        
        if count & 1: print(1)
        else: print(0)


main()
