class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str_to_pattern_map = {}
        sliced_pattern = set()
        s_list = s.split()

        if len(s_list) != len(pattern):
            return False

        for i in range(len(s_list)):
            if s_list[i] not in str_to_pattern_map:
                if pattern[i] not in sliced_pattern:
                    str_to_pattern_map[s_list[i]] = pattern[i]
                    sliced_pattern.add(pattern[i])
                else:
                    return False
            else:
                if str_to_pattern_map[s_list[i]] != pattern[i]:
                    return False

        return True

