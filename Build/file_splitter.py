chunk_size = 50 * 1024 * 1024  # 50MB

with open("Sky-Down_web.data", "rb") as f:
    i = 0

    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break

        with open(f"game.part.{i:03}.bin", "wb") as out:
            out.write(chunk)

        i += 1