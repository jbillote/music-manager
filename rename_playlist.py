from pathlib import Path
import sys

if len(sys.argv) < 2:
    print("Missing arguments")
    sys.exit(1)

playlist = sys.argv[1]
playlist_name = Path(playlist).stem

with open(playlist, 'r', encoding='utf-8') as f:
    songs = f.readlines()

r4_lines = []
a306_lines = []

for song in songs:
    unix_formatted = song.replace("\\", "/")
    r4_lines.append(unix_formatted.replace("D:", "/storage/5B82-0808"))
    a306_lines.append(unix_formatted.replace("D:", "/storage/emulated/0"))

r4_path = Path(f"output/r4/{playlist_name}.m3u")
r4_path.parent.mkdir(parents=True, exist_ok=True)
r4_path.write_text("".join(r4_lines), encoding="utf-8")

a306_path = Path(f"output/a306/{playlist_name}.m3u")
a306_path.parent.mkdir(parents=True, exist_ok=True)
a306_path.write_text("".join(a306_lines), encoding="utf-8")
