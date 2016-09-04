import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

def ok_detect(self, controller):
    gesture_detected = False;
    thumb_x = 0;
    thumb_y = 0;
    thumb_z = 0;
    other_x = 0;
    other_y = 0;
    other_z = 0;
    avg_x = 0;
    avg_y = 0;
    avg_z = 0;
    frame = controller.frame();
    for hand in frame.hands:
        for finger in hand.fingers:
            if self.finger_names[finger.type] == 'Thumb':
                direction_vector = finger.direction;
                thumb_x = direction_vector[0];
                thumb_y = direction_vector[1];
                thumb_z = direction_vector[2];
            else:
                direction_vector = finger.direction;
                if other_x == 0:
                    other_x = direction_vector[0];
                else :
                    if abs(other_x - direction_vector[0]) > 0.6:
                        return False;
                    other_x = direction_vector[0];
                if other_y == 0:
                    other_y = direction_vector[1];
                else :
                    if abs(other_y - direction_vector[1]) > 0.6:
                        return False;
                    other_y = direction_vector[1];
                if other_z == 0:
                    other_z = direction_vector[2];
                else :
                    if abs(other_z - direction_vector[2]) > 0.6:
                        return False;
                    other_z = direction_vector[2];
                avg_x += other_x;
                avg_y += other_y;
                avg_z += other_z;
        avg_x = avg_x/4;
        avg_y = avg_y/4;
        avg_z = avg_z/4;
        if abs(thumb_z - avg_z) > 1.5:
            gesture_detected = True;
    return gesture_detected;


def hello_detect(self, controller):
    frame = controller.frame();
    gesture_detected = False;
    for hand in frame.hands:
        prev_avg_x = 0;
        curr_avg_x = 0;
        prev_avg_y = 0;
        curr_avg_y = 0;
        prev_avg_z = 0;
        curr_avg_z = 0;
        x_plane = True;
        y_plane = True;
        z_plane = True;
        for finger in hand.fingers:
            for b in range(0,4):
                bone = finger.bone(b);
                prev_joint = bone.prev_joint;
                next_joint = bone.next_joint;
                if abs(prev_joint[0] - next_joint[0]) > 20:
                    x_plane = False;
                if abs(prev_joint[1] - next_joint[1]) > 20:
                    y_plane = False;
                if abs(prev_joint[2] - next_joint[2]) > 20:
                    z_plane = False;
                curr_avg_x += prev_joint[0];
                curr_avg_y += prev_joint[1];
                curr_avg_z += prev_joint[2];
            curr_avg_x = curr_avg_x/4;
            curr_avg_y = curr_avg_y/4;
            curr_avg_z = curr_avg_z/4;
            if x_plane == True:
                if prev_avg_x !=0:
                    if abs(prev_avg_x - curr_avg_x) > 50:
                        x_plane = False;
            prev_avg_x = curr_avg_x;
            if y_plane == True:
                if prev_avg_y !=0:
                    if abs(prev_avg_y - curr_avg_y) > 50:
                        y_plane = False;
            prev_avg_y = curr_avg_y;
            if z_plane == True:
                if prev_avg_z !=0:
                    if abs(prev_avg_z - curr_avg_z) > 50:
                        z_plane = False;
            prev_avg_z = curr_avg_z;
        return x_plane or y_plane or z_plane;



def pinch_detect(self, controller):
    frame = controller.frame();
    gesture_detected = False;
    fingerA_x=0;
    fingerB_x=0;
    fingerA_y=0;
    fingerB_y=0;
    fingerA_z=0;
    fingerB_z=0;
    for hand in frame.hands:
        for finger in hand.fingers:
            if self.finger_names[finger.type] == 'Thumb':
                position = finger.tip_position;
                fingerA_x = position[0];
                fingerA_y = position[1];
                fingerA_z = position[2];
            elif self.finger_names[finger.type] == 'Index':
                position = finger.tip_position;
                fingerB_x = position[0];
                fingerB_y = position[1];
                fingerB_z = position[2];
    if fingerA_x!=0 and fingerB_x!=0 and abs(fingerA_x - fingerB_x) < 20 and abs(fingerA_y - fingerB_y) < 20 and abs(fingerA_z - fingerB_z) < 20:
        gesture_detected = True;
    return gesture_detected;

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
        pinch = pinch_detect(self, controller);
        if pinch:
            print "pinch detected";
        hello = hello_detect(self, controller);
        if hello:
            print "hello detected";
        ok = ok_detect(self, controller);
        if ok:
            print "ok detected";

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
