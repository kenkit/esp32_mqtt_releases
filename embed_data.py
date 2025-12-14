import os

def add_embed_files_to_platformio_ini():
    with open('Blink/platformio.ini', 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if not line.strip().startswith('board_build.embed_files'):
            new_lines.append(line)

    in_env_section = False
    for i, line in enumerate(new_lines):
        if line.strip() == '[env:esp8266]':
            in_env_section = True
        elif in_env_section and line.strip().startswith('['):
            new_lines.insert(i, 'board_build.embed_files = data/certs.ar\n')
            in_env_section = False
            break

    if in_env_section:
        new_lines.append('board_build.embed_files = data/certs.ar\n')


    with open('Blink/platformio.ini', 'w') as f:
        f.writelines(new_lines)

if __name__ == '__main__':
    add_embed_files_to_platformio_ini()
    print("Successfully added the data directory to platformio.ini")

