#
# @lc app=leetcode id=875 lang=python3
DEBUG = False
import math
class Solution:
    # def minEatingSpeed(self, piles: List[int], H: int) -> int:
    def minEatingSpeed(self, piles, H):
        n = len(piles)
        if n == H:
            return max(piles)
        if H >= sum(piles):
            return 1

        high = max(piles)
        low = 1
        max_slots = H - n
        # if DEBUG:
        # print('starting low, high', low, high)  
        # print('max extra slots =', max_slots)



        def get_slots_needed(l, K):
            # if DEBUG:
            #     print(l, K)
            # print('here K =',K, "len(l) = ", len(l), [i <= K for i in l], l)
            if all([i <= K for i in l]):
                # print('here', l)
                return len(l)
            else:
                # print('here2', l, 'K=', K)
                return len(l) + sum([math.ceil((i-K)/K) for i in l if i - K > 0])

        

        def f(K, debug=DEBUG):
            if debug:
                print("="*30)
                print('checking K =', K)
                print('piles =', piles)
            l = [p-K for p in piles if p-K > 0]
            pad = list(map(lambda x: K if x - K > 0 else x,piles))
            slots_needed = get_slots_needed(l, K)
            if debug:
                print('piles after deduction =', pad)
                print('extra piles =', l)
                print('slots needed =', slots_needed)
            p_minus_K = [p-K for p in piles if p-K > 0]
            if slots_needed < max_slots:
                # if K == 2:
                #     if 2 * slots_needed >= max_slots:
                #         return False, False
                too_low = False
                too_high = True
                return too_low, too_high
            elif slots_needed > max_slots:
                too_low = True
                too_high = False
                return too_low, too_high
            else:
                if debug:
                    print('else piles after deduction =', pad)
                    print('else extra piles =', l)
                if len(pad) > 1:
                    pad.sort(reverse=True)
                    if pad[0] > pad[1]:
                        too_low = False
                        too_high = True
                        return too_low, too_high
                return False, False
                
               


        def bs(low, high, debug=DEBUG):
            K = low + (high - low) // 2
            too_low, too_high = f(K)
            if debug:
                if too_low:
                    print(K, 'is low')
                if too_high:
                    print(K, 'is high')
            if too_high:
                return bs(low, K)
            elif too_low:
                next_k = K + (high-K) // 2
                # print(next_k, K)
                if next_k == K:
                    return K + 1
                return bs(K, high)
            else:
                # print('here')
                return K
        # print('here', bs(low, high))
        return bs(low, high)



# s = Solution()
# piles = [3,6,7,11]
# H = 8
# print(s.minEatingSpeed(piles, H) == 4)



# piles = [10]
# H = 2
# print(s.minEatingSpeed(piles, H) == 5)


# piles = [11]
# H = 2
# print(s.minEatingSpeed(piles, H) == 6)



# piles = [30,11,23,4,20]
# H = 6
# print(s.minEatingSpeed(piles, H) == 23) #23




# piles = [30, 11, 23, 4, 20]
# H = 5
# print(s.minEatingSpeed(piles, H) == 30)

# # piles = [100,99,98]
# # H = 90
# # print(s.minEatingSpeed(piles, H))



# piles = [332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184]
# H = 823855818
# print(s.minEatingSpeed(piles, H) == 14)
# print(divmod(max(piles), H))
# print(H + 117946366 == max(piles))
# print(H / max(piles))


