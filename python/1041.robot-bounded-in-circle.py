class Solution:
    # def isRobotBounded(self, instructions: str) -> bool:
    def isRobotBounded(self, instructions):
        def run(instructions, pos, face):
            # face = 'N'
            n = len(instructions)
            # pos = [0,0]
            for m in range(n):
                if instructions[m] == "G":
                    if face == 'N':
                        pos[0] += 1
                    elif face == 'S':
                        pos[0] -= 1
                    elif face == 'E':
                        pos[1] += 1
                    elif face == 'W':
                        pos[1] -= 1
                elif instructions[m] == 'L':
                    # print('here')
                    if face == 'N':
                        face = 'W'
                    elif face == 'S':
                        face = 'E'
                    elif face == 'E':
                        face = 'N'
                    elif face == 'W':
                        face = 'S'
                elif instructions[m] == 'R':
                    if face == 'N':
                        face = 'E'
                    elif face == 'S':
                        face = 'W'
                    elif face == 'E':
                        face = 'S'
                    elif face == 'W':
                        face = 'N'
                # print(face, pos)
            return pos, face
        original_pos = [0,0]
        original_face = 'N'
        pos = [0,0]
        face = 'N'
        while pos[0] < 101 and pos[1] < 101 and pos[0] > -101 and pos[1] > -101:
            pos, face = run(instructions, pos, face)
            print(pos, face)
            if pos == original_pos and face == original_face:
                return True
        return False


s = Solution()
# ins = "GGLLGG"
# print(s.isRobotBounded(ins))

# ins = "GG"
# print(s.isRobotBounded(ins))

# ins = "GL"
# print(s.isRobotBounded(ins))


ins = "GLGLGGLGL"
print(s.isRobotBounded(ins))