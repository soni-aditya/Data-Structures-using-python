'''
Each alphabat from a to z is encoded with an integer from 1 to 26 respectively
Write a program to decode a given encoded input
'''
alpha_map = {}
for index,v in enumerate(range(ord('a'), ord('a') + 26)):
    alpha_map[index] = chr(v)

# inp = '25114' # answer 6
inp = '1111111111' # answer 89
total_possible_decodings = []

def decode_str(inp: str, current_index: int, output: str):
    global total_possible_decodings
    if current_index>= len(inp):
        # print(output)
        total_possible_decodings.append(output)
        return
    
    if (int(inp[current_index])!=0):
        output += alpha_map[int(inp[current_index])]
        decode_str(inp,current_index+1, output)
    if (current_index+1 < len(inp)) and (int(inp[current_index]+inp[current_index+1])<=26):
        output += alpha_map[int(inp[current_index]+inp[current_index+1])]
        decode_str(inp, current_index+2, output)

decode_str(inp,0,"")
print(f"Total possible encodings: {len(total_possible_decodings)}")