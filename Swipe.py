import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SwipeListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    alarm = 0
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        gesture_detected = False;
        fingerA_x=0;
        fingerB_x=0;
        for hand in frame.hands:
            for finger in hand.fingers:
                if self.finger_names[finger.type] == 'Thumb':
                    #fingerA_x = finger.x;
                    position = finger.tip_position;
                    fingerA_x = position[0];
                elif self.finger_names[finger.type] == 'Index':
                    #fingerB_x = finger.x;
                    position = finger.tip_position;
                    fingerB_x = position[0];
        if fingerA_x!=0 and fingerB_x!=0 and abs(fingerA_x - fingerB_x) < 20:
            gesture_detected = True;
            print "pinch detected";
            print "fingerA_x: %s and fingerB_x: %s"% (fingerA_x, fingerB_x);
        else :
            print "pinch  not detected";
            print "fingerA_x: %s and fingerB_x: %s"% (fingerA_x, fingerB_x);
        '''if not frame.hands.is_empty:
            for gesture in frame.gestures():
                if gesture.type == Leap.Gesture.TYPE_SWIPE:
                    swipe = SwipeGesture(gesture)

                    if swipe.direction[0] > 0.5 and self.alarm < time.time():
                        self.alarm = time.time() + 1.00
                        print "Right"
                    if swipe.direction[0] < -0.5 and self.alarm < time.time():
                        self.alarm = time.time() + 1.00
                        print "Left"
                    if swipe.direction[1] > 0.5 and self.alarm < time.time():
                        self.alarm = time.time() + 1.00
                        print "Forward"
                    if swipe.direction[1] < -0.5 and self.alarm < time.time():
                        self.alarm = time.time() + 1.00
                        print "Backward"
                if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP and self.alarm < time.time():
                        self.alarm = time.time() + 1.00
                        print "Stop"
                if gesture.type == Leap.Gesture.TYPE_KEY_TAP and self.alarm < time.time():
                        self.alarm = time.time() + 1.00
                        print "Stop"
                        '''
'''
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"
'''

def main():
    print "swipe right for turning right"
    print "swipe left for turning left"
    print "swipe up for going forward"
    print "swipe down for going backward"
    print "key/screen tap for stopping"
    print ""

    # Create a sample listener and controller
    listener = SwipeListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    #print "Press Enter to quit..."
    sys.stdin.readline()

    # Remove the sample listener when done
    controller.remove_listener(listener)


if __name__ == "__main__":
    main()
