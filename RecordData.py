import Leap, sys, thread, time
import csv

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
        data_list = [];

        data1 = "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
              frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))
        print data1;


        f.write(data1 + "\n");

        # Get hands
        #if (len(frame.hands)==1 and len(frame.fingers)==5):
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            data2 = "  %s, id %d, position: %s" % (
                handType, hand.id, hand.palm_position)
            print data2;
            data_list.append("hello");
            data_list.append(handType);
            data_list.append(hand.palm_position[0]);
            data_list.append(hand.palm_position[1]);
            data_list.append(hand.palm_position[2]);

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
            data_list.append(direction.pitch * Leap.RAD_TO_DEG);
            data_list.append(normal.roll * Leap.RAD_TO_DEG);
            data_list.append(direction.yaw * Leap.RAD_TO_DEG);
            f.write(data3 + "\n");

            # Get arm bone
            arm = hand.arm
            data4 = "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
                arm.direction,
                arm.wrist_position,
                arm.elbow_position)
            print data4;
            data_list.append(arm.direction[0]);
            data_list.append(arm.direction[1]);
            data_list.append(arm.direction[2]);
            data_list.append(arm.wrist_position[0]);
            data_list.append(arm.wrist_position[1]);
            data_list.append(arm.wrist_position[2]);
            data_list.append(arm.elbow_position[0]);
            data_list.append(arm.elbow_position[1]);
            data_list.append(arm.elbow_position[2]);
            f.write(data4 + "\n");
            # Get fingers
            for finger in hand.fingers:

                data5 = "    %s finger, id: %d, length: %fmm, width: %fmm, direction: %s" % (
                    self.finger_names[finger.type],
                    finger.id,
                    finger.length,
                    finger.width,finger.direction)
                print data5;
                data_list.append(finger.length);
                data_list.append(finger.width);
                data_list.append(finger.direction[0]);
                data_list.append(finger.direction[1]);
                data_list.append(finger.direction[2]);
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
                    data_list.append(bone.prev_joint[0]);
                    data_list.append(bone.prev_joint[1]);
                    data_list.append(bone.prev_joint[2]);
                    data_list.append(bone.next_joint[0]);
                    data_list.append(bone.next_joint[1]);
                    data_list.append(bone.next_joint[2]);
                    data_list.append(bone.direction[0]);
                    data_list.append(bone.direction[1]);
                    data_list.append(bone.direction[2]);
                    f.write(data6 + "\n");
        if not data_list:
            print "List is empty";
        else:
            with open('data.csv', 'ab') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(data_list);
        if not frame.hands.is_empty:
            print ""
