def get_urls_from_text(text: str) -> bool:
    regex = r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]
                [.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(
                \([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\
                ()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))""".strip()
    return [x[0] for x in findall(regex, str(text))]


  def test_speedtest():
    def speed_convert(size):
        power = 2 ** 10
        zero = 0
        units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
        while size > power:
            size /= power
            zero += 1
        return f"{round(size, 2)} {units[zero]}"
