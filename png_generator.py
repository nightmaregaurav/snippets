#!/usr/bin/env python3

# Generates PNG without using any fancy libraries.
import struct
import zlib

def create_png(output_path):
    # This function writes a PNG file from scratch using raw bytes.
    # It creates a tiny 4x4 image (16 pixels total) with 3 alternating colors using a palette.
    # No image libraries are used — just binary operations!

    # ---------------------------------------------
    # PNG SIGNATURE (first 8 bytes of any PNG file)
    # This lets programs know: "Hey! I'm a PNG image!"
    # These 8 bytes must always come first in a PNG file.
    # \x89 is a special non-text byte to tell it's not a text file
    png_signature = b'\x89PNG\r\n\x1a\n'

    # ---------------------------------------------
    # IHDR CHUNK — Image Header
    # This chunk tells the image's width, height, color mode, etc.
    width = 4
    height = 4
    bit_depth = 8          # 8 bits per pixel (1 byte)
    color_type = 3         # "3" means we're using a color palette (PLTE chunk)
    compression = 0        # Always 0 for PNG (zlib compression)
    filter_method = 0      # Always 0 (adaptive filter method)
    interlace = 0          # 0 = no interlacing (simple image layout)

    # We pack these numbers into a byte sequence using big-endian ("!" means big-endian)
    ihdr_data = struct.pack("!IIBBBBB", width, height, bit_depth, color_type,
                            compression, filter_method, interlace)

    # Wrap the IHDR chunk using our helper
    ihdr_chunk = create_chunk(b'IHDR', ihdr_data)

    # ---------------------------------------------
    # PLTE CHUNK — Color Palette
    # We're going to define 3 colors: red, green, and blue.
    # Each color is made of 3 bytes (R, G, B)
    palette = [
        255, 0, 0,    # Color 0: Red
        0, 255, 0,    # Color 1: Green
        0, 0, 255     # Color 2: Blue
    ]

    # A PNG palette can hold up to 256 colors. We pad with 0s(black color) to reach that.
    # This is optional
    palette += [0, 0, 0] * (256 - len(palette) // 3)
    plte_chunk = create_chunk(b'PLTE', bytes(palette))

    # ---------------------------------------------
    # tRNS CHUNK — Transparency
    # Let's say all 3 colors are fully opaque (255 = no transparency)
    trns_data = bytes([255, 255, 255])
    trns_chunk = create_chunk(b'tRNS', trns_data)

    # ---------------------------------------------
    # IDAT CHUNK — Image Data (Pixels!)
    # Each row of pixels starts with a "filter byte" — we use 0 (no filter)
    # Then we write the pixel indices using our palette.
    # We'll alternate colors like this across 4 rows:
    # Row 1: 0 1 2 0
    # Row 2: 1 2 0 1
    # Row 3: 2 0 1 2
    # Row 4: 0 1 2 0
    pixel_rows = [
        [0, 1, 2, 0],
        [1, 2, 0, 1],
        [2, 0, 1, 2],
        [0, 1, 2, 0]
    ]

    raw_image_data = bytearray()
    for row in pixel_rows:
        raw_image_data.append(0)       # Filter byte (0 = no filter)
        raw_image_data.extend(row)     # Add the actual pixels (indices into palette)

    # Now compress the raw pixel bytes using zlib
    compressed_data = zlib.compress(bytes(raw_image_data))
    idat_chunk = create_chunk(b'IDAT', compressed_data)

    # ---------------------------------------------
    # IEND CHUNK — Image End
    # Marks the end of the PNG file. Required.
    iend_chunk = create_chunk(b'IEND', b'')

    # ---------------------------------------------
    # Finally, write the complete PNG file
    with open(output_path, 'wb') as f:
        f.write(png_signature)
        f.write(ihdr_chunk)
        f.write(plte_chunk)
        f.write(trns_chunk)
        f.write(idat_chunk)
        f.write(iend_chunk)

# Helper function to make a PNG chunk (wraps data in the proper format)
def create_chunk(chunk_type, data):
    # chunk_type is something like b'IHDR' or b'IDAT'
    length = struct.pack("!I", len(data))                       # 4-byte length of data
    crc = struct.pack("!I", zlib.crc32(chunk_type + data) & 0xffffffff)  # 4-byte CRC
    return length + chunk_type + data + crc                    # Full chunk = length + type + data + CRC

# Run the function to create the image
create_png("./alternating_colors.png")
