from main import check_warnings

def test_ram_warning():
    result = check_warnings("RAM",87)

    assert result == "WARNING : RAM USAGE HIGH"

def test_cpu_warning():
    result = check_warnings("CPU",82)

    assert result == "WARNING : CPU USAGE HIGH"

def test_disk_warning():
    result = check_warnings("DISK",92)

    assert result == "WARNING : DISK USAGE HIGH"

def test_ram_at_threshold():
    result = check_warnings("RAM",85)

    assert result is None