def addHeader():
    header_list = ['result','hand_type','hand_position_x','hand_position_y','hand_position_z','pitch','roll','yaw','arm_direction_x','arm_direction_y','arm_direction_z','wrist_postion_x','wrist_postion_y','wrist_postion_z','elbow_position_x','elbow_position_y','elbow_position_z',
                    'thumb_length',
                    'thumb_width',
                    'thumb_direction_x',
                    'thumb_direction_y',
                    'thumb_direction_z',
                    'thumb_metacarpal_start_x',
                    'thumb_metacarpal_start_y',
                    'thumb_metacarpal_start_z',
                    'thumb_metacarpal_end_x',
                    'thumb_metacarpal_end_y',
                    'thumb_metacarpal_end_z',
                    'thumb_metacarpal_direction_x',
                    'thumb_metacarpal_direction_y',
                    'thumb_metacarpal_direction_z]',
                    'thumb_proximal_start_x',
                    'thumb_proximal_start_y',
                    'thumb_proximal_start_z',
                    'thumb_proximal_end_x',
                    'thumb_proximal_end_y',
                    'thumb_proximal_end_z',
                    'thumb_proximal_direction_x',
                    'thumb_proximal_direction_y',
                    'thumb_proximal_direction_z]',
                    'thumb_intermediate_start_x',
                    'thumb_intermediate_start_y',
                    'thumb_intermediate_start_z',
                    'thumb_intermediate_end_x',
                    'thumb_intermediate_end_y',
                    'thumb_intermediate_end_z',
                    'thumb_intermediate_direction_x',
                    'thumb_intermediate_direction_y',
                    'thumb_intermediate_direction_z]',
                    'thumb_distal_start_x',
                    'thumb_distal_start_y',
                    'thumb_distal_start_z',
                    'thumb_distal_end_x',
                    'thumb_distal_end_y',
                    'thumb_distal_end_z',
                    'thumb_distal_direction_x',
                    'thumb_distal_direction_y',
                    'thumb_distal_direction_z]',
                    'index_length',
                    'index_width',
                    'index_direction_x',
                    'index_direction_y',
                    'index_direction_z',
                    'index_metacarpal_start_x',
                    'index_metacarpal_start_y',
                    'index_metacarpal_start_z',
                    'index_metacarpal_end_x',
                    'index_metacarpal_end_y',
                    'index_metacarpal_end_z',
                    'index_metacarpal_direction_x',
                    'index_metacarpal_direction_y',
                    'index_metacarpal_direction_z]',
                    'index_proximal_start_x',
                    'index_proximal_start_y',
                    'index_proximal_start_z',
                    'index_proximal_end_x',
                    'index_proximal_end_y',
                    'index_proximal_end_z',
                    'index_proximal_direction_x',
                    'index_proximal_direction_y',
                    'index_proximal_direction_z]',
                    'index_intermediate_start_x',
                    'index_intermediate_start_y',
                    'index_intermediate_start_z',
                    'index_intermediate_end_x',
                    'index_intermediate_end_y',
                    'index_intermediate_end_z',
                    'index_intermediate_direction_x',
                    'index_intermediate_direction_y',
                    'index_intermediate_direction_z]',
                    'index_distal_start_x',
                    'index_distal_start_y',
                    'index_distal_start_z',
                    'index_distal_end_x',
                    'index_distal_end_y',
                    'index_distal_end_z',
                    'index_distal_direction_x',
                    'index_distal_direction_y',
                    'index_distal_direction_z]',
                    'middle_length',
                    'middle_width',
                    'middle_direction_x',
                    'middle_direction_y',
                    'middle_direction_z',
                    'middle_metacarpal_start_x',
                    'middle_metacarpal_start_y',
                    'middle_metacarpal_start_z',
                    'middle_metacarpal_end_x',
                    'middle_metacarpal_end_y',
                    'middle_metacarpal_end_z',
                    'middle_metacarpal_direction_x',
                    'middle_metacarpal_direction_y',
                    'middle_metacarpal_direction_z]',
                    'middle_proximal_start_x',
                    'middle_proximal_start_y',
                    'middle_proximal_start_z',
                    'middle_proximal_end_x',
                    'middle_proximal_end_y',
                    'middle_proximal_end_z',
                    'middle_proximal_direction_x',
                    'middle_proximal_direction_y',
                    'middle_proximal_direction_z]',
                    'middle_intermediate_start_x',
                    'middle_intermediate_start_y',
                    'middle_intermediate_start_z',
                    'middle_intermediate_end_x',
                    'middle_intermediate_end_y',
                    'middle_intermediate_end_z',
                    'middle_intermediate_direction_x',
                    'middle_intermediate_direction_y',
                    'middle_intermediate_direction_z]',
                    'middle_distal_start_x',
                    'middle_distal_start_y',
                    'middle_distal_start_z',
                    'middle_distal_end_x',
                    'middle_distal_end_y',
                    'middle_distal_end_z',
                    'middle_distal_direction_x',
                    'middle_distal_direction_y',
                    'middle_distal_direction_z]',
                    'ring_length',
                    'ring_width',
                    'ring_direction_x',
                    'ring_direction_y',
                    'ring_direction_z',
                    'ring_metacarpal_start_x',
                    'ring_metacarpal_start_y',
                    'ring_metacarpal_start_z',
                    'ring_metacarpal_end_x',
                    'ring_metacarpal_end_y',
                    'ring_metacarpal_end_z',
                    'ring_metacarpal_direction_x',
                    'ring_metacarpal_direction_y',
                    'ring_metacarpal_direction_z]',
                    'ring_proximal_start_x',
                    'ring_proximal_start_y',
                    'ring_proximal_start_z',
                    'ring_proximal_end_x',
                    'ring_proximal_end_y',
                    'ring_proximal_end_z',
                    'ring_proximal_direction_x',
                    'ring_proximal_direction_y',
                    'ring_proximal_direction_z]',
                    'ring_intermediate_start_x',
                    'ring_intermediate_start_y',
                    'ring_intermediate_start_z',
                    'ring_intermediate_end_x',
                    'ring_intermediate_end_y',
                    'ring_intermediate_end_z',
                    'ring_intermediate_direction_x',
                    'ring_intermediate_direction_y',
                    'ring_intermediate_direction_z]',
                    'ring_distal_start_x',
                    'ring_distal_start_y',
                    'ring_distal_start_z',
                    'ring_distal_end_x',
                    'ring_distal_end_y',
                    'ring_distal_end_z',
                    'ring_distal_direction_x',
                    'ring_distal_direction_y',
                    'ring_distal_direction_z]',
                    'pinky_length',
                    'pinky_width',
                    'pinky_direction_x',
                    'pinky_direction_y',
                    'pinky_direction_z',
                    'pinky_metacarpal_start_x',
                    'pinky_metacarpal_start_y',
                    'pinky_metacarpal_start_z',
                    'pinky_metacarpal_end_x',
                    'pinky_metacarpal_end_y',
                    'pinky_metacarpal_end_z',
                    'pinky_metacarpal_direction_x',
                    'pinky_metacarpal_direction_y',
                    'pinky_metacarpal_direction_z]',
                    'pinky_proximal_start_x',
                    'pinky_proximal_start_y',
                    'pinky_proximal_start_z',
                    'pinky_proximal_end_x',
                    'pinky_proximal_end_y',
                    'pinky_proximal_end_z',
                    'pinky_proximal_direction_x',
                    'pinky_proximal_direction_y',
                    'pinky_proximal_direction_z]',
                    'pinky_intermediate_start_x',
                    'pinky_intermediate_start_y',
                    'pinky_intermediate_start_z',
                    'pinky_intermediate_end_x',
                    'pinky_intermediate_end_y',
                    'pinky_intermediate_end_z',
                    'pinky_intermediate_direction_x',
                    'pinky_intermediate_direction_y',
                    'pinky_intermediate_direction_z]',
                    'pinky_distal_start_x',
                    'pinky_distal_start_y',
                    'pinky_distal_start_z',
                    'pinky_distal_end_x',
                    'pinky_distal_end_y',
                    'pinky_distal_end_z',
                    'pinky_distal_direction_x',
                    'pinky_distal_direction_y',
                    'pinky_distal_direction_z]'];
    print(len(header_list));
    with open('data.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(header_list);
def main():
    # Create a sample listener and controller
    #uncomment if you want to add header to the csv file.can also be used to clear document with only heading
    #addHeader();

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
