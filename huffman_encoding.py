chars = input("Enter characters: ").split()
freq = list(map(int, input("Enter frequencies: ").split()))

nodes = []

for i in range(len(chars)):
    nodes.append([freq[i], chars[i]])

while len(nodes) > 1:

    nodes.sort()

    left = nodes.pop(0)
    right = nodes.pop(0)

    new_node = [
        left[0] + right[0],
        [left[1], right[1]]
    ]

    nodes.append(new_node)


def print_codes(node, code=""):

    if isinstance(node, str):
        print(node, ":", code if code else "0")
        return

    print_codes(node[0], code + "0")
    print_codes(node[1], code + "1")


print("Huffman Codes:")
print_codes(nodes[0][1])
