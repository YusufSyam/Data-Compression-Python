# Encode HDC implementation (brute force)

import re

def encode_hdc(s):
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    if bool(re.search(r'[^\s\dA-Z]', s)) :
        result= 'Masukkan Input yang valid: (A-Z, 0-9, spasi)'
        return result
    else:
        consecutive_code_list = []
        consecutive_code_length_list = []
        consecutive_section_index = []

        curr_consecutive = 1
        prev_char = None

        for idx, i in enumerate(s):
            try:
                if i == prev_char:
                    curr_consecutive += 1

                    if (idx == len(s) - 1 or i != s[idx + 1]):
                        if i == ' ' and curr_consecutive >= 2:
                            consecutive_code_list.append(f'r{str(curr_consecutive).translate(SUB)}')
                            consecutive_code_length_list.append(curr_consecutive)
                            consecutive_section_index.append((idx + 1) - curr_consecutive)
                        else:
                            if curr_consecutive >= 3:
                                consecutive_code_list.append(f'r{str(curr_consecutive).translate(SUB)}{i}')
                                consecutive_code_length_list.append(curr_consecutive)
                                consecutive_section_index.append((idx + 1) - curr_consecutive)
                else:
                    curr_consecutive = 1
            except:
                pass

            prev_char = i

        if len(consecutive_code_list)==0:
            return f'n{str(len(s)).translate(SUB)}{s}'

        result_list = []
        temp_non_consecutive = ''

        idx = 0
        temp_idx = 0
        while idx < len(s):
            if idx in consecutive_section_index:
                if (temp_non_consecutive != ''):
                    result_list.append(f'n{str(len(temp_non_consecutive)).translate(SUB)}{temp_non_consecutive}')
                    temp_non_consecutive = ''

                result_list.append(consecutive_code_list[temp_idx])
                idx += consecutive_code_length_list[temp_idx]
                temp_idx += 1
            else:
                temp_non_consecutive += s[idx]
                idx += 1

        return f'''Input: {s}
Hasil Enkode: {' '.join(result_list)}
        '''

if __name__ == '__main__':
    s= str(input())
    # s= 'GGG      BCDEFG  55GHJK LM777777777777'
    # GGG   BCDEFG  555GHJK LM7777777
    print(encode_hdc(s))