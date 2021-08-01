import speedtest

st = speedtest.Speedtest()
st.get_best_server()

print ("*** SPEED TEST ***")
print(f"Pin {st.results.ping} ms")
print(f"Download speed: {round(st.download() / 1000 / 1000, 1)} Mbit/s")
print(f"Upload speed: {round(st.upload() / 1000 / 1000, 1)} Mbit/s")