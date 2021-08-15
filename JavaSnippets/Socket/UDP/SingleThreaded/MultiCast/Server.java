/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author nightmare
 */
public class Server {
    public static void main(String[] args) {
        try {
            DatagramSocket socket = new DatagramSocket(8800);
            // Create multicast group address object
            InetAddress multicastGroup = InetAddress.getByName("230.0.0.0");
            // Message
            byte[] buffer = "Hi clients".getBytes();
            // Converting buffer to datagram packet
            DatagramPacket datagramPacket = new DatagramPacket(buffer, buffer.length, multicastGroup, 8801);
            // Sending the packet
            socket.send(datagramPacket);
            // Close socket connection
            socket.close();
        } catch (SocketException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        } catch (UnknownHostException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
