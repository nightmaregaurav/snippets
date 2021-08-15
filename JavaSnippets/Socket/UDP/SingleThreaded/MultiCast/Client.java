/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Client {
    public static void main(String[] args) {
        try{
            // Create A datagram Socket and bind it to local port 8800
            MulticastSocket multicastSocket = new MulticastSocket(8801);
            // Create multicast group
            InetAddress multicastGroup = InetAddress.getByName("230.0.0.0");
            // Joining the Multicast Group
            multicastSocket.joinGroup(multicastGroup);
            // Buffer to store data that is received
            byte[] buffer = new byte[1024];
            // Converting buffer to datagram packet
            DatagramPacket datagramPacket = new DatagramPacket(buffer, buffer.length);
            // Sending the packet
            multicastSocket.receive(datagramPacket);
            // Printing out the message
            System.out.println(new String(buffer));
            // Leave group
            multicastSocket.leaveGroup(multicastGroup);
            // Close the socket
            multicastSocket.close();
        } catch (SocketException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        } catch (UnknownHostException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
