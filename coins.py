class Solution:
    def arrangeCoins(self, n):
        stair  = 0
        list = []

        while(stair<=n):
            list.append(stair)
            n = n-stair
            stair = stair+1

        return list[len(list)-1]


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);

            ret = Solution().arrangeCoins(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()