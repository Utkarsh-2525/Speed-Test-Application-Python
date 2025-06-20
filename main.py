import speedtest
import time
import pyttsx3

def speak(message):
    try:
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()
    except Exception as e:
        print(f"(Voice error): {e}")

def test_internet_speed():
    print("🧠 SYSTEM ONLINE")
    print("🔒 Accessing terminal...")
    print("🛰️  Establishing connection...\n")

    welcome_msg = "🤖: 🟢 WELCOME | MR. UTKARSH MISHRA | SYSTEM INITIALIZED ✅"
    print(welcome_msg)
    speak("Welcome, M.Utkarsh, \nSystem initialized and ready.")

    time.sleep(1)

    print("\n📡 Scanning for optimal server...")
    st = speedtest.Speedtest()
    best_server = st.get_best_server()
    print(f"📍 Server selected: {best_server['host']} ({best_server['country']})")
    speak(f"Best server located in {best_server['country']} has been selected.")

    print("\n📥 Testing download speed...")
    download_speed = st.download() / 1_000_000

    print("📤 Testing upload speed...")
    upload_speed = st.upload() / 1_000_000

    ping_result = st.results.ping

    print("\n📶 INTERNET SPEED TEST RESULTS:")
    print(f"⬇️  Download: {download_speed:.2f} Mbps")
    print(f"⬆️  Upload:   {upload_speed:.2f} Mbps")
    print(f"📶  Ping:      {ping_result:.2f} ms")

    speak("Internet speed test complete. Reporting results.")
    speak(f"Download speed is {download_speed:.2f} megabits per second.")
    speak(f"Upload speed is {upload_speed:.2f} megabits per second.")
    speak(f"Ping is {ping_result:.2f} milliseconds.")

if __name__ == "__main__":
    test_internet_speed()
