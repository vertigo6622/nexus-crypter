import sys
import os

bin_path = sys.argv[1]
# finds mingw compiler nonsense and truncates file
marker_bytes = bytes.fromhex("417267756D656E7420646F6D61696E20")

with open(bin_path, 'rb') as f:
    content = f.read()

marker_index = content.find(marker_bytes)

if marker_index == -1:
    print("Error: Marker not found.")
    sys.exit(1)

print(f"Found marker at offset 0x{marker_index:x}")
new_size = marker_index

with open(bin_path, 'wb') as f:
    f.truncate(new_size)
    f.write(content[:new_size])

print(f"Truncated {bin_path} to {new_size} bytes.")

# removes libgcc markers
junk_hex = "6C69626763635F735F6477322D312E646C6C005F5F72656769737465725F6672616D655F696E666F005F5F646572656769737465725F6672616D655F696E666F"
junk_bytes = bytes.fromhex(junk_hex)

with open(bin_path, 'r+b') as f:
    content = bytearray(f.read())
    
    index = content.find(junk_bytes)
    
    if index != -1:
        print(f"Found libgcc junk at offset 0x{index:x}")
        for i in range(len(junk_bytes)):
            content[index + i] = 0
        f.seek(0)
        f.write(content)
        print("Junk successfully zeroed.")
    else:
        print("libgcc junk not found.")
