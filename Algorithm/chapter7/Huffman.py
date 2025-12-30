# https://ko.wikipedia.org/wiki/%ED%97%88%ED%94%84%EB%A8%BC_%EB%B6%80%ED%98%B8%ED%99%94
# http://velog.io/@junhok82/%ED%97%88%ED%94%84%EB%A7%8C-%EC%BD%94%EB%94%A9Huffman-coding
import heapq
import itertools
from collections import defaultdict

def huffman_encoder(data):
    data = data.encode('utf-8')
    frequencies = defaultdict(int)
    for byte in data:
        frequencies[byte] += 1
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)
    encoded_data = ''.join(huffman_codes[byte] for byte in data)
    return encoded_data, huffman_codes

def huffman_decoder(encoded_data, huffman_codes):
    reverse_huffman_codes = {v: k for k, v in huffman_codes.items()}
    current_code = ''
    decoded_bytes = bytearray()
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_huffman_codes:
            decoded_bytes.append(reverse_huffman_codes[current_code])
            current_code = ''
    return decoded_bytes.decode('utf-8')

def build_huffman_tree(frequencies):
    # Use a tie-breaker counter so heap entries remain comparable
    heap = []
    counter = itertools.count()
    for symbol, weight in frequencies.items():
        heapq.heappush(heap, (weight, next(counter), symbol))
    if not heap:
        return []
    while len(heap) > 1:
        w1, _, node1 = heapq.heappop(heap)
        w2, _, node2 = heapq.heappop(heap)
        heapq.heappush(heap, (w1 + w2, next(counter), [node1, node2]))
    return heap[0][2]

def generate_huffman_codes(huffman_tree, prefix='', codebook=None):
    if codebook is None:
        codebook = {}
    # Leaf is an integer (byte)
    if isinstance(huffman_tree, int):
        codebook[huffman_tree] = prefix or '0'
    # Internal node is a list of two elements: [left, right]
    elif isinstance(huffman_tree, list) and len(huffman_tree) == 2:
        left, right = huffman_tree
        generate_huffman_codes(left, prefix + '0', codebook)
        generate_huffman_codes(right, prefix + '1', codebook)
    # Handle single-element wrappers if any
    elif isinstance(huffman_tree, list) and len(huffman_tree) == 1:
        generate_huffman_codes(huffman_tree[0], prefix, codebook)
    return codebook

def main():
    data = "this is an example for huffman encoding"
    encoded_data, huffman_codes = huffman_encoder(data)
    print("Encoded:", encoded_data)
    print("Codes:", huffman_codes)
    decoded_data = huffman_decoder(encoded_data, huffman_codes)
    print("Decoded:", decoded_data)

if __name__ == "__main__":
    main()

