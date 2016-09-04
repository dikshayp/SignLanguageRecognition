################################################################################
# Copyright (C) 2012-2016 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, thread, time

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

f = open("data.txt","w");
deleteContent(f);
class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        data1 = "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
              frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))
        print data1;
        f.write(data1 + "\n");

        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            data2 = "  %s, id %d, position: %s" % (
                handType, hand.id, hand.palm_position)
            print data2;
            f.write(data2 + "\n");

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            data3 = "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
                direction.pitch * Leap.RAD_TO_DEG,
                normal.roll * Leap.RAD_TO_DEG,
                direction.yaw * Leap.RAD_TO_DEG)
            print data3;
            f.write(data3 + "\n");

            # Get arm bone
            arm = hand.arm
            data4 = "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
                arm.direction,
                arm.wrist_position,
                arm.elbow_position)
            print data4;
            f.write(data4 + "\n");
            # Get fingers
            for finger in hand.fingers:

                data5 = "    %s finger, id: %d, length: %fmm, width: %fmm, direction: %s" % (
                    self.finger_names[finger.type],
                    finger.id,
                    finger.length,
                    finger.width,finger.direction)
                print data5;
                f.write(data5 + "\n");

                # Get bones
                for b in range(0, 4):
                    bone = finger.bone(b)
                    data6 = "      Bone: %s, start: %s, end: %s, direction: %s" % (
                        self.bone_names[bone.type],
                        bone.prev_joint,
                        bone.next_joint,
                        bone.direction)
                    print data6;
                    f.write(data6 + "\n");

        if not frame.hands.is_empty:
            print ""

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)
        #f.close();



if __name__ == "__main__":
    main()
