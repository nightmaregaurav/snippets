import java.net.NetworkInterface;
import java.net.SocketException;
import java.util.Arrays;
import java.util.Enumeration;
import java.util.logging.Level;
import java.util.logging.Logger;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author nightmare
 */
public class NetworkInterfaceEx {
    public static void main(String[] args) {
        try {
            Enumeration<NetworkInterface> networkInterface = NetworkInterface.getNetworkInterfaces();
            int i = 0;
            while(networkInterface.hasMoreElements()){
                System.out.println(i);
                i++;
                NetworkInterface _interface = networkInterface.nextElement();
                System.out.println("\tgetDisplayName: " + _interface.getDisplayName());
                System.out.println("\tgetName: " + _interface.getName());
                System.out.println("\ttoString: " + _interface.toString());
                System.out.println("\tgetHardwareAddress: " + Arrays.toString(_interface.getHardwareAddress()));
                System.out.println("\tgetIndex: " + _interface.getIndex());
                System.out.println("\tgetInetAddresses: " + _interface.getInetAddresses());
                System.out.println("\tgetInterfaceAddresses: " + _interface.getInterfaceAddresses());
                System.out.println("\tgetMTU: " + _interface.getMTU());
                System.out.println("\tgetParent: " + _interface.getParent());
                System.out.println("\tgetSubInterfaces: " + _interface.getSubInterfaces());
                System.out.println("\tisLoopback: " + _interface.isLoopback());
                System.out.println("\thashCode: " + _interface.hashCode());
                System.out.println("\tinetAddresses: " + _interface.inetAddresses());
                System.out.println("\tisPointToPoint: " + _interface.isPointToPoint());
                System.out.println("\tisUp: " + _interface.isUp());
                System.out.println("\tisVirtual: " + _interface.isVirtual());
                System.out.println("\tsupportsMulticast: " + _interface.supportsMulticast());
                System.out.println("\tsubInterfaces: " + _interface.subInterfaces());
            }
        } catch (SocketException ex) {
            Logger.getLogger(NetworkInterfaceEx.class.getName()).log(Level.SEVERE, null, ex);
        } 
    }
}

