def connect():
    import network

    ssid = "Ali"
    password = "20180427"

    station = network.WLAN(network.STA_IF)
    if not station.isconnected():
        print("menghubungkan ke jaringan WiFI")
    station.active(True)
    station.connect(ssid, password)

    while not station.isconnected():
        pass

    print("koneksi WIFI terhubung")
    print(station.ifconfig())
    print("coba")
