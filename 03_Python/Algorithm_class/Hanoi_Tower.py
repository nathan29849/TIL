# recursion 이용
# 원반 n개를 source 번째 기둥에서 dest 번째 기둥으로 옮김 (feat. temp 번째 기둥을 보조하여.)
# source = 시작 기둥 / dest = 목표 기둥 / temp = 보조 기둥
def hanoiTower(n, source, dest, temp):
    if (n==1):
        print("Move a disk from peg %d to peg %d" % (source, dest))
    else:
        hanoiTower(n-1, source, temp, dest)     # 우선 보조 기둥(temp)에 마지막 원판을 제외하고 모두 옮긴다.
        print("Move a disk from peg %d to peg %d" % (source, dest)) # 마지막 원판을 시작 기둥에서 목표 기둥에 옮긴다.
        hanoiTower(n-1, temp, dest, source)     # line 8에서 보조기둥으로 모두 옮겼던 것들을 목표기둥으로 이동시킨다.

hanoiTower(3, 1, 3, 2)
