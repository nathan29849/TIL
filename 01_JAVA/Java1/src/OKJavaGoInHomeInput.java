import org.opentutorials_iot.DimmingLights;
import org.opentutorials_iot.Elevator;
import org.opentutorials_iot.Lighting;
import org.opentutorials_iot.Security;

import javax.swing.*;


public class OKJavaGoInHomeInput {
    public static void main(String[] args){
        // 남이 만들어 놓은 코드를 활용해 IoT 프로그램 만들기
        // 어떤 일이 시간 순서로 일어나야하는지 생각하기
//        String id = JOptionPane.showInputDialog("Enter a ID");
//        String Bright = JOptionPane.showInputDialog("Enter a Bright level");
        String id = args[0];
        String Bright = args[1];


        // 1. Elevator call
        Elevator myElevator = new Elevator(id);
        myElevator.callForUp(1);

        // 2. Security Off
        Security mySecurity = new Security(id);
        mySecurity.off();

        // 3. Light ON
        Lighting hallLamp = new Lighting(id + " / Hall Lamp");
        hallLamp.on();

        Lighting floorLamp = new Lighting(id+ " / Floor Lamp");
        floorLamp.on();

        DimmingLights moodeLamp = new DimmingLights(id+ " moodLamp");
        moodeLamp.setBright(Double.parseDouble(Bright));
        moodeLamp.on();



    }
}
