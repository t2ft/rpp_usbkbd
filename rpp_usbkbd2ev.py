import struct
import time


# path to Keyboard-Event-Device (might be adjusted)
EVENT_DEV = '/dev/input/event4'
# path to Touch-Event-Device (might be adjusted)
TOUCH_DEV = '/dev/input/event3'

# Event-Format: timeval(sec,usec), type, code, value
EVENT_FORMAT = 'llHHi'
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

EV_KEY = 0x01
KEY_PRESS = 1
KEY_RELEASE = 0

# Keycodes
KEY_J = 36    # 'j' key
KEY_K = 37    # 'k' key

# Emit a touch event to the input device using struct
def emit_event(device, event_type, event_code, event_value):
    event = struct.pack('llHHi', int(time.time()), int((time.time() % 1) * 1e6), event_type, event_code, event_value)
    device.write(event)
    device.flush()

# Swipe left function
def swipe_from_bottom():
    with open(TOUCH_DEV, "wb") as device:
        try:
            # Simulate touch down at starting position (right side)
            emit_event(device, 3, 53, 1500)  # ABS_MT_POSITION_X (X coordinate, starting at the right)
            emit_event(device, 3, 54, 0)  # ABS_MT_POSITION_Y (Y coordinate, middle of the screen)
            emit_event(device, 3, 57, 1)     # ABS_MT_TRACKING_ID (New touch ID)
            emit_event(device, 1, 330, 1)    # BTN_TOUCH (touch down)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Short delay to simulate the touch action
            time.sleep(0.05)

            # Simulate movement to the left (swipe)
            emit_event(device, 3, 54, 300)  # Move to X = 1200
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Simulate touch up (lift finger)
            emit_event(device, 1, 330, 0)    # BTN_TOUCH (touch up)
            emit_event(device, 3, 57, -1)    # ABS_MT_TRACKING_ID (End touch)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

        finally:
            device.close()    

def swipe_from_top():
    with open(TOUCH_DEV, "wb") as device:
        try:
            # Simulate touch down at starting position (right side)
            emit_event(device, 3, 53, 500)  # ABS_MT_POSITION_X (X coordinate, starting at the right)
            emit_event(device, 3, 54, 1800)  # ABS_MT_POSITION_Y (Y coordinate, middle of the screen)
            emit_event(device, 3, 57, 1)     # ABS_MT_TRACKING_ID (New touch ID)
            emit_event(device, 1, 330, 1)    # BTN_TOUCH (touch down)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Short delay to simulate the touch action
            time.sleep(0.05)

            # Simulate movement to the left (swipe)
            emit_event(device, 3, 54, 1500)  # Move to X = 1200
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Simulate touch up (lift finger)
            emit_event(device, 1, 330, 0)    # BTN_TOUCH (touch up)
            emit_event(device, 3, 57, -1)    # ABS_MT_TRACKING_ID (End touch)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

        finally:
            device.close()               

# Swipe left function
def swipe_left():
    with open(TOUCH_DEV, "wb") as device:
        try:
            # Simulate touch down at starting position (right side)
            emit_event(device, 3, 53, 1500)  # ABS_MT_POSITION_X (X coordinate, starting at the right)
            emit_event(device, 3, 54, 1000)  # ABS_MT_POSITION_Y (Y coordinate, middle of the screen)
            emit_event(device, 3, 57, 1)     # ABS_MT_TRACKING_ID (New touch ID)
            emit_event(device, 1, 330, 1)    # BTN_TOUCH (touch down)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Short delay to simulate the touch action
            time.sleep(0.05)

            # Simulate movement to the left (swipe)
            emit_event(device, 3, 53, 1200)  # Move to X = 1200
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Simulate touch up (lift finger)
            emit_event(device, 1, 330, 0)    # BTN_TOUCH (touch up)
            emit_event(device, 3, 57, -1)    # ABS_MT_TRACKING_ID (End touch)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

        finally:
            device.close()

# Swipe right function
def swipe_right():
    with open(TOUCH_DEV, "wb") as device:
        try:
            # Simulate touch down at starting position (left side)
            emit_event(device, 3, 53, 500)   # ABS_MT_POSITION_X (X coordinate, starting at the left)
            emit_event(device, 3, 54, 1000)  # ABS_MT_POSITION_Y (Y coordinate, middle of the screen)
            emit_event(device, 3, 57, 1)     # ABS_MT_TRACKING_ID (New touch ID)
            emit_event(device, 1, 330, 1)    # BTN_TOUCH (touch down)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Short delay to simulate the touch action
            time.sleep(0.05)

            # Simulate movement to the right (swipe)
            emit_event(device, 3, 53, 900)   # Move to X = 900
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

            # Simulate touch up (lift finger)
            emit_event(device, 1, 330, 0)    # BTN_TOUCH (touch up)
            emit_event(device, 3, 57, -1)    # ABS_MT_TRACKING_ID (End touch)
            emit_event(device, 0, 0, 0)      # EV_SYN (sync event)

        finally:
            device.close()

# main function
def main():
    print("Event-Listener is starting...")
    first_retry = True
    while True:
        try:
            with open(EVENT_DEV, 'rb') as f:
                print("EVENT_DEV is now available");
                first_retry = True
                while True:
                    data = f.read(EVENT_SIZE)
                    if not data:
                        break

                    tv_sec, tv_usec, ev_type, code, value = struct.unpack(EVENT_FORMAT, data)

                    if ev_type == EV_KEY and value == KEY_PRESS:
                        if code == KEY_J:
                            print("next page")
                            swipe_right()
                        elif code == KEY_K:
                            print("previous page")
                            swipe_left()
        except IOError:
            if first_retry:
                print("IOError, retry after short delay")
                first_retry = False
            time.sleep(2)
            

if __name__ == "__main__":
    main()
